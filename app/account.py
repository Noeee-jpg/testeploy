from pkg import openConnection
import datastore

# import function datasore

def login(username: str, password: str):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resLogin, err = datastore.login(conn, username, password)
        if err != None:
            raise Exception(err)
        return resLogin, None
    except Exception as e:
        return None, e
    
def get_role(username):
    try:
        conn, err = openConnection()
        if err is not None or conn is None:
            raise Exception(f"Koneksi tidak berhasil: {err}")
        
        resLogin, err = datastore.get_role(conn, username)
        if err is not None:
            raise Exception(err)
        
        return resLogin, None
    except Exception as e:
        return None, e
    finally:
        if conn is not None:
            conn.close()


    
def register(username,email, password):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resRegister, err = datastore.register_user(conn,username,email, password,)  
        if err != None:
            raise Exception(err)
        
        return resRegister, None
    except Exception as e:
        return None, e
    
def list_dokter(conn, keyword:str, limit: int, page: int) :
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        # hit api ke service login next meet
        listdokter, err = datastore.list_dokter(conn, keyword, limit, page )
        if err != None:
            raise Exception(err)
        return listdokter, None
    except Exception as e:
        return None, e
    
def biodata(conn, username):
    try:
        if conn is None:
            conn, err = openConnection()
            if err is not None or conn is None:
                raise Exception(f"Gagal membuka koneksi database: {err}")
        
        biodata_diri, err = datastore.biodata_diri(conn, username)
        if err is not None:
            raise Exception(f"Gagal mengambil biodata: {err}")
        
        return biodata_diri, None
    except Exception as e:
        return None, str(e)
    finally:
        if conn:
            conn.close()