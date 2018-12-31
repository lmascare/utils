FROM python:3
WORKDIR /home/lmascare/misc/gitwork/utils/python/admin
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /u/admin/logs
COPY . .
CMD ["python", "./mp_ping.py"]
