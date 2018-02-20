#!/usr/bin/env python3


import random

from tlon.agent_factory.agents.programmed.State import *

from tlon.agent_factory.behaviors import *

BOARDS = {
    'SocialDilemmaMatrix': {(1, 1): (2, 2),
                            (0, 1): (3, 0),
                            (1, 0): (0, 3),
                            (0, 0): (1, 1)},

    'CoordinationMatrix': {(1, 1): (1, 1),
                           (0, 1): (0, 0),
                           (1, 0): (0, 0),
                           (0, 0): (1, 1)},

    'TotalCoverageMatrix': {(1, 1): (3, 3),
                            (0, 1): (2, 2),
                            (1, 0): (2, 2),
                            (0, 0): (1, 1)},

    'PartialCoverageMatrix': {(1, 1): (3, 3),
                              (0, 1): (2, 2),
                              (1, 0): (2, 5),
                              (0, 0): (1, 1)}
}


class Game():
    """It takes a list of players, a payout matrix and a number of rounds.
    It exposes a play() function which triggers a single match and a start() function which 'plays'
    as many rounds as specified in constructor."""

    def __init__(self, players, matrix, rounds):
        self._players = players
        self._rounds = rounds
        self._board = BOARDS[matrix]

    def start(self):
        scores = {}
        [self.play() for _ in range(self._rounds)]
        for player in self._players:
            scores[player.name] = player.getScore()

        print('*** END OF GAME***', scores, '\n')
        return self

    def getScores(self):
        scores = {}
        for player in self._players:
            scores[player.name] = player.getScore()
        return scores

    def getStrategyList(self):
        strategy = {}
        for player in self._players:
            strategy[player.name] = player.strategy
        return strategy

    def play(self):
        plays = [player.play() for player in self._players]
        results = Game.resolve(self._board, tuple(plays))
        [self._players[idx].update(*results[idx]) for idx in range(len(self._players))]

    @staticmethod
    def resolve(matrix, plays):
        """Given a payout matrix, and a list of plays, it returns a list of tuples
           containing the calculated payout and the opponent's play."""
        # print (list(zip(matrix[plays], tuple(reversed(plays)))))
        return list(zip(matrix[plays], tuple(reversed(plays))))


class Player:
    """A player has a name, a strategy, a score and a context.
       The context is the opponent's last play.
       The result of the next play will depend on the context (mutable) and the strategy (immutable)."""

    def __init__(self, name, strategy):
        self._name = name
        self._strategy = strategy
        self._score = 0
        self._context = None

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self._name

    @property
    def strategy(self):
        return self._strategy.__class__.__name__

    def play(self):
        return self._strategy.decide(self._context)

    def update(self, score, rs):
        self._score += score
        self._context = rs

    def reset(self):
        self._score = 0

    def getScore(self):
        return self._score

    def __str__(self):
        return self.name + ' scored ' + str(self.score) + ' with strategy ' + self.strategy


class ControlSpace(object):
    """Control space for Coalition """

    def __init__(self, nodeId, environment):
        self.id = random.random()
        self.coordinator = SocialAgent(State(), "Coordinator Agent for Coalition: " + str(self.id), self.id)
        self.coordinator.getConfidence()
        self.registrator = SocialAgent(State(), "Registrator Agent for Coalition:" + str(self.id), self.id)
        self.common_space = environment
        self.workers = set([])
        for a in [0,3]:
            self.workers.add(SocialAgent(State(), "Worker Agent for Coalition:" + str(self.id), self.id))
        print ("Workers for Coalition:", str(self.id),": ",self.workers)

        #######################Coalition definitions#########################
        self.confidence = {}
        self.strategylist=[]

    #####################################################################
    # get_agents(self,agent=None)
    #
    # Function that returns control agents (registrator and coordinator)
    # of coalition.
    #####################################################################
    def get_agents(self, agent=None):
        if agent:
            keys = {"coordinator": self.coordinator, "registrator": self.registrator}
            return keys.get(agent)
        return [self.coordinator, self.registrator]

    #####################################################################
    # calculate_difficult(self)
    #
    # Property or coalition that represents its resources and gain in each
    #  cooperative game
    ######################################################################
    @property
    def calculate_difficult(self):
        return 200

    #####################################################################
    # get_workers(self) --> set(workerAgents)
    #
    # Function that returns pool of worker agents of the coalition
    #####################################################################
    def get_workers(self):
        return self.workers

    #####################################################################
    # play(self, data)
    #
    # Play Game between my coalition and guess (opponent)
    # Define Game Matrix based on confidence info
    ######################################################################
    def play(self, data):
        #Play the Game beteen my coallition and guess
        rounds_per_game = 100 #Load history!!
        game_matrix = self.coordinator.defineGameMatrix(data.id,BOARDS,self.common_space)
        #get game type Coordination, partial cover, total cover or PD??
        print("********************Game Matrix:", game_matrix,"***********************")
        strategies = self.coordinator.defineStrategy(data.id, self.common_space)
        guess = Player(data.id, globals()[strategies.get(data.id)]())
        coalition = Player(str(self.id), globals()[strategies.get(self.id)]())
        game = Game([guess, coalition],game_matrix, rounds_per_game).start()
        # Pay with  scores by delay function
        return game

    #####################################################################
    # collude(self,opponent):
    #
    # Check if both has confidence on each other, then collude
    # opponent = self
    ####################################################################

    def collude(self,opponent):
            if (self.registrator.collude(opponent, self)):
                opponent = self
        #change it in nodes_directory -> agregate coalitiondi agents to opponent.get_agents[0].collude(self.id) coalition

    #####################################################################
    # work(self,data)
    #
    # Ask coalition coordinator to asign data (work)
    # to workers pool.
    ######################################################################
    def work(self,data):
        result=self.coordinator.social_work(data,self)
        return result

def main():
    ############################################################
    #               ControlSpace - Initial Setup
    ############################################################
    control_space = ControlSpace("CS")


if __name__ == "__main__":
    # execute only if run as a script
    main()