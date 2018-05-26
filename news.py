#!/usr/bin/python3
import psycopg2
DBNAME = "news"

# Query 1 What are the most popular three articles of all time?
# Uses join statement along with concat function to add
# /article/ to the slug to match log.path


def most_popular_articles():
    # opens and closes the datebase and also executes the Query
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """SELECT title, COUNT(*) FROM articles
        JOIN log ON log.path LIKE CONCAT('/article/', slug)
        WHERE log.status LIKE '%OK%'
        GROUP BY title ORDER BY COUNT(*) DESC LIMIT 3;"""
        )
    return c.fetchall()
    db.close()

# Query 2 Who are the most popular article authors of all time?
# Similar to first query however joining articles and log to
# authors


def most_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """SELECT name, COUNT(*) FROM authors
        JOIN articles on articles.author = authors.id
        JOIN log ON log.path LIKE CONCAT('/article/', slug)
        WHERE log.status LIKE '%OK%'
        GROUP BY name ORDER BY COUNT(*) DESC;"""
        )
    return c.fetchall()
    db.close()
# query 3 view 1 to get amount of errors per day
# On what days did more than 1% of requests lead to errors
# uses subqueries to solve problem and assigning the final math
# problem to a float to solve for error percent


def errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """WITH errors AS(
        SELECT date(time), COUNT(status) AS err FROM log
        WHERE status != '200 OK'
        GROUP BY date (time)),
        total AS(
        SELECT date(time) AS day, COUNT(status) AS num from log
        GROUP BY date (time)),
        e_rate AS(
        SELECT total.day,
        ((err / num::float) * 100) AS eperc
        FROM errors, total
        WHERE errors.date = total.day)
        SELECT * FROM e_rate WHERE eperc > 1;"""
        )
    return c.fetchall()
    db.close()


def print_mostpopulararticles():
    answer = most_popular_articles()
    print('\n1. The three most popular articles are:\n')
# cycle through answer to clean up results
    for string in answer:
        print "\t - %s: %s views" % (string[0], string[1])


def print_mostpopularauthors():
    answer = most_popular_authors()
    print('\n2. The most popular authors are:\n')
# Cycle through answer to clean up results
    for string in answer:
            print "\t - %s: %s views" % (string[0], string[1])


def print_errors():
    answer = errors()
    print('\n3. The days where more than 1% of requests led to errors are:\n')
# cycle through answer to clean up result and asign floating value to
# percent in order to limit the amount of decimal places
    for string in answer:
        print "\t - %s : %.1f%% of requests" % (string[0], string[1])

# call the 3 functions that print the answers
print_mostpopulararticles()
print_mostpopularauthors()
print_errors()
