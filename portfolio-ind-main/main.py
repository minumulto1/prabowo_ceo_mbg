#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')


#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_db = request.form.get('button_db')

    return render_template('index.html',button_python=button_python, button_db=button_db)

@app.route('/feedback', methods=['POST'])
def process_feedback():
    #menyimpan email dan text dari feedback ke dalam variabel
    email = request.form.get('email')
    text = request.form.get('text')

    with open("feedback.txt", "a") as f:
        f.write("Email: "+email+"\n")
        f.write("Text: "+text+"\n")

    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)

