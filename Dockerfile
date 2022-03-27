FROM python:3.10-slim AS base

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

COPY --from=base /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

RUN useradd --create-home service
WORKDIR /home/service
USER service

COPY sample/ ./sample/
COPY app.key.pub .

ENTRYPOINT ["python", "-m", "sample"]
