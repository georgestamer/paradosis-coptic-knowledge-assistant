# PARADOSIS

Deterministic WhatsApp knowledge assistant MVP for approved Coptic Orthodox Church content. It never generates theological content.

## Start
```bash
cp .env.example .env
docker compose up --build
docker compose exec api alembic upgrade head
pytest
```
