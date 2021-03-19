FROM python:3.9.2-slim

COPY requirements.txt requirements.txt
COPY app2.py app2.py
COPY parser.py parser.py
COPY parser2.txt parser2.txt
CMD ["apt","install","python3-pip"]
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 
RUN pip install requests 
RUN pip install emoji --upgrade
CMD [ "python3", "parser.py"]
CMD [ "python3", "app2.py"]

