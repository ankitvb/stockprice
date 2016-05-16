from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index(request):
  if request.GET:
    ticker = request.GET['ticker']
    close = request.GET['close']
    adjClose = request.GET['adjClose']  
    open_ = request.GET['open']
    adjOpen = request.GET['adjOpen']

    print ticker, close, open_

  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
