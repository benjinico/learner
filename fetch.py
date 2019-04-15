import psycopg2
"""make a connection"""
try:
    connect= psycopg2.connect(
        host= "localhost", user = "postgres", password="benji",
        database= "employees", port= 5433)

    cursor= connect.cursor()
    """the cursor object executes our queries """
    """querying the database to inssert data"""

    query ="""SELECT *
	FROM public.bio_data;"""
    cursor.execute(query)
    results = cursor.fetchall()
    for i in results:
        print(i)
    print(results)

    """commit changes"""
    connect.commit()
    print("retrieved successfully")



except(Exception, psycopg2.Error) as error:
    print("something went wrong!",error)