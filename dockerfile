FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/b4dm0nd4y/st_tut.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Hello.py", "--server.port=8501", "--server.address=0.0.0.0"]
