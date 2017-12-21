# ! /usr/bin/env python3
import psycopg2

# What are the most popular three articles of all time?
query_1_title = ("What are the most popular three articles of all time?")
query_1 = """select articles.title, count(*) as views
        from articles inner join log on log.path
        like concat('%',articles.slug,'%')
        where log.status like '%200%'
        group by articles.title, log.path
        order by views desc limit 3"""

# Who are the most popular article authors of all time?
query_2_title = ("Who are the most popular article authors of all time?")
query_2 = """select authors.name, count(*) as views from articles inner
        join authors on articles.author = authors.id inner join log
        on log.path like concat('%', articles.slug, '%') where
        log.status like '%200%' group by authors.name order by views desc"""

# On which days did more than 1% of requests lead to errors?
query_3_title = ("On which days did more than 1% of requests lead to errors?")
query_3 = """select * from error_log_view where \"Percent Error\" > 1"""


def option():
    """ Provide the options to select from """
    print("Welcome")
    print("Enter your option *_* \n")
    print("1 : What are the most popular three articles of all time?")
    print("2 : Who are the most popular article authors of all time?")
    print("3 : On which days did more than 1% of requests lead to errors?\n")
    while True:
        opt = int(input("Enter : "))
        if opt < 1 or opt > 3:
            print("Please Choose between the three options")
            continue
        else:
            break
    return opt


def connection():
    """Connect to the PostgreSQL database. Returns a database connection"""
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        return db, c
    except:
        print("Sorry, Unable to connect to Database")


def query_results(query):
    """Return query results for given query """
    db, c = connection()
    c.execute(query)
    return c.fetchall()
    db.close()


def print_query_results(query_result):
    """Prints query results for given query """
    print ('\n'+query_result[1])
    for index, results in enumerate(query_result[0]):
        print ('> ' + str(results[0]) + ' --- ' + str(results[1]) + ' views')


def print_error_results(query_result):
    """Prints query results for error query """
    print ('\n'+query_result[1])
    for results in query_result[0]:
        print ('> ' + str(results[0]) + ' --- ' + str(results[1]) + "% errors")


if __name__ == '__main__':
    opt = option()
    if opt == 1:
        # stores the result
        article_result = query_results(query_1), query_1_title
        # prints the output
        print_query_results(article_result)
    elif opt == 2:
        # stores the result
        author_result = query_results(query_2), query_2_title
        # prints the output
        print_query_results(author_result)
    else:
        # stores the result
        error_result = query_results(query_3), query_3_title
        # prints the output
        print_error_results(error_result)
     