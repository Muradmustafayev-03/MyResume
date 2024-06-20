FROM ubuntu:20.04

LABEL authors="muradmustafayev"

ENV DEBIAN_FRONTEND=noninteractive

# Install Python
RUN apt-get update && \
    apt-get install -y python3 python3-pip

WORKDIR /app
COPY . .

RUN pip3 install -r src/requirements.txt

# Install necessary dependencies to add repositories and install wkhtmltopdf
RUN apt-get update && \
    apt-get install -y software-properties-common wget && \
    wget -q https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb && \
    apt-get install -y ./wkhtmltox_0.12.6-1.bionic_amd64.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && rm wkhtmltox_0.12.6-1.bionic_amd64.deb

EXPOSE 8080
CMD ["python3", "src/app.py"]
