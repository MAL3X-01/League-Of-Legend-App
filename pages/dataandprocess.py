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
        
            ## Data and Process
            
            
            The dataset is 7621 profesional League games from 2015 to 2017 and includes many teams from different regions.
            Results should be different with many updates the game had. The data was obtain from [kaggle]
            (https://www.kaggle.com/chuckephron/leagueoflegends#LeagueofLegends.csv). 
            
            
            My objective was to predict profesional team winning probabilty at the 15 minute mark. It is determine by the gold difference and 
            first to obtain objectives. This model has over 70% accuracy score because 15 minute is still early in the game. The surrender 
            model can be used by anyone to determine if they are going to win or lose based on first to obtain objectives. The surrender 
            model has over a 80% accuracy score.
            
            
            There was many csv file I had to reformat so I can merge all the csv into one dataframe. I wanted to figure out what team obtain 
            the objectives first and feature engineer those new columns. Dropped many features that wouldnt be useful to my objective for 
            this model. 
            
            
            
            ## Disclaimer
            Knowing League of Legends goes through constant updates and data is based of profesional gamers. The prediction of the model 
            might not be as accurate for the current version of LOL and varies depending on skill level.
            
            """
        ),

    ],
)

layout = dbc.Row([column1])