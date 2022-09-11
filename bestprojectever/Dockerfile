FROM node:18.9.0-alpine
WORKDIR /code/frontend
COPY frontend/package.json /code/frontend/
RUN npm init -y
RUN npm i webpack webpack-cli --save-dev
RUN npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
RUN npm i react react-dom --save-dev
# RUN npm run dev # - here or in the entrypoint - discuss & discover 

FROM python:3
# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
# RUN chmod a+x /code/docker-entrypoint.sh
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py runserver 0.0.0.0:8000
