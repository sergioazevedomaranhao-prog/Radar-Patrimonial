# Radar Patrimonial

Coleta diária de imóveis de leilão (Belém, Grande São Luís e rural do Pará), deduplicação, análise de viabilidade e site privado. Plano completo em `BRIEFING.md`.

## Estado
- [x] Fase 1a — coletor da Caixa (PA e MA), histórico de preços, coleta diária no GitHub Actions
- [ ] Fase 1b — banco Supabase + página simples
- [ ] Fase 2 — Norte Leilões, Leilão VIP, Mega, Zuk, Sold, Flex, Seu Imóvel BB/AgroBB, PGFN Comprei
- [ ] Fases 3 a 7 — ver BRIEFING.md

## Rodar no computador
```
pip install -r requirements.txt
python -m coletor.main
```
Segredos (Supabase) ficam em variáveis de ambiente / secrets do GitHub, nunca no código.
