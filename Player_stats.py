from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog


stats_to_keep = ['WL', 'MATCHUP', 'GAME_DATE', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS']


def find_player_id(name):
    player_dict = players.get_players()
    player = [i for i in player_dict if i['full_name'] == name][0]
    return player['id']


def get_reg_seas_data(season, player):
    games_data = playergamelog.PlayerGameLog(player_id=player, season=season)
    games_data_df = games_data.get_data_frames()[0]
    games_data_df = games_data_df[stats_to_keep]
    return games_data_df


def get_po_data(season, player):
    po_games_data = playergamelog.PlayerGameLog(player_id=player, season=season, season_type_all_star='Playoffs')
    po_games_data_df = po_games_data.get_data_frames()[0]
    po_games_data_df = po_games_data_df[stats_to_keep]
    return po_games_data_df
