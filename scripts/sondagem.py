"""Testa quais fontes respondem a partir do servidor de coleta (sem burlar nada)."""
import requests
SITES = {
 "caixa": "https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_PA.csv",
 "vip": "https://www.vipleiloes.com.br/", "norte": "https://www.norteleiloes.com.br/",
 "maestro": "https://www.maestroleiloes.com.br/", "leilo": "https://www.leilo.com.br/",
 "dg": "https://www.danielgarcialeiloes.com.br/", "galvani": "https://www.galvanileiloes.com.br/",
 "solidus": "https://www.soliduslevel.com.br/", "mwd": "https://www.leiloesmwd.com.br/",
 "lancecerto": "https://www.lancecertoleiloes.com.br/", "mega": "https://www.megaleiloes.com.br/",
 "zuk": "https://www.portalzuk.com.br/", "sold": "https://www.sold.com.br/",
 "frazao": "https://www.frazaoleiloes.com.br/", "superbid": "https://www.superbid.net/",
 "seuimovelbb": "https://www.seuimovelbb.com.br/", "comprei": "https://comprei.pgfn.gov.br/",
 "vendasgov": "https://imoveis.vendasgov.serpro.gov.br/", "leilaoimovel": "https://www.leilaoimovel.com.br/leilao-de-imoveis/pa",
 "leilaomaps": "https://leilaomaps.com/", "flex": "https://www.flexleiloes.com.br/",
 "grleiloes": "https://www.grleiloes.com/", "alfa": "https://alfaleiloes.com/",
}
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
for nome, url in SITES.items():
    try:
        r = requests.get(url, headers=UA, timeout=25)
        t = r.text[:4000].lower()
        bloq = any(k in t for k in ("captcha", "radware", "cf-challenge", "just a moment", "access denied", "bot manager"))
        print(f"{nome:12} {r.status_code} {len(r.content):>8}B {'BLOQUEADO' if bloq else 'ok'}")
    except Exception as e:
        print(f"{nome:12} ERRO {type(e).__name__}")
