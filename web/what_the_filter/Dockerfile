FROM python:3.10-alpine3.19

COPY app/ /app/
COPY flag.txt /

RUN adduser -D -h /home/chall -s /bin/bash chall && \
	pip install -r /app/requirements.txt --no-cache && \
	chmod 755 /app/* && \
	chmod 777 /app/uploads/

USER chall
EXPOSE 5000
ENV FLASK_APP=/app/app.py
CMD ["flask", "run", "--host=0.0.0.0"]
