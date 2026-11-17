# One Way — site institucional

Site estático da **One Way**, consultoria e desenvolvimento de soluções específicas e práticas
(web, mobile e banco de dados). Sem build, sem framework, sem JavaScript: HTML + CSS em `public/`.

## Estrutura

```
public/
  index.html     página única: abertura, abordagem, serviços, como trabalhamos, soluções, projetos, contato
  404.html       página de erro
  css/style.css  identidade da logo oficial (grafite #2E3338, laranja #EE7A1E, fundo branco, Montserrat)
  img/           símbolo, nome "ONE WAY", logo completa e imagem de compartilhamento (gerados)
  favicon.png, apple-touch-icon.png, icon-512.png   ícones (só a esfera do símbolo)
  _headers       cabeçalhos de segurança (CSP sem scripts) e cache
  robots.txt
wrangler.jsonc   publicação no Cloudflare Workers (só arquivos estáticos)
docs/marca/      arte original da logo One Way
scripts/identidade.py   gera public/img e os ícones a partir da arte original (Pillow)
```

Marca: "O seu caminho à solução" · pilares Sistemas, Soluções, Tecnologia e Consultoria ·
"Tecnologia que transforma. Soluções que conectam." Trocou a arte? Substitua `docs/marca/oneway-logo-original.jpg`
e rode `python3 scripts/identidade.py`.

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
- **Domínio**: quando estiver definido, acrescentar `<link rel="canonical">`, `og:url`, deixar o `og:image` com endereço completo e criar um `sitemap.xml`.
- **Clientes**: os projetos sob medida estão descritos por segmento, sem o nome do cliente. Citar nomes ou logos só com autorização.
