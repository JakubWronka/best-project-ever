FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install "graphene-django>=2.0"
COPY . /code/
RUN pwd >> location_of_pwd.txt
# sed commands are used here due to graphene issue fix (found on internet)
RUN sed -i 's/import force_text/import force_str/g' /usr/local/lib/python3.10/site-packages/graphene_django/utils/utils.py
RUN sed -i 's/s = force_text(s)/s = force_str(s)/g' /usr/local/lib/python3.10/site-packages/graphene_django/utils/utils.py
RUN sed -i 's/return to_camel_case(s) if isinstance(s, six.string_types) else s//g' /usr/local/lib/python3.10/site-packages/graphene_django/utils/utils.py
