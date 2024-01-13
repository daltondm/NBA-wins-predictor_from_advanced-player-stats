# NBA-wins-predictor-from-advanced-player-stats

# Overview

Contains code to:
    
1. nba_reference_scrape_and_sql.ipynb: Scrape nba standings data and player advanced statistics from basketball-reference.com and push these data to tables stored in a Microsoft SQL Express database. In this script, I also practice working with SQLAlchemy using declarative classes and both textual and pythonic queries. 

2. nba_pytorch_practice.ipynb: Prepare predictive features for each season+team based on advanced stats from players in that season. Then use pyTorch to train variations on custom feedforward neural networks and evaluate performance. Finally, explore the basics of interpretability using Captum.     
