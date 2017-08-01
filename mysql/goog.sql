-- Create the user
create user 'stocks'@'localhost' identified by 'PASSWORD';
grant all privileges on 'stocks'@'localhost' identified by 'PASSWORD';
grant all privileges on 'stocks'@'%' identified by 'PASSWORD';

-- mysql -u stocks -p
create database stocks default character set UTF8;
use stocks;
create table goog (
date    date not null,
open    float(10,2) not null,
high    float(10,2) not null,
low     float(10,2) not null,
close   float(10,2) not null,
volume  int(10) not null
);

-- To modify a column
-- alter table goog modify volume int(10) not null;

-- To rename a table
-- rename table x to y;

-- load historical data into a MySQL table
-- Ensure you convert STR to DATE
load data local infile '/home/lmascare/misc/mysql/goog.csv'
into table goog
fields terminated by ',' ignore 1 lines
(@date, open, high, low, close, volume)
set date = str_to_date(@date,'%d-%b-%y');