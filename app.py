from flask import Flask, render_template   

app = Flask(__name__)    



@app.route('/')
def index():
    return "hello, world"




@app.route('/index/<num>')          
def bye_world(num):
    return render_template('index.html',num=int(num))  


@app.route('/index/<num>/<color>')
def hello_world(num,color):
    return render_template('index.html',num=int(num),color=color) 






if __name__=="__main__":   
    app.run(debug=True)    