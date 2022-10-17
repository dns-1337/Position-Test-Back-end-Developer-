FROM python:3.9-alpine

WORKDIR /code

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requeriments.txt requeriments.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requeriments.txt

COPY . .

CMD ["flask", "run"]