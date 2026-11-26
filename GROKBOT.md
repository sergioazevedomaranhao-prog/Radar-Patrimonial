# Rotina do Grokbot — entregar a lista da Caixa ao Radar Patrimonial

A Caixa bloqueia servidores de nuvem (tela de CAPTCHA), então a coleta na nuvem não consegue baixar a lista.
Pela internet de casa, num navegador normal, a lista abre. O Grokbot faz só essa parte: baixa e entrega.
O resto (filtrar cidades, histórico de preços, análise) continua automático no GitHub.

## Requisito
O Grokbot precisa rodar **no Mac do Sergio (internet de casa)**, com um navegador.
Se ele roda num servidor na nuvem (VPS), vai ser bloqueado igual — nesse caso, avise o Claude.

## Rotina (todo dia, sugestão: 05:30 de Belém)
1. Abrir no navegador: https://venda-imoveis.caixa.gov.br/sistema/download-lista.asp
2. Baixar os dois arquivos, sem alterar nada:
   - https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_PA.csv
   - https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_MA.csv
3. Conferir que cada arquivo começa com "Lista de Imóveis da Caixa" (se vier uma página de CAPTCHA ou "Bot Manager": **não tentar resolver**; parar e avisar o Sergio).
4. Enviar cada arquivo para o GitHub, substituindo o anterior:
   - Repositório: `sergioazevedomaranhao-prog/Radar-Patrimonial`, branch `main`
   - Caminho: `entrada/caixa/Lista_imoveis_PA.csv` e `entrada/caixa/Lista_imoveis_MA.csv`
   - Via API: `PUT https://api.github.com/repos/sergioazevedomaranhao-prog/Radar-Patrimonial/contents/entrada/caixa/<arquivo>`
     com `message`, `content` (arquivo em base64) e `sha` do arquivo atual (pegar antes com GET no mesmo endereço; na primeira vez não há sha).
   - Cabeçalho: `Authorization: Bearer <TOKEN>` (token guardado só no Grokbot — ver abaixo).
5. Avisar o Sergio no fim: "Caixa entregue: PA e MA" ou o erro.

O envio dispara sozinho a coleta no GitHub (aba Actions → "Coleta diária").

## Token do GitHub (o Sergio cria e entrega só ao Grokbot)
github.com → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** → Generate new token:
- Repository access: **Only select repositories → Radar-Patrimonial**
- Permissions → Repository → **Contents: Read and write** (nada além disso)
- Validade: 90 dias (renovar quando vencer)
Nunca colar esse token em chat, e-mail ou no código.
