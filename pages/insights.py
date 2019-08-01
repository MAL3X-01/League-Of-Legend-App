import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            
            For my first model the permutation table shows important features for the model prediction. Gold difference at minute 
            15 is the most important feature to determine the winning team. It makes sense for it to be the most weighted feature. Gold 
            allows a team to buy items in the game to make their champion stronger to fight. Gold is obtain by killing monsters and enemy 
            players in the game. These pro players maximize the amount gold they can get in a game so they can have an advantage. Usually
            once you have the lead in gold, it's really hard for the enemy team to catch up. Professional players leverage their gold lead 
            very well compared to amateur players. The team will start gaining map control for objectives and have a snowball effect to 
            victory. It's very crucial for a team to not fall behind in gold. The other features used in model changes the outcome when the 
            gold difference between team is very low.
            
            
            
            The partial dependence plot is showing the effect of the model when gold difference range from 0-10,000 gold.

            """
        ),
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.H2('Permutation Importance Pro Team Prediction Model', className='text-center'),
        html.Img(src='assets/perm1.png', className='rounded mx-auto d-block'),
        
        html.H2('Partial Dependence Plots Pro Team Prediction Model', className='text-center'),
        html.Img(src='assets/pdp1.png', className='img-thumbnail'),
        
        html.H2('Permutation Importance Surrender Model', className='text-center'),
        html.Img(src='assets/perm2.png', className='rounded mx-auto d-block'),
    ]
)

layout = dbc.Row([column1, column2])