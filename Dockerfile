FROM python:3.9

RUN apt-get update && \
    apt-get install -y libgl1-mesa-dev

Run pip install --upgrade pip


RUN pip install uvicorn fastapi multipart numpy scikit-learn tensorflow

EXPOSE 8501

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501"]
