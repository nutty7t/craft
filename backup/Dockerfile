FROM python:3.7

COPY requirements.txt .
COPY backup.py .

RUN pip install --upgrade pip \
	&& pip install -r requirements.txt

CMD ["python", "backup.py"]

