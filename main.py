import pandas as pd
import NBA_API_connection
import Prediction
import Feature_optimalization


player = 'Luka Doncic'
matchup = 'DAL vs. OKC'

player_id = NBA_API_connection.find_player_id(player)

games_df = NBA_API_connection.get_all_data(number_of_seasons=6, player=player_id)
valid_columns = Feature_optimalization.optimize_features(games_df)
games_df = games_df[valid_columns]

wl_data = games_df.drop(['WL', 'GAME_DATE', 'MATCHUP'], axis=1)
wl_target = games_df['WL']

stats_target = games_df.drop(['WL', 'GAME_DATE', 'MATCHUP'], axis=1)
stats_data = games_df['MATCHUP']

stats_prediction = Prediction.performance_prediction(stats_data, stats_target, matchup)
stats_prediction = pd.DataFrame(stats_prediction.reshape(1, -1), columns=wl_data.columns)
wl_prediction = Prediction.wl_prediction(wl_data, wl_target, stats_prediction, True)

print(f'Predicted stats:\n{stats_prediction}')
print(f'Predicted outcome: {wl_prediction}')

