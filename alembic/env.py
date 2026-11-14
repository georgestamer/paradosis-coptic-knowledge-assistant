from alembic import context
from app.core.config import settings
from app.database.base import Base
from app.models import Alias, Category, Content, Reference
config = context.config
config.set_main_option('sqlalchemy.url', settings.database_url.replace('%','%%'))
target_metadata = Base.metadata
def run_migrations_online():
    from sqlalchemy import engine_from_config, pool
    with engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool).connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction(): context.run_migrations()
run_migrations_online()
