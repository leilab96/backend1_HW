# type: ignore
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


from flask import Flask
from flask import send_file
app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
    with open('income.txt', 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        data_source = [list(map(int, line.strip().replace(' ', '').split(','))) for line in lines[1:]]
 
    
    df = pd.DataFrame(data_source, columns=header)
    sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    





