FROM python:3.9

WORKDIR app

COPY . .
RUN pip install poetry
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install -r requirements.txt

CMD ["python","src/app.py"]