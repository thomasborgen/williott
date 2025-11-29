from sqlmodel import SQLModel, create_engine  # noqa: F401

from williott.settings import settings

# Import models here to ensure they are registered

engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    echo=settings.DATABASE_ECHO,
)
