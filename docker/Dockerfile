FROM python:3
WORKDIR /home/lmascare/misc/gitwork/utils/python/admin
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /u/admin/logs
COPY . .
CMD ["python", "./mp_ping.py"]

# # Set proxy server, replace host:port with values for your servers
# ENV http_proxy host:port
# ENV https_proxy host:port
