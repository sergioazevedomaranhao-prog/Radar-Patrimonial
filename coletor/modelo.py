"""Formato único de anúncio, igual para todas as fontes."""
from dataclasses import dataclass, field, asdict
from typing import Optional
import re

TIPOS = {
    "APARTAMENTO": "apartamento", "CASA": "casa", "SOBRADO": "casa", "TERRENO": "terreno",
    "LOTE": "terreno", "SALA": "comercial", "LOJA": "comercial", "COMERCIAL": "comercial",
    "PREDIO": "comercial", "GALPAO": "comercial", "FAZENDA": "rural", "SITIO": "rural",
    "CHACARA": "rural", "GLEBA": "rural", "RURAL": "rural", "AREA RURAL": "rural",
}

def tipo_padrao(texto: str) -> str:
    from .escopo import norm
    t = norm(texto)
    for chave, valor in TIPOS.items():
        if t.startswith(chave) or f" {chave}" in f" {t}":
            return valor
    return "outro"

def numero_br(txt: str) -> Optional[float]:
    """'1.234,56' -> 1234.56 ; '1234.56' -> 1234.56"""
    if txt is None:
        return None
    s = str(txt).strip().replace("R$", "").strip()
    if not s:
        return None
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None

def area(desc: str, rotulo: str) -> Optional[float]:
    m = re.search(r"([\d.,]+)\s+de\s+área\s+" + rotulo, desc or "", re.I)
    if not m:
        return None
    v = numero_br(m.group(1))
    return v or None  # 0.00 vira None

@dataclass
class Anuncio:
    fonte: str                 # ex.: "caixa"
    id_fonte: str              # id do imóvel na fonte
    url: str
    uf: str
    cidade: str
    bairro: str = ""
    endereco: str = ""
    tipo: str = "outro"
    descricao: str = ""
    area_privativa: Optional[float] = None
    area_total: Optional[float] = None
    area_terreno: Optional[float] = None
    quartos: Optional[int] = None
    vagas: Optional[int] = None
    avaliacao: Optional[float] = None
    lance_1: Optional[float] = None
    data_1: Optional[str] = None
    lance_2: Optional[float] = None
    data_2: Optional[str] = None
    preco_atual: Optional[float] = None
    desconto: Optional[float] = None
    modalidade: str = ""
    financiamento: Optional[bool] = None
    fgts: Optional[bool] = None
    ocupacao: str = "nao_informado"   # ocupado | desocupado | nao_informado
    leiloeiro: str = ""
    edital_url: str = ""
    fotos: list = field(default_factory=list)
    extra: dict = field(default_factory=dict)

    def chave(self) -> str:
        return f"{self.fonte}:{self.id_fonte}"

    def dict(self) -> dict:
        d = asdict(self)
        d["chave"] = self.chave()
        return d
