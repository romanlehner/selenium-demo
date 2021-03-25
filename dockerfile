FROM python:3.7-slim
WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY test.py .
CMD ["pytest", "test.py" ]
