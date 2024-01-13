# NBA-wins-predictor-from-advanced-player-stats

# Overview

Contains code to:
    
1. [nba_reference_scrape_push_to_sql_database.ipynb](/nba_reference_scrape_push_to_sql_database.ipynb): Scrape nba standings data and player advanced statistics from basketball-reference.com and push these data to tables stored in a Microsoft SQL Express database. In this script, I also practice working with SQLAlchemy using declarative classes and both textual and pythonic queries. 

2. [nba_pytorch_models.ipynb](/nba_pytorch_models.ipynb): Prepare predictive features for each season+team based on advanced stats from players in that season. Then use pyTorch to train variations on custom feedforward neural networks and evaluate performance. Finally, explore the basics of interpretability using Captum.     

A summary of the models created, thought process, and final results is written at the beginning of nba_pytorch_models.ipynb.