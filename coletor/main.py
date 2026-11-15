"""Roda todas as fontes, guarda o resultado e registra mudanças de preço.

Uso: python -m coletor.main
Saídas:
  dados/anuncios.json        -> foto do dia (todos os anúncios ativos)
  dados/historico.jsonl      -> uma linha por novidade (novo, mudou preço, saiu)
  Supabase (opcional)        -> se SUPABASE_URL e SUPABASE_KEY estiverem definidos
"""
import json, os, sys, datetime, traceback
from pathlib import Path
from .fontes import caixa

FONTES = {"caixa": caixa.coletar}
DADOS = Path(__file__).resolve().parent.parent / "dados"

def agora():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

def carregar_anterior():
    f = DADOS / "anuncios.json"
    if not f.exists():
        return {}
    return {a["chave"]: a for a in json.loads(f.read_text(encoding="utf-8"))}

def enviar_supabase(anuncios, eventos):
    url, key = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")
    if not (url and key):
        print("Supabase não configurado: pulando envio.")
        return
    import requests
    h = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json",
         "Prefer": "resolution=merge-duplicates,return=minimal"}
    for i in range(0, len(anuncios), 500):
        r = requests.post(f"{url}/rest/v1/anuncios?on_conflict=chave", headers=h, json=anuncios[i:i+500], timeout=60)
        r.raise_for_status()
    if eventos:
        r = requests.post(f"{url}/rest/v1/historico", headers={**h, "Prefer": "return=minimal"}, json=eventos, timeout=60)
        r.raise_for_status()

def main():
    DADOS.mkdir(exist_ok=True)
    anterior = carregar_anterior()
    hoje, eventos, falhas = {}, [], []
    for nome, coletar in FONTES.items():
        try:
            n = 0
            for a in coletar():
                d = a.dict()
                old = anterior.get(d["chave"])
                d["visto_primeiro"] = old["visto_primeiro"] if old else agora()
                d["visto_ultimo"] = agora()
                d["ativo"] = True
                if not old:
                    eventos.append({"chave": d["chave"], "quando": agora(), "evento": "novo", "preco": d["preco_atual"]})
                elif old.get("preco_atual") != d["preco_atual"]:
                    eventos.append({"chave": d["chave"], "quando": agora(), "evento": "preco",
                                    "preco_antes": old.get("preco_atual"), "preco": d["preco_atual"]})
                hoje[d["chave"]] = d
                n += 1
            print(f"{nome}: {n} anúncios no escopo")
        except Exception:
            falhas.append(nome)
            traceback.print_exc()
            # mantém os anúncios dessa fonte do dia anterior para não "sumirem" por erro de coleta
            for k, v in anterior.items():
                if v["fonte"] == nome:
                    hoje[k] = v
    for k, v in anterior.items():
        if k not in hoje and v.get("ativo"):
            v = {**v, "ativo": False, "saiu_em": agora()}
            hoje[k] = v
            eventos.append({"chave": k, "quando": agora(), "evento": "saiu", "preco": v.get("preco_atual")})
    lista = sorted(hoje.values(), key=lambda x: (x["uf"], x["cidade"], x["tipo"], x["chave"]))
    (DADOS / "anuncios.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(DADOS / "historico.jsonl", "a", encoding="utf-8") as f:
        for e in eventos:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    enviar_supabase(lista, eventos)
    ativos = sum(1 for x in lista if x["ativo"])
    print(f"Total ativos: {ativos} | eventos: {len(eventos)} | fontes com falha: {falhas or 'nenhuma'}")
    return 1 if falhas and len(falhas) == len(FONTES) else 0

if __name__ == "__main__":
    sys.exit(main())
