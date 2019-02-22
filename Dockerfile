FROM python:3.7.2-alpine

LABEL maintainer="kaden@vermilion.tech"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x main.py
RUN ln -s $(pwd)/main.py /bin/validator

ENTRYPOINT [ "validator" ]

CMD [ "--help" ]
