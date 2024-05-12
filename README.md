
# NBA Prediction Project


## Disclaimer
Under no circumstances should this project or its models be used for gambling or betting. It is strictly intended for educational and research purposes only.
## Description

The main assumption of this project and how it started was that individual statistics of a player are sufficient to predict the outcome of a match. The initial model used only logistic regression to predict the win or loss. It succeeded at about 80% efficiency varying on importance of player to the organizations success. 
The final version focuses on utilizing two machine learning models which hopefully are capable of predicting future matches outcomes and player performances.

## Setup
Before running the program make sure to change two variables below (found in main.py) to your desired player and matchup.
```python
player = ''
matchup = ''
```


## Models
### Logistic Regression
Logistic regression is used to model the probability that a given dataset belongs to a specific class. In our case, these classes represent the success (W) or defeat (L) of a team. This model will utilize individual player statistics to predict the outcome of a match.
### Linear Regression
Linear regression is used to model the relationship between independent variables and a dependent variable. In our project, linear regression will be used to predict player statistics based on data related to the opposing team. This model will attempt to find relationships between player statistics and the team they are playing against. It also takes into account whether the game is played away  or in the hometown of the team (NBA recognizes those differences by either writing @ or vs.).
## Data Source
The data used in this project is sourced from NBA-API, providing detailed player statistics and match outcomes. Player statistics encompass various parameters, MOST IMPORTANTLY the +- statistic as well as points scored, assists, blocks, etc. Match outcomes specify whether a team won or lost. Please refer to the NBA API terms of use regarding the appropriate usage of their data.
## Optimizations

To optimize models used there is a permanent Sequential Feature Selector put in place. A few columns were dropped from original data after conducting EDA.

### Technology used

**Libraries:** nba_api, seaborn, sklearn



## Authors

- [@woznin](https://github.com/woznin)

