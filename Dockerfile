FROM python:3.11.3-alpine3.18
RUN mkdir -p /app
WORKDIR /app

RUN apk add --no-cache curl gcc libc-dev python3-dev g++ unixodbc-dev linux-headers
RUN curl -O https://download.microsoft.com/download/1/f/f/1fffb537-26ab-4947-a46a-7a45c27f6f77/msodbcsql18_18.2.1.1-1_amd64.apk
#RUN curl -O https://download.microsoft.com/download/1/f/f/1fffb537-26ab-4947-a46a-7a45c27f6f77/mssql-tools18_18.2.1.1-1_amd64.apk
RUN apk add --allow-untrusted msodbcsql18_18.2.1.1-1_amd64.apk
#RUN apk add --allow-untrusted mssql-tools18_18.2.1.1-1_amd64.apk

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/ /app/src/
EXPOSE 5000

# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \ 
#                 CMD curl -f http://localhost:5000/health || exit 1

CMD python "./src/app.py"