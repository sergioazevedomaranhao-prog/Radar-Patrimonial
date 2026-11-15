-- Radar Patrimonial — banco no Supabase (cole no SQL Editor do projeto)
create table if not exists anuncios (
  chave text primary key,            -- fonte:id_fonte
  fonte text not null,
  id_fonte text not null,
  url text, uf text, cidade text, bairro text, endereco text, tipo text, descricao text,
  area_privativa numeric, area_total numeric, area_terreno numeric, quartos int, vagas int,
  avaliacao numeric, lance_1 numeric, data_1 text, lance_2 numeric, data_2 text,
  preco_atual numeric, desconto numeric, modalidade text, financiamento boolean, fgts boolean,
  ocupacao text, leiloeiro text, edital_url text, fotos jsonb, extra jsonb,
  visto_primeiro timestamptz, visto_ultimo timestamptz, saiu_em timestamptz, ativo boolean default true,
  imovel_id bigint                   -- preenchido pela deduplicação (fase 3)
);
create table if not exists historico (
  id bigserial primary key,
  chave text references anuncios(chave),
  quando timestamptz default now(),
  evento text,                       -- novo | preco | saiu
  preco numeric, preco_antes numeric
);
create index if not exists anuncios_cidade_tipo on anuncios (uf, cidade, tipo) where ativo;
-- Acesso: só o service key (usado pelo coletor) escreve; o site lê com login.
alter table anuncios enable row level security;
alter table historico enable row level security;
