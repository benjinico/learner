# pushing data into the postgres database
import psycopg2
"""make a connection"""
try:
    connect= psycopg2.connect(
        host= "localhost", user = "postgres", password="benji",
        database= "employees", port= 5433)

    cursor= connect.cursor()
    """the cursor object executes our queries """
    """querying the database to inssert data"""

    query ="""INSERT INTO public.bio_data(
	employee_name, employee_id, department)
	VALUES ('oli', '230001', 'sales'),('mob', '45678123', 'accounts');"""
    """execute query"""
    cursor.execute(query)

    """commit changes"""
    connect.commit()
    print("new record added successfully")

except(Exception, psycopg2.Error) as error:
    print("something went wrong!",error)




