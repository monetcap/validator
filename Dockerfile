FROM python:3.7.2-alpine

LABEL maintainer="kaden@vermilion.tech"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./validator.py" ]

CMD [ "--help" ]
