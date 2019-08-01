import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipe2 = load('assets/pipe2.joblib')

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown('## How likely your favorite team is going to win', className='mb-5'), 
        dcc.Markdown('## Gold Difference @ 15 Minutes, Blue Advantage=+'), 
        dcc.Slider(
            id='min_15', 
            min=-5000, 
            max=5000, 
            step=250, 
            value=None, 
            marks={n: str(n) for n in range(-5000,6000,1000)}, 
            className='mb-5', 
        ),
        dcc.Markdown('#### First Dragon'), 
        dcc.Dropdown(
            id='First_Dragon', 
            options = [
                {'label': 'Blue', 'value': 0}, 
                {'label': 'Red', 'value': 1},  
            ], 
            value = None, 
            className='mb-5', 
        ),
        dcc.Markdown('#### First Tower'), 
        dcc.Dropdown(
            id='First_Tower', 
            options = [
                {'label': 'Blue', 'value': 0}, 
                {'label': 'Red', 'value': 1},  
            ], 
            value = None, 
            className='mb-5', 
        ),
        dcc.Markdown('#### First Herald'), 
        dcc.Dropdown(
            id='First_Herald', 
            options = [
                {'label': 'No Team', 'value': 0}, 
                {'label': 'Blue', 'value': -1}, 
                {'label': 'Red', 'value': 1},  
            ], 
            value = None, 
            className='mb-5', 
        ),
        dcc.Markdown('#### First Blood'), 
        dcc.Dropdown(
            id='First_Blood', 
            options = [
                {'label': 'Blue', 'value': 0}, 
                {'label': 'Red', 'value': 1},  
            ], 
            value = None, 
            className='mb-5', 
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Winning Team ', className='text-center'), 
        html.H3(id='prediction-content', className='text-center'),
        html.Img(src='assets/lolvictory.jpg', className='rounded mx-auto d-block')
    ]
)

layout = dbc.Row([column1, column2])

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('min_15', 'value'), Input('First_Dragon', 'value'), Input('First_Tower', 'value'),        
     Input('First_Herald', 'value'), Input('First_Blood', 'value')
 ])
def predict(min_15, First_Dragon, First_Tower, First_Herald, First_Blood):
    df = pd.DataFrame(
        columns=['min_15', 'First_dragon', 'First_Tower', 'First_Herald', 'First_Blood'], 
        data=[[min_15, First_Dragon, First_Tower,First_Herald, First_Blood]]
    )
    y_pred = pipe2.predict(df)[0]
    if y_pred == 0:
        y_pred = 'Blue Team'
    else:
        y_pred = 'Red Team'
    return y_pred