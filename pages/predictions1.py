import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipe3 = load('assets/pipe3.joblib')

from app import app
CHANGE_COLOR = {'color': 'black',}


column1 = dbc.Col(
    [
        dcc.Markdown('#### First Blood'), 
        dcc.Dropdown(
            id='First_Blood', 
            options = [
                {'label': 'Blue', 'value': 0}, 
                {'label': 'Red', 'value': 1},  
            ], 
            value = None, 
            className='mb-5',
            style=CHANGE_COLOR,
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
            style=CHANGE_COLOR,
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
            style=CHANGE_COLOR,
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
            style=CHANGE_COLOR,
        ),
        dcc.Markdown('#### First Baron'), 
        dcc.Dropdown(
            id='First_Baron', 
            options = [
                {'label': 'No Team', 'value': 0},
                {'label': 'Blue', 'value': -1},
                {'label': 'Red', 'value': 1},  
            ], 
            value = None, 
            className='mb-5', 
            style=CHANGE_COLOR,
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Winning Team ', className='text-center'), 
        html.H3(id='prediction-content1', className='text-center'),
        html.Img(src='assets/lolvictory.jpg', className='rounded mx-auto d-block')
    ]
)

layout = dbc.Row([column1, column2])

import pandas as pd

@app.callback(
    Output('prediction-content1', 'children'),
    [Input('First_Dragon', 'value'), Input('First_Tower', 'value'),        
     Input('First_Herald', 'value'), Input('First_Blood', 'value'), Input('First_Baron', 'value')
 ])
def predict(First_Dragon, First_Tower, First_Herald, First_Blood, First_Baron):
    df1 = pd.DataFrame(
        columns=['First_dragon', 'First_Tower', 'First_Herald', 'First_Blood', 'First_Baron'], 
        data=[[First_Dragon, First_Tower,First_Herald, First_Blood, First_Baron]]
    )
    y_pred1 = pipe3.predict(df1)[0]
    if y_pred1 == 0:
        y_pred1 = 'Blue Team'
    else:
        y_pred1 = 'Red Team'
    return y_pred1