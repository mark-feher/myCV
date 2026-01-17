FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for Docker cache)
COPY src/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src ./src
COPY static ./static

# Expose Flask port
EXPOSE 3030

# Environment variables
ENV FLASK_ENV=production
ENV PORT=3030

# Run the app
CMD ["python", "src/app.py"]

