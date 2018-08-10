from flask import Flask , render_template, flash, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/my_work')
def mywork():
    return render_template('mywork.html')



if __name__ == '__main__':
    app.secret_key='secret1231231923'
    app.run(debug=True)


    


  
   
