FROM python:3.8-alpine

ARG USER=scan
ARG GROUP=scan
ARG HOME=/home/${USER}
ARG APP_DIR=${HOME}/app

ENV APP_DIR=${APP_DIR}

# Put pipenv in PATH
ENV LOCAL_BIN=${HOME}/.local/bin
ENV PATH="${PATH}:${LOCAL_BIN}"

WORKDIR ${APP_DIR}
RUN apk upgrade --no-cache

# Install required tools 
RUN apk add --no-cache \
    curl \
    bash \
    git \
    ruby

# Install brakeman
RUN gem install brakeman -v 5.1.1  

COPY  . $WORKDIR
ENV PYTHONPATH="${PYTHONPATH}:${APP_DIR}"
RUN echo $PYTHONPATH


# Create an user for security issues (256000 - Last id)
RUN addgroup -g 256000 ${GROUP} && \
    adduser -D -u 256000 -G ${USER} ${GROUP} && \
    chown -R ${USER}:${GROUP} ${HOME}

# Install the python packages
RUN chown -R ${USER}:${GROUP} ${APP_DIR}
USER ${USER}
RUN pip install --upgrade pip
RUN pip install --user --no-cache-dir \
    pipenv \
    setuptools
RUN pipenv requirements > requirements.txt \
    && pip install --user -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]

