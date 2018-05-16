import psycopg2


# Query 1 What are the most popular three articles of all time?
# Uses join statement along with concat function to add
#/article/ to the slug to match log.path

def most_popular_articles():
    db = psycopg2.connect(database=news)
    c = db.cursor()
    c. execute(
    """SELECT title, COUNT(*) FROM articles
    JOIN log ON log.path LIKE CONCAT('/article/', slug)
    WHERE log.status LIKE '%OK%'
    GROUP BY title ORDER BY COUNT(*) DESC LIMIT 3;"""
    )

# Query 2 Who are the most popular article authors of all time?
#  Similar to first query however joining articles and log to
#   authors
def most_popular_authors():
    db = psycopg.connect(database=news)
    c. db.cursor()
    c.execute(
     """SELECT name, COUNT(*) FROM authors
    JOIN articles on articles.author = authors.id
    JOIN log ON log.path LIKE CONCAT('/article/', slug)
    WHERE log.status LIKE '%OK%'
    GROUP BY name ORDER BY COUNT(*) DESC;"""
    )

#query 3
 view errors (
 select date(time), count(status) as sum from log
 where status != '200 OK'
 group by date (time);
)
 view total entries

  select date(time), count(status) as sum from log
  where status != '200 OK'
  group by date (time);
