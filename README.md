# One Way — site institucional

Site estático da **One Way**, consultoria e desenvolvimento de soluções específicas e práticas
(web, mobile e banco de dados). Sem build, sem framework, sem JavaScript: HTML + CSS em `public/`.

## Estrutura

```
public/
  index.html     página única: abertura, abordagem, serviços, como trabalhamos, soluções, projetos, contato
  404.html       página de erro
  css/style.css  identidade One Way (carvão #24282C/#181B1F, laranja #E97D25, cinza metálico #6A7077, Montserrat)
  favicon.svg    símbolo (seta de crescimento em laranja)
  _headers       cabeçalhos de segurança (CSP sem scripts) e cache
  robots.txt
wrangler.jsonc   publicação no Cloudflare Workers (só arquivos estáticos)
```

## Ver localmente

```bash
python3 -m http.server 8000 --directory public
```

Abra http://localhost:8000.

## Publicar (Cloudflare Workers, mesmo padrão dos outros sistemas)

1. Cloudflare › Workers & Pages › Create › Import a repository › `MarcusMagalhaes/oneway`.
2. Build command: vazio. Deploy command: `npx wrangler deploy`.
3. Domínio próprio: no Worker `oneway-site`, *Settings › Domains & Routes › Add › Custom domain*.

Também funciona em qualquer hospedagem estática (GitHub Pages, Netlify): basta servir a pasta `public/`.

## Pendências

- **WhatsApp**: em `public/index.html`, seção Contato, descomente o botão e troque `55DDDNUMERO` pelo número.
- **Domínio**: quando estiver definido, acrescentar `<link rel="canonical">`, `og:url`, `og:image` e um `sitemap.xml`.
- **Clientes**: os projetos sob medida estão descritos por segmento, sem o nome do cliente. Citar nomes ou logos só com autorização.
