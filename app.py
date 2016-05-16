from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  if request.method == 'GET':
    ticker = request.form['ticker']
    close = request.form['close']
    adjClose = request.form['adjClose']  
    open_ = request.form['open']
    adjOpen = request.form['adjOpen']

    print ticker, close, open_

  return render_template('index.html')

if __name__ == '__main__':
  app.debug = True
  app.run(port=33507)
