#!/usr/bin/env python3

import psycopg2
from decimal import Decimal
import datetime

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
query1 = """
SELECT articles.title,
       count(*) AS num
FROM articles
JOIN log ON articles.slug = REPLACE(log.path, '/article/', '')
GROUP BY articles.title
ORDER BY num DESC
LIMIT 3;
"""
c.execute(query1)
post1 = c.fetchall()
query2 = """
SELECT authorkey.name,
       count(*) AS views
FROM authorkey
JOIN log ON authorkey.slug = REPLACE(log.path, '/article/', '')
GROUP BY authorkey.name
ORDER BY views DESC;
"""
c.execute(query2)
post2 = c.fetchall()
query3 = """
SELECT DISTINCT date_trunc('day', log.time) AS \"Day\",
       count(*) filter(
WHERE status LIKE '%404%') / count(*)::numeric AS percentage
FROM log
GROUP BY date_trunc('day', log.time);
"""
c.execute(query3)
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
