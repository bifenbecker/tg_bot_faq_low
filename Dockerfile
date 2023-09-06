FROM python:3.10-alpine3.17
#FROM python:3.10.2-slim-bullseye

WORKDIR /app

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Install pipenv and compilation dependencies
RUN pip3 install pipenv
#RUN apt-get update --fix-missing && \
#    apt-get install -y \
#      wget \
#      curl \
#      gcc \
#      nano \
#      g++ \
#      make \
#      lsof \
#      libpq-dev \
#      libffi-dev \
#      figlet \
#      netcat \
RUN apk add --no-cache build-base
RUN apk add gcc python3-dev musl-dev

RUN pip3 install asyncpg


# Install project requarements
COPY Pipfile .
COPY Pipfile.lock .

ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv uninstall --all
RUN pipenv --clear
RUN pipenv install --dev

# Set venv path
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

CMD ["pipenv", "run", "shell"]
#CMD ["pipenv", "run", "auto_migration"]
#CMD ["pipenv", "run", "migrate"]
CMD ["pipenv", "run", "start"]

