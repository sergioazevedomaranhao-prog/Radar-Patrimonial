from coletor.fontes.caixa import parse

AMOSTRA = """
 Lista de Imóveis da Caixa;;Data de geração:;13/11/2026;;;;;;;
 N° do imóvel;UF;Cidade;Bairro;Endereço;Preço;Valor de avaliação;Desconto;Financiamento;Descrição;Modalidade de venda;Link de acesso

 8444416307435 ;PA ;ALTAMIRA ;ALBERTO SOARES ;RUA MARIO SOARES, N. 710, QD 02 CS 04 ;104.661,26;239.000,00;56.21;Não;Casa, 0.00 de área total, 120.00 de área privativa, 120.00 de área do terreno,  2 qto(s), varanda, a.serv, WC, 1 sala(s), cozinha.;Venda Direta Online;https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnimovel=8444416307435
 1444420607024 ;PA ;ALTAMIRA ;JARDIM UIRAPURU ;RUA POLIVALENTE, N. SN, ;395.927,85;701.000,00;43.52;Sim;Casa, 161.30 de área total, 100.80 de área privativa, 274.75 de área do terreno,  2 qto(s), a.serv, WC, 2 sala(s), cozinha.;Venda Direta Online;https://venda-imoveis.caixa.gov.br/sistema/detalhe-imovel.asp?hdnimovel=1444420607024
"""

def test_parse():
    itens = list(parse(AMOSTRA))
    assert len(itens) == 2
    a, b = itens
    assert a.id_fonte == "8444416307435" and a.tipo == "casa"
    assert a.preco_atual == 104661.26 and a.avaliacao == 239000.0
    assert a.area_total is None and a.area_privativa == 120.0 and a.quartos == 2
    assert a.financiamento is False and b.financiamento is True
    assert b.area_total == 161.30 and b.area_terreno == 274.75
