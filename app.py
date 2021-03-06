from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.charts import Line
from bokeh.embed import components 
from bokeh.resources import CDN

import requests
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  """Generating the main user facing page"""
  # See if we have params to process
  try:
    if request.method == 'GET':
      if request.args is not None:
        stock_args = dict(request.args.to_dict().items())
        df = get_data(stock_args)
        if df is not None:
          script,div = plot(df, stock_args['ticker'])
          return render_template('plot.html', script=script, div=div, symbol=stock_args['ticker'])
        else:
          print "Failed to get data. Abort."
      else:
        print "Args not found"
  except:
    pass
  #else:
  #  return render_template('index.html')

  return render_template('index.html')

def get_data(stock_args):
  """Getting data from Quandl API and putting it into Pandas dataframe
  """
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
  start_date = "" 
  end_date = ""
  # Get column ids for data of interest
  col_list = [data_cols.index(translate[key]) for key in stock_args if key not in ['ticker']]
  print col_list

  # Get data from Quandl
  # and convert to list of lists to be consumed by pandas
  qdl_full_url = qdl_base_url + stock_args['ticker'] + ".csv" \
               + "?api_key="+api_key

  res = requests.get(qdl_full_url)
  if res.status_code != 200:
    print "Could not get data from Quandl. Check ticker name"
    return None
  else:
    data = [list(line.split(',')) for line in res.iter_lines()] 
    headers = data[0]
    #print headers
  
    # Dump data into Pandas dataframe
    df = pd.DataFrame(data[1:], columns=headers)
    df[['Open', 'Close', 'Adj. Open', 'Adj. Close']]  \
    = df[['Open', 'Close', 'Adj. Open', 'Adj. Close']].astype('float64',copy=False)

    #print df.dtypes 

  return df  

#@app.route('/plot')
def plot(stock_df,symbol):
  """Generate a embedded html plot from dataframe data with Bokeh
  """
  reduced_df = stock_df[['Date','Open','Close']].copy()
  reduced_df = reduced_df.head(n=10)

  # Create plot
  ylabel = symbol + " stock price ($)"

  p = Line(reduced_df, x='Date', y=['Open','Close'], legend="top_right", ylabel=ylabel)

  script, div = components(p,CDN)
  
  print "Plotting figure"

  return script, div #render_template('plot.html')

#  return render_template('plot.html')

if __name__ == '__main__':
  app.run(port=33507, debug=True)
