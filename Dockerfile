FROM python:3.10
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY main.py ./main.py
COPY my_module.py ./my_module.py
COPY pages ./pages
COPY .streamlit ./.streamlit
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]