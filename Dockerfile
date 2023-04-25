##ENTRYPOINT ["top", "-b"]
#
#FROM python:alpine
##создаем директорию
#
#SHELL ["/bin/bash", "-c"]
#
## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /app
# #копируем все в директорию
#COPY . /app
##устанавливаем зависимости
#RUN pip install -r requirements.txt
#
## открывает 5000 порт
##EXPOSE 5000
#
#CMD [ "python3", "main.py" ]

#docker build . -t posting_vk


FROM python:3.10.9


SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

#RUN pip install --upgrade pip
 #создаем директорию
WORKDIR /app
 #копируем все в директорию
COPY . /app
#устанавливаем зависимости



#CMD [ "python3", "main.py" ]