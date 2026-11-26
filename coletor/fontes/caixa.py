"""Coletor da Caixa: lista oficial de imóveis por UF (CSV)."""
import re
import datetime
from pathlib import Path
import requests
from ..modelo import Anuncio, numero_br, area, tipo_padrao
from ..escopo import no_escopo

URL = "https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_{uf}.csv"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/130.0 Safari/537.36",
    "Referer": "https://venda-imoveis.caixa.gov.br/sistema/download-lista.asp",
}

def baixar(uf: str) -> str:
    r = requests.get(URL.format(uf=uf), headers=HEADERS, timeout=60)
    r.raise_for_status()
    texto = r.content.decode("latin-1")
    if "Lista de Im" not in texto[:500]:
        raise RuntimeError(f"Caixa não devolveu a lista de {uf} (status {r.status_code}, "
                           f"{len(texto)} bytes). Início: {texto[:300]!r}")
    return texto

def parse(texto: str):
    for linha in texto.splitlines():
        if not re.match(r"\s*\d{8,}", linha):
            continue
        c = [x.strip() for x in linha.split(";")]
        if len(c) < 12:
            continue
        num, uf, cidade, bairro, end, preco, aval, desc_pct, fin, descricao, modalidade, link = c[:12]
        tipo = tipo_padrao(descricao.split(",")[0])
        qto = re.search(r"(\d+)\s*qto", descricao)
        vaga = re.search(r"(\d+)\s*vaga", descricao, re.I)
        yield Anuncio(
            fonte="caixa", id_fonte=num, url=link, uf=uf, cidade=cidade, bairro=bairro, endereco=end,
            tipo=tipo, descricao=descricao,
            area_privativa=area(descricao, "privativa"), area_total=area(descricao, "total"),
            area_terreno=area(descricao, "do terreno"),
            quartos=int(qto.group(1)) if qto else None, vagas=int(vaga.group(1)) if vaga else None,
            avaliacao=numero_br(aval), preco_atual=numero_br(preco),
            desconto=numero_br(desc_pct), modalidade=modalidade,
            financiamento=(fin.lower().startswith("s")) if fin else None,
        )

ENTRADA = Path(__file__).resolve().parents[2] / "entrada" / "caixa"
MAX_DIAS = 3

def data_geracao(texto: str):
    m = re.search(r"Data de gera\S*:;\s*(\d{2})/(\d{2})/(\d{4})", texto[:600])
    return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None

def da_entrada(uf: str) -> str:
    """Lista entregue pelo Grokbot (baixada no Mac do Sergio, pela internet de casa)."""
    f = ENTRADA / f"Lista_imoveis_{uf}.csv"
    if not f.exists():
        raise RuntimeError(f"Sem lista da Caixa para {uf}: o site bloqueou e não há arquivo em entrada/caixa/")
    texto = f.read_bytes().decode("latin-1")
    d = data_geracao(texto)
    if d is None or (datetime.date.today() - d).days > MAX_DIAS:
        raise RuntimeError(f"Lista da Caixa {uf} em entrada/ está velha (gerada em {d}); o Grokbot não enviou a de hoje")
    print(f"caixa {uf}: usando lista entregue pelo Grokbot, gerada em {d:%d/%m/%Y}")
    return texto

def obter(uf: str) -> str:
    try:
        return baixar(uf)
    except Exception as e:
        print(f"caixa {uf}: download direto falhou ({str(e)[:80]}); tentando entrada/caixa/")
        return da_entrada(uf)

def coletar(ufs=("PA", "MA")):
    for uf in ufs:
        for a in parse(obter(uf)):
            if no_escopo(a.uf, a.cidade, a.tipo):
                yield a
