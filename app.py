from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Carregar os dados
    df = pd.read_csv('data/sales_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Criar o gráfico
    fig, ax = plt.subplots()
    df.resample('M').sum()['Revenue'].plot(ax=ax)
    ax.set_title('Revenue per Month')
    ax.set_xlabel('Date')
    ax.set_ylabel('Revenue')

    # Converter gráfico em imagem
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
