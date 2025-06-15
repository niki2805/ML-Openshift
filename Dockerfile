FROM registry.access.redhat.com/ubi9/python-39

WORKDIR /opt/app-root/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV FLASK_APP=app.py
EXPOSE 8080
CMD ["python", "app.py"]