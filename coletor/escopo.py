"""Escopo geográfico do Radar Patrimonial."""
import unicodedata

def norm(txt: str) -> str:
    """Maiúsculas, sem acento, sem espaços duplicados."""
    t = unicodedata.normalize("NFKD", txt or "").encode("ascii", "ignore").decode()
    return " ".join(t.upper().split())

CIDADES_URBANAS = {
    "PA": {"BELEM"},
    "MA": {"SAO LUIS", "SAO JOSE DE RIBAMAR", "PACO DO LUMIAR", "RAPOSA"},
}
# Rural: todo o estado do Pará.
UF_RURAL = {"PA"}

def no_escopo(uf: str, cidade: str, tipo: str) -> bool:
    uf, cidade = norm(uf), norm(cidade)
    if tipo == "rural" and uf in UF_RURAL:
        return True
    return cidade in CIDADES_URBANAS.get(uf, set())
