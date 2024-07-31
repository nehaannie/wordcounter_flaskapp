from flask import Flask,render_template,request

app=Flask(__name__)

def multiple_newlines(text):
    lines=text.split('\n');
    lines = [i for i in lines if i.strip()]
    return len(lines)

#homepage
@app.route("/")
def home():
    return render_template("index.html");

#### form
@app.route('/count',methods=['GET','POST'])
def count():
    text = request.form['text']
    words = len(text.split())
    lines=text.split('\n');
    lines = [i for i in lines if i.strip()]
    paras = len(lines)

    text = text.replace('\r','')
    text = text.replace('\n','')

    chars = len(text)
    return render_template('index.html',words=words,paras=paras,chars=chars) 


#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)