FROM python

WORKDIR /reminder
COPY . /reminder/
RUN pip install  --no-cache-dir -r requirements.txt

CMD ["python", "index.py"]
# for you might be python3