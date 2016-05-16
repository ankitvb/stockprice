from flask import Flask, render_template, request, redirect
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  # See if we have params to process
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
  
  # Translate from template variables to API variables
  translate = {'open':'Open',
               'close':'Close',
               'volume':'Volume',
               'adjOpen':'Adj. Open',
               'adjClose':'Adj. Close',
               'adjVolume':'Adj. Volume'
              }

  # Default columns in Quandl stock data
  data_cols = ['Date','Open','High','Low','Close','Volume',
               'Ex-Dividend','Split' 'Ratio',
               'Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']

  # Parameters for call to the Quandl API

  # Get column ids for data of interest
  for key in stock_args:
    if key != 'ticker':
      print translate[key]
  #col_list = [data_cols.index(translate[key]) for key,_ in stock_args.items()]
  #print col_list

  # Get data from Quandl
  # and convert to list of lists to be consumed by pandas
  qdl_full_url = qdl_base_url + stock_args['ticker'] + ".csv" \
               + "?api_key="+api_key

  res = requests.get(qdl_full_url)
  data = [line for line in res.iter_lines()]  
  headers = data.pop(0)
  print headers

  # Dump data into Pandas dataframe
  df = pd.DataFrame(data, columns=headers)
  print df 


#@app.route('/plot')
#def plot(request_args):


#  return render_template('plot.html')

if __name__ == '__main__':
  app.debug = True
  app.run(port=33507)
