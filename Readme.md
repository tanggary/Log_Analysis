# Readme

### Description
Log Analysis Project.

Answers 3 Queries:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

* A report generating python program that executes and returns 3 queries from a postgres database.
* Program uses psycopg2, decimal and datetime module.
* Executes 1 query at a time, and saves query result to a variable. After executing the 3 queries, the program will print the results in an easy-to-read format using for loops, string concatenation and string formatting.

### Pre-requisite
* Need to have python version 3 and postgres installed.
  * Python download: https://www.python.org/downloads/
  * Postgres download: https://www.postgresql.org/download/
* Download database logs [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
* Execute psql command to generate tables. ``` psql -d (database name) -f newsdata.sql ```
* Create view in database: ``` create view authorkey AS select authors.name, articles.slug
FROM authors join articles on authors.id = articles.author; ```
* Download/pull report.py

### How to run program
* python3 report.py
