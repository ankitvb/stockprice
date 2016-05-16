from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  try:
    print "Before GET"
    if request.method == 'GET':
      print "Inside GET"
      if request.args is not None:
        print "Inside request->args"
        print request.args
      else:
        print "Args not found"
  except:
    pass
  else:
    return render_template('index.html')

  return render_template('index.html')

if __name__ == '__main__':
  app.debug = True
  app.run(port=33507)
