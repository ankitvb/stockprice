from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
#  if request.POST:
#    ticker = request.POST['ticker']
#    close = request.POST['close']
#    adjClose = request.POST['adjClose']  
#    open_ = request.POST['open']
#    adjOpen = request.POST['adjOpen']
#
#    print ticker, close, open_

  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
