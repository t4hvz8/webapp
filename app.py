from flask import Flask, render_template
import sqlite3



app = Flask(__name__)





@app.route('/')
@app.route('/index')
def index():
    con = sqlite3.connect('/home/firestormwebapp/webapp/winners.db', check_same_thread=False)
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) from winners")
    ava_range = cur.fetchone()
    ava_range = int(ava_range[0])

    for i in range (1, ava_range+1):
        idtg = cur.execute('SELECT id_tg FROM winners WHERE id = ?', [i]).fetchone()
        date = (cur.execute('SELECT giveaway_date FROM winners WHERE id = ?', [i]).fetchone())[0]
        idtg = idtg[0]
        ava_path = f'img/avatars/{idtg}.jpg'
        ava_path_file = f"/home/firestormwebapp/webapp/static/img/avatars/{idtg}.jpg"
        try:
            cur.execute("SELECT us_ava FROM winners WHERE id = ?", [i])
            image_blob = (cur.fetchone())[0]
            with open(ava_path_file, 'wb') as file:
                file.write(image_blob)

            cur.execute(f"UPDATE winners SET ava_path = ? WHERE id = {i}", [ava_path])
            con.commit()
        except:
            ava_path = f'img/no_ava.jpg'
            cur.execute(f"UPDATE winners SET ava_path = ? WHERE id = {i}", [ava_path])
            con.commit()
            pass

    cur.execute('SELECT id, us_nick, us_name, ava_path FROM winners')
    rows = cur.fetchall()
    cur.close()
    con.close()
    return render_template("index.html", rows=rows, date=date)

@app.route('/start')
def start():
    return render_template('start.html')




if __name__ == '__main__':
    app.run(debug=True)