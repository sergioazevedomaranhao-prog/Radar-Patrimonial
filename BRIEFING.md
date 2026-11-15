# Radar Patrimonial — Briefing para o Claude Code

> Coloque este arquivo na pasta do projeto e diga ao Claude Code: **"Leia o BRIEFING.md e comece pela Fase 1."**

## 1. O que é

Site de **uso pessoal** do Sergio (investidor em Belém/PA) para encontrar imóveis de leilão baratos, comprar abaixo do mercado e revender com lucro.
Objetivo: **todos** os imóveis de leilão da região aparecendo **uma única vez**, **atualizados todo dia**, com as informações necessárias para decidir rápido quais merecem análise detalhada.

## 2. Escopo

| Área | Cidades | Tipos |
|---|---|---|
| Pará (urbano) | Belém | apartamento, casa, terreno, sala/loja/galpão comercial |
| Maranhão (urbano) | São Luís, São José de Ribamar, Paço do Lumiar, Raposa | apartamento, casa, terreno, comercial |
| Pará (rural) | **todo o estado** | fazendas, glebas, chácaras, áreas rurais / agronegócio |

## 3. Fontes (mapeadas em 15/11/2026)

Prioridade 1 = maior volume ou exclusividade. Cada fonte vira um coletor separado.

### 3.1 Bancos e governo (fonte primária)
| Prioridade | Fonte | O que tem | Observação |
|---|---|---|---|
| 1 | **Caixa — Portal Imóveis Caixa** (venda-imoveis.caixa.gov.br) | Maior estoque: venda direta, venda online, licitação aberta, leilão SFI | Verificar o download da lista de imóveis por UF (PA e MA). Leilões da Caixa são feitos por leiloeiros credenciados — o link do leiloeiro vem no imóvel |
| 1 | **Seu Imóvel BB / AgroBB** (seuimovelbb.com.br, parceria Resale) + Lance no Leilão | Urbanos e **rurais** do Banco do Brasil | AgroBB é a vitrine de fazendas do BB |
| 1 | **PGFN — Comprei** (comprei.pgfn.gov.br) | Imóveis penhorados em execução fiscal da União, venda direta com até 50% de desconto | Login gov.br |
| 2 | **SPU — VendasGov Imóveis** (imoveis.vendasgov.serpro.gov.br) | Imóveis da União e de estatais (ex.: BNB) | |
| 2 | Santander, Bradesco, Itaú, Banco Inter, Sicoob, Sicredi | Extrajudiciais | Vendem via Mega Leilões, Zuk, Frazão, Sold etc. — cobertos pelos coletores dos leiloeiros |
| 2 | **Banco da Amazônia (BASA)**, **Banpará**, **Banco do Nordeste (BNB)** | Rurais e comerciais na região | Portal de venda a confirmar — importante para agro no PA |
| 3 | Correios, governos estaduais | Imóveis próprios esporádicos | |

### 3.2 Justiça (leilões judiciais)
| Prioridade | Fonte | Observação |
|---|---|---|
| 1 | **TRT-8** (PA/AP) — Leilão Unificado das Varas de Belém e Ananindeua | ~6 por ano; já usou Norte Leilões, Maestro Leilões e King Leilões |
| 1 | **TJPA** (CELC/CAPJUS) e **TJMA** (Corregedoria, sorteio de leiloeiros) | Editais de praças por vara |
| 2 | **TRT-16** (MA) — leilão judicial unificado | |
| 2 | **Justiça Federal — SJPA e SJMA (TRF1)** | Execuções fiscais com imóveis em Belém |

### 3.3 Leiloeiros
**JUCEPA — leiloeiros ativos com site (lista oficial jucepa.pa.gov.br/node/171, consultada em 15/11/2026)**
Coletor obrigatório para cada site abaixo. ★ = base em Belém/PA.

| Leiloeiro | Site | Nota |
|---|---|---|
| ★ Célia Maria Campos Cardoso | vipleiloes.com.br | **Grupo VIP / Leilão VIP**, sede no Umarizal. Também ligados ao VIP: Wirna Campos Cardoso (wirnacampos.com.br), Érico Sobral, Vicente de Paulo (MA), Francisco Aranha (MA). **Prioridade 1** |
| ★ Sandro de Oliveira | norteleiloes.com.br | Norte Leilões — TRT-8, Prefeitura, execuções fiscais. **Prioridade 1** |
| ★ Lúcia Amélia Coutinho Tobelem | maestroleiloes.com.br | Maestro Leilões — TRT-8. Família Tobelem: Leonardo Simon e David Marcos |
| ★ Felipe Guimarães Carrijo | leilo.com.br | Grupo Leilo (Benevides). Mesmo endereço: Leonardo Nunes Lobo |
| ★ Daniel Elias Garcia | danielgarcialeiloes.com.br | DG Leilões, escritório no Umarizal |
| ★ Ana Laura de Souza Pires | solidusleiloes.com.br | |
| ★ Marcos Wladimir Dulnik | leiloesmwd.com.br | Redenção/PA — **rural sul do Pará** |
| Rafael Galvani Ferreira | galvanileiloes.com.br | Apartamentos em Belém |
| Luciano Resende Rodrigues | lancecertoleiloes.com.br | |
| Francisco Jonnathan S. Freitas | franciscofreitasleiloes.com.br / nortenordesteleiloes.com.br | Também credenciado no TJMA |
| Cristiane Borguetti M. Lopes | lanceja.com.br | |
| Victor Oliveira Dorta | victordortaleiloes.com.br | Também TJMA |
| Celso Alves Cunha | celsocunhaleiloes.com.br | |
| Lucas Rafael Antunes Moreira | lucasleiloeiro.com.br | Também TJMA |
| Jonas Gabriel Antunes Moreira | jonasleiloeiro.com.br | Também TJMA / JUCEMA 48 |
| Fernando Caetano Moreira Filho | fernandoleiloeiro.com.br | Também TJMA |
| Luiz Barbosa de Lima Junior | lbleiloes.com.br | |
| Alex Willian Hoppe | hoppeleiloes.com.br | Também TJMA |
| Ícaro A. Felfili Jardim | felfilileiloes.com.br | Sinop/MT — **agro** |
| Carlos Henrique Barbosa | chbarbosaleiloes.com.br | Cuiabá/MT — **agro** |

Ativos sem site informado (descobrir site via busca/edital; vários atuam em leilões judiciais e da Justiça do Trabalho): Getúlio Boadana, Aldenor de Souza Bohadana, Dorival Gomes Pinheiro, Ana Alice Freitas de Souza, João Neves Neto, Péricles Weber de Almeida, Odenerza Maria P. de Souza, Paulo Sergio Torres Lourenço, Armando Grello Cabral, Dereck Bentes Donis, Máximo Moura Lima, **Helisson Silva Souza Maia** (conduz leilões do TRT-8), Daniel Benarroch Barcessat, Edilene Nazaré Silva, José Araken Pamplona Barros, Davison F. de Azevedo Barros (Marituba), Carlos da Silva Oliveira (Dom Eliseu), Lucas Vasconcelos Chagas, Érico Sobral Soares, Edivan Ribeiro dos Santos (Marabá), Gleinda C. C. Cavalheri (Sta. Izabel), Ronaldo Galvão do Nascimento (Ananindeua), Luzinete dos Santos (Marituba).
Irregulares/cancelados (não coletar, mas registrar se aparecerem): Maria do Socorro Patello, Antonio Alberto do Vale, Ananias de Sá, Erick Rodrigo C. de Oliveira, Hugo Moreira Pimenta, Davi Borges de Aquino (alfaleiloes.com — irregular na JUCEPA, mas credenciado no TJMA), Lucyanna Miranda (lmleiloes.com.br), Ramon de Souza Prado, Fábio Prando (apiceleiloes.com), Arthur Souto Cabral Neto, Tiago Tessler Blecher, José Antônio Rodovalho Jr., Renato Guedes Rocha.
Outros vistos atuando em Belém: King Leilões (TRT-8), Leilonorte (leilonorte.com), Spencer Leilões (Caixa).

**Maranhão — leiloeiros credenciados no TJMA (tjma.jus.br/midia/cgj/pagina/site/507476; o site da JUCEMA estava fora do ar em 15/11/2026)**
| Leiloeiro | Site/contato |
|---|---|
| Francisco de Assis Costa Aranha | vipleiloes.com.br / hastavip.com.br |
| Vicente de Paulo Albuquerque Costa Filho | vipleiloes.com.br |
| Gustavo Martins Rocha | grleiloes.com |
| Marco Antônio Barbosa de Oliveira Jr. | marcoantonioleiloeiro.com.br |
| Davi Borges Aquino | alfaleiloes.com |
| Daniel Cerqueira de Mendonça | (98) — sem site |
| Conceição Maria Fixer | mariafixerleiloes.com.br |
| Rodrigo Aparecido Rigolon da Silva | rigolonleiloes.com.br |
| Ana Claudia Blasczyk | planaltoleiloes.com.br |
| Rafael Cicolin | absolutaleiloes.com.br |
| Tassiana Menezes de Mello | sem site |
| + Sandro de Oliveira (Norte Leilões, JUCEMA 027/2021), Wirna Campos, Érico Sobral, Jonas e Lucas Antunes, Fernando Caetano, Victor Dorta, Alex Hoppe, Francisco Freitas | ver tabela do Pará |

Outros vistos em São Luís: **Flex Leilões** (vários apartamentos), Rodolfo Schöntag (Caixa), Danyllo de Oliveira Maia (dmleiloesjudiciais.com.br, JUCEMA 042/2024), Tiago Vasconcelos Silva (JUCEMA 054/2025).
→ Tentar de novo a lista oficial da JUCEMA (ma.gov.br/jucema) quando voltar ao ar.

**Nacionais que atuam em PA/MA** (prioridade 1–2)
Mega Leilões · Portal Zuk · Sold · Frazão Leilões (Itaú) · Superbid · Fidalgo · Cagnelutti · Leilão VIP · Lance no Leilão (BB)

### 3.4 Agregadores — só para CONFERÊNCIA de cobertura
Não são fonte principal. Servem para descobrir imóvel/leiloeiro que está faltando.
| Agregador | Números observados |
|---|---|
| **LeilãoMaps** (exige login) | API interna `GET /api/imoveis.php?uf=PA&cidade=Belém&tipo=...&pos=0` (páginas de 36). 592 sites de origem; PA 719; Belém 89 anúncios (~55–62 únicos); apartamentos em Belém 41 anúncios (~16 únicos). Muitas duplicatas e dados errados |
| **Leilão Imóvel** (leilaoimovel.com.br) | Diz coletar 400+ leiloeiros; 366 imóveis no PA (128 Caixa), Belém 44. Página por imóvel traz leiloeiro, praças, ocupação |
| spyleiloes.com.br, pesquisaleiloes.com.br | Fontes do próprio LeilãoMaps |
| imovelweb (seção leilão) | Complementar |

**Sinal importante:** o site antigo do Sergio mostrou imóveis que o LeilãoMaps não tem (Ville Solare, Fontana di Trevi, Torre de Farnese/Norte Leilões). Nenhuma fonte sozinha tem tudo.

## 4. Dados que cada imóvel precisa ter

- Fonte(s) e link original de **cada** fonte (após deduplicação, um imóvel pode ter várias)
- Tipo, endereço completo, bairro, cidade, UF, condomínio/edifício, nº da unidade, CEP, coordenadas
- Área privativa, área total, área do terreno, quartos, vagas (rural: hectares, matrícula, CAR/CCIR se houver)
- Valor de avaliação; lance da 1ª praça e data; lance da 2ª praça e data; modalidade (judicial, extrajudicial, venda direta, venda online, licitação aberta)
- Ocupado / desocupado / não informado
- Quem paga débitos de condomínio e IPTU (regras da Caixa: arrematante até 10% da avaliação)
- Aceita financiamento / FGTS / parcelamento
- Matrícula, cartório, número do processo, link do edital (PDF)
- Fotos (link da fonte)
- **Histórico**: data em que apareceu, todas as mudanças de preço, data em que saiu (vendido/retirado)

## 5. Regras de negócio

**Deduplicação** (o maior diferencial — concorrentes falham aqui)
Mesmo imóvel quando bater a maioria de: matrícula + cartório; ou endereço normalizado + nº da unidade; ou condomínio + área (±3%, lembrando que fontes misturam área privativa e total) + bairro; ou mesmo valor de avaliação + mesmo lance + mesmo prédio. Guardar o grau de confiança e permitir que o Sergio junte/separe manualmente.

**Limpeza**
Padronizar bairros (ex.: "Icoraci" → "Icoaraci", "Tenone" → "Tenoné"), cidades ("Belem" → "Belém"), tipos. Marcar dados absurdos (apto de 80.280 m², lance de R$ 8,9 milhões num apto de 72 m²) como "a revisar" em vez de exibir.

**Nota de potencial e lucro estimado**
- Desconto sobre a avaliação
- **R$/m² do imóvel vs. R$/m² de mercado do bairro** (base a montar: anúncios de venda da região ou valores informados pelo Sergio)
- Custos: comissão do leiloeiro (5% na Caixa), ITBI, escritura/registro, débitos de condomínio/IPTU, reforma estimada por m², desocupação (se ocupado), tempo de venda
- Lucro estimado = preço de revenda estimado − (lance + custos). Ordenar a lista por isso.

## 5b. Ferramentas de análise (o que faz o Radar ser melhor)

1. **Calculadora de viabilidade** — já existe uma versão pronta (artifact "Viabilidade de Arremate", arquivo `calculadora/index.html`). Portar a função `calc()` para o site e rodar em **todo** imóvel automaticamente. Saídas: lucro líquido, retorno no período e ao ano, comparação com o CDI, **lance máximo para a meta**, quanto a venda pode cair até zerar o lucro, cenários pessimista/realista/otimista, tabela de sensibilidade lance × R$/m².
2. **Base de preço de mercado por bairro** — coletar anúncios de venda (ZAP/VivaReal, OLX, imobiliárias locais) de Belém e Grande São Luís; mediana de R$/m² por bairro × tipo × faixa de área; atualizar semanalmente. Mostrar no imóvel os **5 comparáveis** mais parecidos (mesmo prédio > mesma rua > mesmo bairro). Permitir o Sergio corrigir o valor com conhecimento próprio (vale mais que anúncio).
3. **Lance máximo no card** — em vez de só "desconto", mostrar "lance máximo para 20%" e a diferença para o lance atual. Ordenar a lista por isso.
4. **Leitura do edital por IA** — baixar o PDF do edital/matrícula e extrair em 5 linhas: ocupação, quem paga dívidas, ações judiciais citadas (ex.: ação anulatória), penhoras, divergência de área, forma de pagamento, prazo para pagar. Gerar o **semáforo de risco** a partir disso.
5. **Histórico do imóvel** — já foi a leilão antes? quantas vezes? quedas de preço; prever o valor provável da 2ª praça; avisar quando a Caixa baixar o preço na venda direta.
6. **Liquidez** — quantos anúncios parecidos à venda no bairro e há quanto tempo; estimar meses para vender (alimenta a calculadora).
7. **Funil de trabalho** — Novo → Analisando → Visitar → Dar lance → Arrematado → Reforma → À venda → Vendido, com anotações, fotos da visita e agenda (aviso 3 dias e 1 dia antes de cada praça).
8. **Comparar lado a lado** até 4 imóveis com a calculadora aplicada a todos com os mesmos parâmetros.
9. **Mapa** com cor por retorno estimado e camada de R$/m² por bairro.
10. **Rural (Pará)** — R$/ha comparado com a média do município; checagens públicas: embargos do IBAMA, sobreposição no CAR/SIGEF, terra indígena/UC, distância do asfalto e da sede; marcar risco fundiário (importante no PA).
11. **Alertas** no WhatsApp/Telegram: imóvel novo acima da meta, queda de preço, praça chegando.
12. **Parâmetros padrão do Sergio** (meta de retorno, custo de reforma por m², corretagem, regime de imposto, ITBI por cidade) salvos uma vez e usados em tudo.

## 6. Site (manter o layout atual do Sergio: "Radar Patrimonial")

Menu atual: Mapa · Oportunidades · Descobrir · Acompanhar · Buscar imóveis · Comparar · Simulador · Agenda. Filtros: cidade, tipo, faixa de preço, financiamento, modalidade/praça, desconto e ocupação, favoritos. Campo "Seu orçamento".

Melhorias:
1. **Visão em lista/tabela** (uma linha por imóvel) além dos cards, para triar 20+ de uma vez
2. **Lucro estimado e nota** no card, com ordenação por eles
3. **R$/m² vs. bairro**
4. **Data e valor da 1ª e 2ª praça** no card
5. **Selo de ocupação** ao lado da triagem documental
6. "Pendência" sempre dizendo **qual** pendência
7. Indicador "visto em N fontes" e "novo hoje" / "preço caiu"
8. Alertas no **WhatsApp ou Telegram** para imóvel novo que passe dos critérios ou queda de preço

## 7. Arquitetura sugerida

- **Coletores**: Python (requests/httpx + BeautifulSoup; Playwright só quando o site exigir JavaScript). Um módulo por fonte, todos devolvendo o mesmo formato.
- **Banco**: Supabase (Postgres) — tabelas `imoveis`, `anuncios` (um por fonte), `historico_precos`, `fontes`, `execucoes_coleta`.
- **Agendamento**: GitHub Actions diário (ou VPS pequeno se pesar).
- **Site**: Next.js na Vercel, com login (uso privado).
- **Segredos** (senhas, chaves) só em `.env` / secrets — nunca no código nem no chat.
- **Coleta educada**: intervalo entre requisições, poucos acessos por site, respeitar bloqueios.

## 8. Fases

1. **Caixa PA + MA** → banco → lista simples no site. (Valida tudo de ponta a ponta.)
2. Norte Leilões, Mega Leilões, Zuk, Sold, Flex, Seu Imóvel BB/AgroBB, PGFN Comprei.
3. Deduplicação + limpeza + histórico de preços.
4. Conferência de cobertura contra LeilãoMaps e Leilão Imóvel (relatório "imóveis que eles têm e nós não").
5. Layout completo + nota/lucro + R$/m² do bairro.
6. Tribunais (TRT-8, TRT-16, TJPA, TJMA, JF) + leiloeiros JUCEPA/JUCEMA restantes + rural PA (BASA, Banpará, BNB, VendasGov).
7. Rotina diária + alertas WhatsApp/Telegram.

**Critério de pronto:** relatório de cobertura mostrando 0 imóveis da área que aparecem nos agregadores e faltam no Radar.

## 9. Prompt inicial para colar no Claude Code

```text
Leia o BRIEFING.md. Quero construir o Radar Patrimonial descrito nele.
Comece pela Fase 1:
1. Crie a estrutura do projeto (coletores em Python, banco no Supabase, site em Next.js).
2. Escreva o coletor da Caixa para PA e MA, filtrando as cidades do escopo
   e guardando todos os campos da seção 4 que a Caixa fornece.
3. Crie as tabelas no Supabase (seção 7) e grave os imóveis coletados.
4. Faça uma página simples listando os imóveis, para eu conferir.
Antes de cada etapa, me diga o que vai fazer e o que precisa de mim
(contas, chaves). Nunca me peça senha pelo chat: me diga em qual
arquivo .env colocar. Ao final, me mostre quantos imóveis vieram por cidade e tipo.
```
