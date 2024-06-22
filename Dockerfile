FROM python:3.12

# set workdir RUN and CMD will be executed from here
WORKDIR /app

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="${PATH}:/root/.local/bin"

# For local dev:
ENV GOOGLE_APPLICATION_CREDENTIALS='key.json'
COPY ./key.json /app/

# setup poetry to use virtualenv
RUN poetry config virtualenvs.create true
RUN poetry config virtualenvs.in-project true

# COPY this to make use of some cache thingie
COPY poetry.lock pyproject.toml /app/

# Install dependencies
RUN poetry install --no-root --no-dev --no-interaction

# Copy alembic migrations and files
COPY alembic.ini /app/
COPY ./alembic /app/alembic

COPY ./migration_data /app/migration_data

# move williott app into the app folder
COPY ./williott /app/williott

# Upgrade/Make Database
RUN poetry run alembic upgrade head


# This will execute from within /app/ so we can find warp directly
CMD ["poetry", "run",  "uvicorn", "williott.main:app", "--host", "0.0.0.0", "--port", "8080"]
