import psycopg2

db_name = "newsdata"


def create_view(view):
    db = psycopg2.connect(database=db_name)
    c = db.cursor()
    c.execute(view)
    db.commit()
    db.close()

total_views = """
CREATE VIEW totalviews AS
SELECT slug, views 
FROM(SELECT SUBSTRING(path FROM 10) AS slug,COUNT(*) AS views
FROM log
WHERE path LIKE '%article%' AND status LIKE '%200%'
GROUP BY path
ORDER BY VIEWS DESC) AS totalviews;"""

author_slug = """
CREATE VIEW author_slug AS
SELECT author,name,slug
FROM authors
JOIN articles ON authors.id = articles.author;"""

status200 = """
CREATE VIEW status200 AS
SELECT EXTRACT(day from time) AS day,COUNT(*) AS totalsuccess
FROM log
WHERE status LIKE '%200%'
GROUP BY day;"""

status404 = """
CREATE VIEW status404 AS
SELECT EXTRACT(day from time) AS day,COUNT(*) AS totalerrors
FROM log
WHERE status LIKE '%404%'
GROUP BY day;"""

create_view(total_views)
create_view(author_slug)
create_view(status200)
create_view(status404)
