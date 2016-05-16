from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  try:
    if request.method == 'GET':
      if request.args is not None:
        stock_args = dict(request.args.to_dict().items())
        get_data(stock_args)
      else:
        print "Args not found"
  except:
    pass
  else:
    return render_template('index.html')

  return render_template('index.html')

def get_data(stock_args):
  qdl_base_url = "https://www.quandl.com/api/v3/datasets/WIKI/"
  api_key = "QndbBLZGfwiqgg_MkvWW" 
  
  translate = {'open':'Open',
               'close':'Close',
               'volume':'Volume',
               'adjOpen':'Adj. Open',
               'adjClose':'Adj. Close',
               'adjVolume':'Adj. Volume'
              }

  cols = ['Date','Open','High','Low','Close','Volume',
          'Ex-Dividend','Split' 'Ratio',
          'Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']

  
  qdl_full_url = qdl_base_url + stock_args['ticker'] + ".csv"
               + "?api_key="+api_key
  print qdl_full_url

  res = requests.get(qdl_full_url)
  data = [line for line in res.iter_lines()]  

  print data

#@app.route('/plot')
#def plot(request_args):


#  return render_template('plot.html')

if __name__ == '__main__':
  app.debug = True
  app.run(port=33507)
