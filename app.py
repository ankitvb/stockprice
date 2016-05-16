from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  try:
    if request.method == 'GET':
      if request.args is not None:
        print dict(request.view_args.items()+request.args.to_dict().items())
      else:
        print "Args not found"
  except:
    pass
  else:
    return render_template('index.html')

  return render_template('index.html')

#def get_data(request_args):
  

#@app.route('/plot')
#def plot(request_args):


#  return render_template('plot.html')

if __name__ == '__main__':
  app.debug = True
  app.run(port=33507)
