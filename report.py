#!/usr/bin/python3

import psycopg2
from decimal import Decimal
import datetime

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select articles.title, count(*) as num FROM articles join log on articles.slug = REPLACE(log.path,'/article/','') group by articles.title order by num DESC LIMIT 3")
post1 = c.fetchall()
c.execute("select authorkey.name, count(*) as views FROM authorkey join log on authorkey.slug = REPLACE(log.path,'/article/','') GROUP by authorkey.name ORDER by views DESC")
post2 = c.fetchall()
c.execute("select distinct date_trunc('day',log.time) AS \"Day\", count(*) filter(where status like '%404%') / count(*)::numeric as percentage FROM log GROUP by date_trunc('day', log.time)")
post3 = c.fetchall()
db.close()

print("Three most popular articles.")
print("--------------------------------------")

for row in post1:
    print(row[0] + ' | ' + str(row[1]) + " views")

print()
print("Most popular article authors of all time.")
print("--------------------------------------")

for row in post2:
    print(row[0] + ' | ' + str(row[1]) + " views")

print()
print("Days where more than 1% of requests lead to errors.")
print("--------------------------------------")

for row in post3:
    if (row[1] > .02):
        x = row[0]
        z = x.strftime("%B" + " " + "%d" + ", " + "%Y")
        print(z + ' | ' + str(round(row[1]*100, 2)) + " percent")
