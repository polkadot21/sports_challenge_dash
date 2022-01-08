from scripts.main import plot_cum_chart, load_data, plot_bar_chart
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chart():
    path = 'data/event1.xlsx'
    df = load_data(path)

    graphJSON_bar = plot_bar_chart(df)
    graphJSON_cum = plot_cum_chart(df)

    return render_template('graph.html',
                           graphJSON_bar = graphJSON_bar,
                           graphJSON_cum = graphJSON_cum)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)


