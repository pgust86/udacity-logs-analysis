import psycopg2


# Q1 What are the most popular three articles of all time?
# Uses join statement along with concat function to
# article.slug with log.path
most_popular_articles = """
    SELECT articles.title, COUNT(*) as visitors from articles
    JOIN log on log.path LIKE CONCAT('/article/', articles.slug)
    WHERE log.status LIKE '%OK%'
    GROUP BY articles.title ORDER BY visitors DESC LIMIT 3;
    """
