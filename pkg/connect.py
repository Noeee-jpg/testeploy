import psycopg2
# from config import load_config

def connection():
    try:
        conn = psycopg2.connect(database="coba",
                                host="localhost",
                                user="postgres",
                                password="123456789",
                                port="5432")
        return conn, None
    except (psycopg2.DatabaseError, Exception) as error:
        return None, error
    """ Connect to the PostgreSQL database server """
    # try:
    #     # connecting to the PostgreSQL server
    #     with psycopg2.connect(**config) as conn:
    #         print('Connected to the PostgreSQL server.')
    #         return conn
    # except (psycopg2.DatabaseError, Exception) as error:
    #     print(error)

def grant_access_connect():
    # config = load_config
    connect, err = connection()
    return connect, err

grant_access_connect()