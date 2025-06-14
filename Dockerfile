# Dockerfile

FROM registry.access.redhat.com/ubi9/python-312

WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 8080

# Run the Flask app
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
