from flask import Flask, render_template, request, flash, redirect, url_for,session
import app as service
import pkg as database
app = Flask(__name__)
app.secret_key = b'dsadasw2w'  # Ini digunakan untuk enkripsi session cookies
app.debug = True  # Untuk reload otomatis saat file berubah

# halaman awal
@app.route("/")
def index():
    return render_template("01_index.html")

# menuju menu login
@app.route("/loginpage", methods=["get"])
def login_page():
    return render_template("02_login.html")

# login tanpa pertimbangan user dan admin
# @app.route("/login", methods=["POST"])a
# def login():
#     username = request.form["username"]
#     password = request.form["password"]
#     print(username, password)
#     res , err = service.login(username, password)
#     # print(len(res))
#     if err != None:
#         flash(f"{err}")
#         return redirect(url_for('login_page'))
#     elif len(res) > 0:
#         flash("login berhasil")
#         return redirect(url_for('admin_menu'))
#     else:
#         return redirect(url_for('login_page'))

# login dengan pertimbangan admin dan user
# @app.route("/login", methods=["POST"])
# def login():
#     username = request.form["username"]
#     password = request.form["password"]

#     # Memanggil service untuk login
#     res_login, err_login = service.login(username, password)
#     if err_login:
#         flash('username atau password salah')
#         return "Gagal login: {}".format(err_login)

#     # Memanggil service untuk mendapatkan role
#     role, err_role = service.get_role(username)
#     if err_role:
#         return "Gagal mendapatkan role: {}".format(err_role)

#     # Menyimpan role ke dalam session
#     session['role'] = role

#     # Menentukan redirect berdasarkan role
#     if role == "admin":
#         return redirect(url_for("admin_menu"))
#     elif role == "user":
#         return redirect(url_for("user_menu"))
#     else:
#         return "Role tidak valid: {}".format(role)

# login menyimpan username ke session
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Memanggil service untuk login
        res_login, err_login = service.login(username, password)
        if err_login:
            flash('username atau password salah')
            return render_template("02_login.html", error="Gagal login: {}".format(err_login))

        # Memanggil service untuk mendapatkan role
        role, err_role = service.get_role(username)
        if err_role:
            return render_template("02_login.html", error="Gagal mendapatkan role: {}".format(err_role))

        # Menyimpan username dan role ke dalam session
        session['username'] = username
        session['role'] = role

        # Menentukan redirect berdasarkan role
        if role == "admin":
            return redirect(url_for("admin_menu"))
        elif role == "user":
            return redirect(url_for("user_menu"))
        else:
            return render_template("02_login.html", error="Role tidak valid: {}".format(role))
    else:
        return render_template("02_login.html")

# menuju regrister
@app.route("/registerpage", methods=["get"])
def register_page():
    return render_template("03_register.html")


# register status auto user
@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    success, error = service.register(username, email, password)
    if error:
        flash(f"Registration failed: {error}")
    else:
        flash("Registration successful")
    return redirect(url_for('login_page'))

# menu utama admin
@app.route("/admin_menu")
def admin_menu():
    # keyword = request.form["keyword"]
    # page = request.form["page"]
    # limit = request.form["limit"]
    
    res, err = service.list_dokter(None, 1, 1,1)
    if err != None:
        print(err)
    
    if res in (None, []):
        msg = flash("data not found")
        return render_template("04_admin_menu.html", msg = msg)
    
    return render_template('04_admin_menu.html', data=res)

# menu utama user
@app.route("/user_menu")
def user_menu():
    # keyword = request.form["keyword"]
    # page = request.form["page"]
    # limit = request.form["limit"]
    
    res, err = service.list_dokter(None, 1, 1,1)
    if err != None:
        print(err)
    
    if res in (None, []):
        msg = flash("data not found")
        return render_template("04_user_menu.html", msg = msg)
    
    return render_template('04_user_menu.html', data=res)

@app.route("/biodata_admin", methods=['GET', 'POST'])
def biodata_admin():
    if 'username' not in session:
        flash('Anda harus login terlebih dahulu')
        return redirect(url_for('login'))

    username = session['username']
    print(username)
    res, err = service.biodata(None, username)
    print(res)
    if err is not None:
        flash(err)
        return render_template("05_biodata_admin.html", data=None)
    
    if res is None:
        flash("Data not found")
        return render_template("05_biodata_admin.html", data=None)
    
    return render_template("05_biodata_admin.html", data=res)


@app.route("/edit_biodata")
def edit_biodata():
    return render_template("06_edit_biodata.html")

@app.route("/tambah_dokter")
def tambah_dokter():
    return render_template("07_tambah_dokter.html")

@app.route("/daftar_antrian")
def daftar_antrian():
    return render_template("08_daftar_antrian.html")

@app.route("/keluar")
def keluar() :
    return render_template("01_index.html")








# u/ pasien dikerjakan hendris
@app.route("/main_menu")
def main_menu():
    return render_template("menu_pasien.html")

@app.route("/janji_temu")
def janji_temu():
    return render_template("janji_temu.html")