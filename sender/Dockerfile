FROM python:3.7-alpine
ADD . /
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python", "send.py"]
