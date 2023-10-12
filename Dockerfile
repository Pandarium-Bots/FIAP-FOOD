FROM python:latest

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# CMD [ "python app.py" ]

CMD ["tail", "-f", "/dev/null"]
