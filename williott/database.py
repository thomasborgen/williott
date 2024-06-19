from sqlmodel import SQLModel, create_engine  # noqa: F401

from williott.settings import settings

# Import models here to ensure they are registered
from williott.pokemon.models import *  # noqa: F403

engine = create_engine(
    settings.database_url,
    echo=settings.database_echo,
)
