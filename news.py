import psycopg2


# Q1 What are the most popular three articles of all time?
# Uses join statement along with concat function to add
#/article/ to the slug to match log.path

most_popular_articles = """
    SELECT title, COUNT(*)
    from articles
    JOIN log ON
    log.path LIKE CONCAT('/article/', slug)
    WHERE log.status LIKE '%OK%'
    GROUP BY title ORDER BY COUNT(*) DESC LIMIT 3;
    """

# Q2 Who are the most popular article authors of all time?
#  Similar to first query added second join for the authors table
most_popular_authors = """
    SELECT authors.name, COUNT(*)
    from articles
    JOIN log ON
    log.path LIKE CONCAT('/article/', slug)
    JOIN authors on articles.author = authors.id
    WHERE log.status LIKE '%OK%'
    GROUP BY authors.name ORDER BY COUNT(*) DESC;
    """
