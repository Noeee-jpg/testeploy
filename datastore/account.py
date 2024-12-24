def login (conn, username:str, password:str):
    try:
        cur = conn.cursor()
        query = '''
            select username, password 
            from public.users_healthcare
            where username = '{0}' and password = '{1}'
        '''.format(username, password)
        cur.execute(query)
        resdata = cur.fetchone()
        if resdata:
            return resdata, None
        else:
            raise Exception("username or password incorrect")
    except Exception as e:
        return None, e

def get_role(conn, username):
    try:
        cur = conn.cursor()
        query = '''
            SELECT role
            FROM public.users_healthcare
            WHERE username = %s
        '''
        cur.execute(query, (username,))
        resdata = cur.fetchone()
        if resdata is not None:
            return resdata[0], None  # Mengembalikan nilai role dari tuple hasil
        else:
            raise Exception("Role tidak valid untuk username ini")
    except Exception as e:
        return None, str(e)
    finally:
        if cur is not None:
            cur.close()


def register_user(conn, username, email, password):
    try:
        cur = conn.cursor()
        query = '''
            INSERT INTO public.users_healthcare (username, email, password, role) 
            VALUES (%s, %s, %s, 'user')
        '''
        cur.execute(query, (username, email, password))
        conn.commit()
        return "Registration successful", None
    except Exception as e:
        conn.rollback()
        return None, str(e)
    finally:
        if cur is not None:
            cur.close()

def list_dokter(conn, keyword:str, limit: int, page: int):
    try :
        cur = conn.cursor()
        query = '''
            SELECT * FROM dokter
        '''

        print(query)
        cur.execute(query)
        resdata = cur.fetchall()
        print(resdata)
        if resdata not in (None, []):
            return resdata, None
        else:
            raise Exception("data not found")
    except Exception as e:
        return None, e

def list_dokter(conn, keyword:str, limit: int, page: int):
    try :
        cur = conn.cursor()
        query = '''
            SELECT * FROM dokter
        '''

        print(query)
        cur.execute(query)
        resdata = cur.fetchall()
        print(resdata)
        if resdata not in (None, []):
            return resdata, None
        else:
            raise Exception("data not found")
    except Exception as e:
        return None, e

def biodata_diri(conn, username):
    try:
        cur = conn.cursor()
        query = '''
            SELECT *
            FROM public.users_healthcare
            WHERE username = %s
        '''
        cur.execute(query, (username,))
        resdata = cur.fetchone()  # Fetch one result
        if resdata is not None:
            return resdata, None
        else:
            return None, "Data tidak ditemukan untuk username ini"
    except Exception as e:
        return None, str(e)
    finally:
        if cur:
            cur.close()
