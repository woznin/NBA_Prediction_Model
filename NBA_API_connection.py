import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog


def find_player_id(name):
    player_dict = players.get_active_players()
    player = [i for i in player_dict if i['full_name'] == name][0]
    return player['id']


def get_all_data(number_of_seasons, player):
    seasons = []
    for i in range(24-number_of_seasons, 24):
        seasons.append(f'20{i}-{i + 1}')

    player_performances = []

    for season in seasons:
        temp_seas_data = playergamelog.PlayerGameLog(player_id=player, season=season)
        temp_data_df = temp_seas_data.get_data_frames()[0]
        temp_po_data = playergamelog.PlayerGameLog(player_id=player, season=season, season_type_all_star='Playoffs')
        temp_po_data_df = temp_po_data.get_data_frames()[0]

        player_performances.append(temp_data_df)
        player_performances.append(temp_po_data_df)

    player_performances = [df for df in player_performances if len(df) > 0]
    all_data_df = pd.concat(player_performances, ignore_index=True)

    all_data_df['GAME_DATE'] = pd.to_datetime(all_data_df['GAME_DATE'], format='%b %d, %Y')
    all_data_df = all_data_df.sort_values(by='GAME_DATE')
    all_data_df.reset_index(drop=True, inplace=True)

    # dropping unnecessary columns
    all_data_df.drop(['SEASON_ID', 'Player_ID', 'Game_ID', 'FG_PCT', 'FG3_PCT',
                      'FT_PCT', 'REB', 'VIDEO_AVAILABLE'], axis=1, inplace=True)

    # Dropping None values is crucial due to None values being present in WL column while the game is live
    all_data_df.dropna(inplace=True)

    return all_data_df
