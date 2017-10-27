FROM python:2
ADD . /code
RUN mkdir /generated
WORKDIR /code
RUN pip install -r requirements.txt
WORKDIR /code/bin
CMD ["--id-prefix", "smart", "--write-fhir","/generated"]
ENTRYPOINT  ["python", "generate.py"]