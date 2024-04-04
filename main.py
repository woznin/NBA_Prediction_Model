import pandas as pd
import Player_stats
import Prediction

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

player = 'Devin Booker'
matchup = 'PHX vs. CLE'

player_id = Player_stats.find_player_id(player)
seasons = []

for i in range(18, 24):
    seasons.append(f'20{i}-{i+1}')


seasons_dataframes = []
for season in seasons:
    reg_season_data_singular = Player_stats.get_reg_seas_data(season, player_id)
    po_season_data_singular = Player_stats.get_po_data(season, player_id)
    seasons_dataframes.append(reg_season_data_singular)
    seasons_dataframes.append(po_season_data_singular)


seasons_all_data = pd.concat(seasons_dataframes, ignore_index=True)
print(seasons_all_data)
seasons_wl_data_x = seasons_all_data.drop(['WL', 'GAME_DATE', 'MATCHUP'], axis=1)
seasons_wl_data_y = seasons_all_data['WL']
seasons_stats_data_y = seasons_all_data.drop(['WL', 'GAME_DATE', 'MATCHUP'], axis=1)
seasons_stats_data_x = seasons_all_data['MATCHUP']
stats_prediction = Prediction.stats_model_process(seasons_stats_data_x, seasons_stats_data_y, matchup)
stats_prediction = pd.DataFrame(stats_prediction.reshape(1, -1), columns=['REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS'])
print(f'Predicted stats:\n{stats_prediction}')
Prediction.wl_model_process(seasons_wl_data_x, seasons_wl_data_y, stats_prediction)
