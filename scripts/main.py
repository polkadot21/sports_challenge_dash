import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import json
import plotly


def load_data(path):
    df = pd.read_excel(path)

    columns = [
        'Date',
        'Sum_1',
        'Sum_2',
        'Sum_3',
        'Sum_4',
        'Sum_5',
        'Sum_6',
        'Sum_7']

    df = df[columns]
    df.index = pd.to_datetime(df['Date'])
    return df


def plot_bar_chart(df):
    traces = []
    teams = df.columns.to_list()[1:]
    fig = go.Figure()
    fig.update_layout(width=1400,
                               height=600,
                               template=pio.templates['plotly_white'],
                               title="Daily results of Event 1")

    for team in teams:
        trace = go.Bar(x=df.index,
                             y=df[team],  # temperature
                             showlegend=True,
                             name = 'Team {}'.format(teams.index(team)+1)
                             )
        traces.append(trace)
    fig.add_traces(traces)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def plot_cum_chart(df):
    teams = df.columns.to_list()[1:]
    df_ = df[teams]
    #cumulative kms
    for i in range(0, len(df_)-1):
        df_.iloc[i+1] = df_.iloc[i] + df_.iloc[i+1]

    traces = []
    fig = go.Figure()
    fig.update_layout(width=1400,
                               height=600,
                               template=pio.templates['plotly_white'],
                               title="Overall results after Event 1")

    for team in teams:
        trace = go.Scattergl(x=df_.index,
                             y=df_[team],  # temperature
                             showlegend=True,
                             name='Team {}'.format(teams.index(team) + 1)
                             )
        traces.append(trace)
    fig.add_traces(traces)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON