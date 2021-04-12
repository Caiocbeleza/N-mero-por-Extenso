FROM python:3.6
RUN mkdir /usr/src/docker/
COPY . /usr/src/docker/
WORKDIR /usr/src/docker/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
