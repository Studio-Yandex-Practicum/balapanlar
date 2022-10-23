FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY . /app
CMD ["python", "app/manage.py", "runserver", "0:80"]