# Python3
# FROM python:3
# WORKDIR /home/lmascare/misc/gitwork/utils/python/admin
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# RUN mkdir -p /u/admin/logs
# COPY . .
# CMD ["python", "./mp_ping.py"]

# # Set proxy server, replace host:port with values for your servers
# ENV http_proxy host:port
# ENV https_proxy host:port

# Python2 App with Flask
FROM python:2.7-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "app.py"]
