FROM python:3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY recipe_site .

CMD ["gunicorn", "recipe_site.wsgi:application", "--bind", "0.0.0.0:8000"]