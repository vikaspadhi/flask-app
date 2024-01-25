from flask import Flask , render_template

app = Flask(__name__)

# Configure the app to serve static files from the 'static' folder
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html',ctx={'title':'JOBFLARE | HOME'})



if __name__ =="__main__":
    app.run(debug=True)