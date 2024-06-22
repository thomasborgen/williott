from typing import Generator

from sqlmodel import Session

from williott.database import engine


def get_session() -> Generator[Session, None, None]:
    """Yield FastApi session dependency."""
    with Session(engine) as session:
        yield session
