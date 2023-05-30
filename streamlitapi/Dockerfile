FROM python:3.7-slim
WORKDIR /streamlit
COPY ./requirements.txt /streamlit/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl vim jq
COPY ./webapp.py /streamlit/
EXPOSE 8501
CMD ["streamlit","run","webapp.py"]
