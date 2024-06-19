#Base Image
FROM python:3.11-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1



# Create and activate virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"


RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
