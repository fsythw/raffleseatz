from flask import Flask
from flask import render_template, request
import sqlite3

app = Flask(__name__)

s_order = list()

queue_number = 0
  
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/first", methods = ['GET', 'POST'])
def stall():
    if request.method == 'POST':
        if request.form['action1'] == 'Go Greens':
            stall_name = request.form['action1']
            s_order.append(stall_name)
            return render_template('go-greens.html')

        elif request.form['action1'] == "Nek's Special":
            stall_name = request.form['action1']
            s_order.append(stall_name)
            return render_template('neks-special.html')

        elif request.form['action1'] == "Oishi":
            stall_name = request.form['action1']
            s_order.append(stall_name)
            return render_template('oishi.html')

        elif request.form['action1'] == 'Taste Mee':
            stall_name = request.form['action1']
            s_order.append(stall_name)
            return render_template('taste-mee.html')

        elif request.form['action1'] == 'Thirst Tea':
            stall_name = request.form['action1']
            s_order.append(stall_name)
            return render_template('thirst-tea.html')

@app.route("/second", methods = ['GET', 'POST'])
def order():
    global queue_number
    global s_order
    if request.method == 'POST':
        if request.form.getlist('gg') != []:
            selected = request.form.getlist('gg')
            remark = request.form.get('remarks')
            queue_number +=1
        elif request.form.getlist('ns') != []:
            selected = request.form.getlist('ns')
            remark = request.form.get('remarks')

            queue_number +=1
            
        elif request.form.getlist('oi') != []:
            selected = request.form.getlist('oi')
            remark = request.form.get('remarks')

            queue_number +=1
        elif request.form.getlist('tm') != []:
            selected = request.form.getlist('tm')
            remark = request.form.get('remarks')

            queue_number +=1

        elif request.form.getlist('tt') != []:
            selected = request.form.getlist('tt')
            remark = request.form.get('remarks')

            queue_number +=1

        conn = sqlite3.connect("raffleseatz.db")
        conn.execute("INSERT INTO Student_Order(Stall_Name, Dish, Queue_Number, Remarks) VALUES (?,?,?,?)", (s_order[0], ','.join(selected), queue_number, remark))
        conn.commit()
        conn.close()

        
        s_order = []
        return render_template("queue.html", queue_number=queue_number)


if __name__ == '__main__':
    app.run()

