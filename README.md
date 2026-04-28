# Hashflix

Plataforma de streaming de vídeos educacionais inspirada na Netflix, desenvolvida com Python e Django. Projeto baseado no curso da Hashtag Programação, com melhorias de arquitetura, performance e organização aplicadas de forma independente.

---

## Stack

- Python / Django
- SQLite
- Django Class-Based Views (CBV)
- Django Authentication System
- Tailwind CSS + Bootstrap 5
- django-crispy-forms
- Pillow

---

## Como funciona

### Fluxo do usuário
- Usuário informa o e-mail na entrada da plataforma
- Caso já exista conta → redireciona para login
- Caso contrário → redireciona para registro
- Todas as rotas internas exigem autenticação

### Experiência dentro da plataforma
- Página inicial com filme em destaque
- Listagem separada por:
  - filmes recentes
  - filmes em alta (baseado em visualizações)
  - continuar assistindo (histórico do usuário)
- A cada acesso a um filme:
  - visualização é incrementada automaticamente
  - filme é registrado no histórico do usuário

### Página de filme
- Exibição de descrição e detalhes
- Lista de episódios com links diretos
- Sugestão de filmes relacionados por categoria

### Navegação
- Busca global por título no navbar
- Perfil de usuário com edição de dados e senha

---

## Decisões técnicas
Algumas escolhas foram além do que o curso cobria, pesquisadas durante o desenvolvimento:
 
**Contador de visualizações com `F()` expressions**
Incrementar direto no Python (`filme.visualizacoes += 1`) causa race condition com múltiplos requests simultâneos. A operação foi substituída por `update(visualizacoes=F('visualizacoes') + 1)`, delegando o incremento ao banco de forma atômica.
 
**`prefetch_related` na listagem de filmes**
Cada filme acessando seus episódios individualmente gerava o problema N+1 — uma query extra por filme. Com `prefetch_related('episodios')`, tudo é resolvido em 2 queries independente do volume.
 
**Custom Manager para lógica de negócio**
Filtros e ordenações foram centralizados no `FilmeManager` com métodos semânticos (`recentes`, `em_alta`, `relacionados`, `filme_destaque`), mantendo as views limpas e a lógica reutilizável.
 
**`save()` override para unicidade do destaque**
A regra de "apenas um filme pode estar em destaque" foi implementada no próprio modelo via `save()`, e não na view ou no admin. Qualquer ponto de entrada que salvar um filme respeita a invariante automaticamente.

---

## Como rodar

```bash
git clone https://github.com/devthayron/hashflix.git
cd hashflix
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Autor

- **Thayron Higlânder** – [LinkedIn](https://www.linkedin.com/in/thayron-higlander) 