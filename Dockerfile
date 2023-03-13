FROM python:3
ENV PYTHONUNBUFFERED 1  
RUN pip install --upgrade pip
WORKDIR /project
COPY requirements.txt /project/
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]
#, "0.0.0.0:8000"