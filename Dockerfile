FROM python:3.6.10

WORKDIR /src

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

RUN pytest --cov=. tests/

CMD ["bash", "run.sh"]