import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smallersize screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What is LoL?
            
            League of Legends is a online multiplayer [MOBA](https://en.wikipedia.org/wiki/Multiplayer_online_battle_arena) game. There is 
            two teams with five players in each team. Each player is assign a special role and have to work cooperatively to destroy the 
            enemy nexus.
            
            
            """
        ),
        
        dcc.Markdown(
            """
        
            ## Make Gold for Victory
            
            Want to find out if your favorite professional team is going to win at the 15 minute mark? 
            
            
            """
        ),
        dcc.Link(dbc.Button('Pro Team Prediction', color='primary'), href='/predictions'),
        
       dcc.Markdown(
            """
        
            ## Focus on Objectives for Victory
            
            Find out if your chances of winning is low and surrender after the 15 minute mark unanimously.  
            
            
            """
        ),
        dcc.Link(dbc.Button('Surrender', color='primary'), href='/predictions'),
        
        dcc.Markdown(
            """
            ## Random Fact
            The plot to the right is a scatterplot with every kill locations from the dataset. All the empty spots are structures. 
            
            
            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Summoner Rift Map', className='text-center'),
        html.Img(src='assets/Summoners_rift_map.jpeg', className='img-fluid'),
        html.Img(src='assets/mapkill.png', className='img-fluid'),
    ],
    md=8,
        
    
)

layout = dbc.Row([column1, column2])