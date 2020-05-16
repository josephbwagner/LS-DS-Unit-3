"""Player class to record stats for individual players
"""


class Player:
    """THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    """

    def __init__(
        self,
        name=None,
        yards=120,
        touchdowns=1,
        safety=0,
        interceptions=0,
        field_goals=0,
    ):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        """Gets points scored by the player from stats
        """
        td_points = 6 * self.stats["td"]
        safety_points = 2 * self.stats["safety"]
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    """Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    """

    def __init__(
        self,
        name=None,
        yards=130,
        touchdowns=3,
        completed_passes=20,
        interceptions=4,
        safety=0,
        field_goals=0,
    ):
        super().__init__(
            name=name,
            yards=yards,
            touchdowns=touchdowns,
            safety=safety,
            interceptions=interceptions,
        )
        self.completed_passes = completed_passes

    def passing_score(self):
        """This is a random formula... FYI
        """
        score = self.completed_passes - (2 * self.interceptions)
        return score


class DefensivePlayer(Player):
    """Override certain parameters of the Player class and add some
       functionality unique to Defensive Players"""

    def __init__(
        self,
        name=None,
        yards=0,
        touchdowns=0,
        interceptions=1,
        safety=0,
        field_goals=0,
        sacks=2,
        tackles=11,
        defensive_fouls=0,
    ):
        super().__init__(
            name=name,
            yards=yards,
            touchdowns=touchdowns,
            interceptions=interceptions,
            safety=safety,
        )
        self.sacks = sacks
        self.tackles = tackles
        self.defensive_fouls = defensive_fouls

    def total_tackles(self):
        return self.tackles + self.sacks
