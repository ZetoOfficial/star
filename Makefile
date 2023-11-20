COMPOSE := docker-compose -f docker-compose.yml

.PHONY: up
up:
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down -v

ps:
	$(COMPOSE) ps

migrate:
	alembic upgrade head