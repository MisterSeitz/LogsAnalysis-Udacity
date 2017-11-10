-- CREATE VIEW 'totalviews TO RETRIEVE slug TO JOIN ON ARTICLES TABLE

CREATE VIEW totalviews AS
SELECT slug, views FROM(SELECT SUBSTRING(path FROM 10) AS slug,COUNT(*) AS views
FROM log
WHERE path LIKE '%article%' AND status LIKE '%200%'
GROUP BY path
ORDER BY VIEWS DESC) AS totalviews;

-- CREATE VIEW 'author_slug' TO JOIN TABLE 'articles' WITH authors

CREATE VIEW author_slug AS
SELECT author,name,slug
FROM authors
JOIN articles ON authors.id = articles.author;

--CREATE VIEW TO PRODUCE TABLE WITH SUCCESSFUL VIEWS

CREATE VIEW status200 AS
SELECT EXTRACT(day from time) AS day,COUNT(*) AS totalsuccess
FROM log
WHERE status LIKE '%200%'
GROUP BY day;

--CREATE VIEW TO PRODUCE TABLE WITH ERRONEOUS VIEWS

CREATE VIEW status404 AS
SELECT EXTRACT(day from time) AS day,COUNT(*) AS totalerrors
FROM log
WHERE status LIKE '%404%'
GROUP BY day;