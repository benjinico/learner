# a databases is a collection of data stored in acomputer system
"""connecting to a postgres dataabase"""
"""import the psycopg2 driver for python"""
import psycopg2
"""make a connection"""
try:
    connect= psycopg2.connect(
        host= "localhost", user = "postgres", password="benji",
        database= "employees", port= 5433)

    print(connect)


except(Exception, psycopg2.Error)as error:
    print ("something went wrong")
