# Hashflix

Plataforma de streaming de vídeos educacionais inspirada na Netflix, desenvolvida com Python e Django. Projeto baseado no curso da Hashtag Programação, com melhorias de arquitetura, performance e organização aplicadas de forma independente.

---

## Stack

- Python / Django
- SQLite
- Django Class-Based Views (CBV)
- Django Authentication
- Tailwind CSS + Bootstrap 5
- django-crispy-forms
- Pillow

---

## Arquitetura do sistema

### Fluxo de autenticação
- Sistema baseado em e-mail com redirecionamento condicional 
- Caso já exista conta → redireciona para login
- Caso contrário → redireciona para registro

### Experiência dentro da plataforma
- Filme em destaque definido no backend e centralizado no model
- Listagem separada por:
  - filmes recentes
  - filmes mais assistidos
  - continuar assistindo 

### Consumo de conteúdo
- A cada acesso a um filme:
  - visualização é incrementada automaticamente
  - filme é registrado no histórico do usuário

### Página de filme
- Exibição de descrição e detalhes 
- Lista de episódios com links diretos
- Sugestão de recomendações por categoria

---

## Decisões técnicas
 
**Contador de visualizações com `F()` expressions**
Incremento feito diretamente no Python (`filme.visualizacoes += 1`) gerava race condition em requisições simultâneas. A solução foi usar `F('visualizacoes') + 1`, garantindo atualização atômica no banco.
 
**`prefetch_related` na listagem de filmes**
Cada filme acessando seus episódios individualmente gerava o problema N+1 — uma query extra por filme. Com `prefetch_related('episodios')`, tudo é resolvido em 2 queries independente do volume.
 
**Custom Manager para lógica de negócio**
Filtros e ordenações foram centralizados no `FilmeManager` no model com métodos semânticos (`recentes`, `em_alta`, `relacionados`, `filme_destaque`), mantendo as *views limpas* e a *lógica reutilizável*.
 
**`save()` override para regra do destaque**
A regra de *"apenas um filme pode estar em destaque"* foi implementada no próprio model `Filme` via `save()`, assim garantindo consistência independente do ponto de entrada (admin, view ou script) respeitando a regra.

---

## Impacto técnico geral
- **Redução** de queries desnecessárias em listagens de filmes
- **Eliminação** de inconsistências em requisições simultâneos
- **Centralização** de regras de domínio no model 
- **Redução** de lógica nas views (CBV mais limpa)


## Como rodar

```bash
# Clonar o repositório
git clone https://github.com/devthayron/hashflix.git
cd hashflix

# Criar ambiente virtual no Linux/Mac
python -m venv venv
source venv/bin/activate  

# Criar ambiente virtual no windows
python -m venv venv
venv/scripts/activate 

# Instalar dependências
pip install -r requirements.txt

# Configurar banco de dados / criar superuser / rodar o servidor
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# ACESSAR
http://127.0.0.1:8000/
```

## Autor

- **Thayron Higlânder** – [LinkedIn](https://www.linkedin.com/in/thayron-higlander) 