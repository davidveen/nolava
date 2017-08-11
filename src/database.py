"""
Everything to do with data
"""

from typing import List

import src.data_access as boomerdb
import src.common.enums as enums
import src.common.model as model


def add_slack_user(slack_id: str, name: str, super_user: bool=False) -> None:
    """
    Add Slack user to the database.
    """
    sql = "INSERT INTO SlackUser (SlackID, Name, Participating) VALUES(?, ?, 1)"

    boomerdb.query(sql, slack_id, )


def user_join(client_id: int, slack_id: str) -> None:
    """
    User will be included as player the next time a new game is started.
    """
    raise NotImplementedError


def user_leave(client_id: int, slack_id: str) -> None:
    """
    User will not be included as player the next time a new game is started.
    """
    raise NotImplementedError


def get_game(client_id: str) -> model.Game:
    """
    Return current game.
    """
    raise NotImplementedError


def new_game(client_id: str) -> model.Game:
    """
    Create a new game.
    # mission counter should be 1
    # (automatically create first mission with proposal count 0, status PROPOSING)
    # position should be 1
    # game state should be empty
    """
    raise NotImplementedError


def get_slackuser(slack_id: str) -> model.SlackUser:
    raise NotImplementedError


def get_player_by_position(position: int) -> model.Player:
    raise NotImplementedError


def get_player_by_slack_id(slack_id: str) -> model.Player:
    raise NotImplementedError


def get_players_in_order(starting_position: int=1) -> List[model.Player]:
    raise NotImplementedError


def check_player_has_joined(client_id: int, slack_id: str) -> bool:
    raise NotImplementedError


def get_available_users(client_id: int) -> List[model.SlackUser]:
    raise NotImplementedError


def register_player(game_id: int, slack_id: str, role: int, position: int):
    raise NotImplementedError


def set_game_state(game_id: int, target_state: enums.GameState):
    raise NotImplementedError


def register_proposal(game_id: int):
    raise NotImplementedError


def register_team_vote(
    game_id: int,
    player_id: int,
    vote: bool,
    message: str
) -> bool:
    """
    Register team vote
    Return False if player already voted.
    """
    raise NotImplementedError


def register_mission_vote(
    game_id: int,
    player_id: int,
    vote: bool
) -> bool:
    """
    Register team vote
    Return False if player already voted.
    """
    raise NotImplementedError


def get_player_by_name(game_id: int, player_name: str):
    raise NotImplementedError


def get_next_message():
    raise NotImplementedError


def mark_message_posted(message_id):
    pass


def _get_mission(game_id):
    # get active mission
    raise NotImplementedError


def _get_proposal(mission_id):
    # get active proposal
    raise NotImplementedError


def get_players(game_id) -> List[model.Player, ...]:
    raise NotImplementedError


def get_players_on_mission(game_id) -> List[model.Player, ...]:
    raise NotImplementedError


def get_mission_votes(game_id) -> List[model.Vote, ...]:
    raise NotImplementedError


def get_proposal_votes(game_id) -> List[model.Vote, ...]:
    raise NotImplementedError


def get_leader(game_id):
    # get active leader
    raise NotImplementedError


def _get_assassin(game_id):
    # get assassin player id
    raise NotImplementedError
