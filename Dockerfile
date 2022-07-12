#sistema linux com python
FROM python:3.8-slim-buster

#crinado um diretorio
WORKDIR /app

#Copiar as dependecia do sistema
COPY requirements.txt requirements.txt
#Rodar as dependecia do sistema
RUN pip3 install -r requirements.txt

#copiar tudo é colocar dentro da pasta criar APP
COPY . .

CMD ["python3", "manage.py","runserver", "0.0.0.0:8000"]
