FROM python:3.6-slim-stretch
RUN pip install nameko -i  https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com 
RUN pip install aliyun-python-sdk-core-v3 -i  https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com 

COPY sms /var/sms
COPY config.yml /var/config.yml
WORKDIR /var
