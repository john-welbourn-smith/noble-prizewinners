FROM python:3.12-slim

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./load_data.py /app/load_data.py

CMD ["python", "/app/load_data.py"]
