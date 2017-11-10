import psycopg2

db_name = "newsdata"


def execute_query(query):
    db = psycopg2.connect(database=db_name)
    c = db.cursor()
    c.execute(query)
    query = c.fetchall()
    db.close()
    return query


top3_articles = """
SELECT title,totalviews.views
FROM articles
JOIN totalviews ON articles.slug = totalviews.slug
ORDER BY views DESC
LIMIT 3;"""

best_authors = """
SELECT name,SUM(views) AS author_totalviews
FROM author_slug
JOIN totalviews ON author_slug.slug = totalviews.slug
GROUP BY name
ORDER BY author_totalviews DESC;"""

error_day = """
SELECT status200.day,
ROUND(totalerrors/ROUND(((totalsuccess+totalerrors)/100),2),2)
AS error_percentage
FROM status200
JOIN status404 ON status200.day = status404.day
WHERE totalerrors >= ((totalsuccess+totalerrors)/100);"""

query1 = execute_query(top3_articles)
query2 = execute_query(best_authors)
query3 = execute_query(error_day)

q1 = '1. What are the most popular three articles of all time?\n\n' + \
    str(q1[0][0]) + ' - ' + str(q1[0][1]) + ' views\n' + \
    str(q1[1][0]) + ' - ' + str(q1[1][1]) + ' views\n' + \
    str(q1[2][0]) + ' - ' + str(q1[2][1]) + ' views'

q2 = '\n\n2. Who are the most popular article authors of all time?\n\n' + \
    str(q2[0][0]) + ' - ' + str(q2[0][1]) + ' views\n' + \
    str(q2[1][0]) + ' - ' + str(q2[1][1]) + ' views\n' + \
    str(q2[2][0]) + ' - ' + str(q2[2][1]) + ' views\n'

q3 = '\n\n3. On which days did more than 1% of requests lead to errors?\n' + \
    'July ' + str(int(q3[0][0])) + ' 2016 - ' + str(q3[0][1]) + '% errors'

f = open('log_report.txt', 'w')
f.write(q1)
f.write(q2)
f.write(q3)
f.close()
