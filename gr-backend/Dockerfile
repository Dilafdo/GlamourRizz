FROM python:3.8-slim

WORKDIR /app

RUN mkdir data/
RUN mkdir data/out/

COPY requirments.txt .

RUN apt-get update \
    && apt-get install -y libgl1 libglib2.0-0  # Install necessary libraries \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirments.txt

COPY . .

EXPOSE 8000

CMD ["python3", "main.py"]
