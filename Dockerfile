FROM python:3.9.2

COPY requirements.txt requirements.txt
COPY app2.py app2.py
COPY parser2.txt parser2.txt
CMD ["apt","install","python3-pip"]
RUN pip install -r requirements.txt
RUN pip install requests 
CMD [ "python3", "app2.py"]


