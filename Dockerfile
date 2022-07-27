FROM python:3.11.0b5-alpine3.15
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python", "DeLab.py" ]
