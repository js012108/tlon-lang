import sys
IS_PY2 = sys.version_info < (3, 0)

if IS_PY2:
    from Queue import Queue
else:
    from queue import Queue

from tlon.agent_factory.abstract_agent import *
from random import randint
from threading import Thread

class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()
class ThreadPool:
    """ Pool of threads consuming tasks from a queue """
    def __init__(self, workers):
        self.tasks = Queue(len(workers))
        for worker in workers:
            worker.worker_tread=Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()

class SocialAgent(AbstractAgent):
    #def __init__(self):
    worker_tread = Worker
    max_treads = 100
    confidence = {}
    strategylist = ["Nice", "TitForTat", "Selfish"]

    ################################Functions for coalition coordination#####################

    def set_community_id(self,id):
        self.community_id=id;

    def play_game(self,opponent,CS):

        # If this opponent is in my same coalition just cooperate to gain the most we can
        #  calculated as score  else play the game with opponent

        if (opponent.get_agents("coordinator").community_id == CS.get_agents("coordinator").community_id):
            G_score=CS.calculate_difficult
            return {"coalition":True,"scores":{self.community_id: G_score}}

        game=CS.play(opponent)
        scores = game.getScores()

        CS.get_agents("registrator").setConfidence(opponent.id,scores[opponent.id]-scores[str(self.community_id)])
        opponent.get_agents("registrator").setConfidence(self.community_id,scores[str(self.community_id)]-scores[opponent.id])

        if game.getStrategyList()[opponent.id] not in CS.strategylist:
          CS.strategylist.append(game.getStrategyList()[opponent.id])#game.guess.strategy

        return {"coalition":False,"game":game}

    def defineStrategy(self,nodeid,CS):
        if (CS):
            opponent=CS.games_directory[str(nodeid)].get_agents()[1].defineStrategy(self.community_id,False)
            print ("Oppenent Strategy",opponent)
            if self.getConfidence(nodeid):
                strategy={self.community_id:self.strategylist[randint(0,2)],nodeid:opponent}
            else:
                strategy={self.community_id:self.strategylist[randint(0,2)],nodeid:opponent}
            print("Agents strategys", strategy)
        else:
            if self.getConfidence(nodeid):
                strategy=self.strategylist[randint(0,2)]
            else:
                strategy=self.strategylist[randint(0,2)]
            print("Agents strategys", strategy)
        return strategy

    def defineGameMatrix(self,nodeid,BOARDS,CS):
        if self.getConfidence(nodeid):
            #n = randint(1, 3)
            Board="TotalCoverageMatrix"#list(BOARDS.keys())[n]
            print("Confidence -> Board defined:::::::",Board)
        else:
            Board = "SocialDilemmaMatrix"#list(BOARDS.keys())[0]
            print("NOT Confidence -> Board defined:::::::",Board)
        return Board
##################################################Functions for coalition registration########################################

    def getConfidence(self,nodeid=0):
        if nodeid in self.confidence:
            return self.confidence[nodeid]
        else:
            return False

    ##############################################################################
    # setConfidence(self,nodeid,profit)
    #
    # If there wasnt negative profit for my coalition set confidence true
    # if there was a lose then make a reciprocity function calculled
    # as forced cooperation or punishment
    #############################################################################
    def setConfidence(self,nodeid,profit):

        self.confidence[nodeid] = [True if profit >= 0 else False]
        self.confidence[nodeid] = self.get_reciprocity(nodeid, self.confidence[nodeid])

        print ("Confidence ",[True if profit >= 0 else False]," between ",self.community_id," and ",nodeid)

    def get_reciprocity(self, nodeid,actual_confidence):
        return actual_confidence

    ###############################################################################
    # Check if both has confidence on each other, then collude
    #
    #
    ################################################################################
    def collude(self,opponentCS,CS):
        a = self.getConfidence(opponentCS.id)[0]
        b = opponentCS.get_agents("registrator").getConfidence(self.community_id)[0]
        if (a and b):
            agents=opponentCS.get_agents()
            workers=opponentCS.get_workers()
            for agent in agents:
                agent.set_community_id(self.community_id)
                print ("Agente",agent.description,"asignado a Coalición",self.community_id,"-->",agent.community_id)
            for worker in workers:
                worker.set_community_id(self.community_id)
                CS.workers.add(worker)
                print (
                "Worker", worker.description, "asignado a Coalición", self.community_id, "-->", worker.community_id)
            return self.community_id
        return False

    def social_work(self,data,CS):
        def wait_delay(d):
            from time import sleep

            print("sleeping for (%d)sec" % d)
            sleep(d)

        import time # Generate random delays
        from random import randrange  # Generate random delays
        delays = [randrange(1, 2) for i in range(60)]

        print ("Coalition",self.community_id," working!!")
        workers = CS.get_workers()
        selected_workers=[]
        for i, val in enumerate(random.sample(workers, len(workers) if len(workers)<self.max_treads else self.max_treads)):
            selected_workers.append(val)
        print(len(selected_workers[:self.max_treads]), " Workers")
        start_time = time.time()
        pool=ThreadPool(selected_workers[:self.max_treads])
        pool.map(wait_delay, delays)
        pool.wait_completion()
        # your code
        elapsed_time = time.time() - start_time
        return elapsed_time, len(selected_workers[:self.max_treads]),{"max_workers":len(workers)}
        #for k, v in some_dict.iteritems():
        #    new_dict[v].append(k)
        #for : #allAgents (TheadPool) in my coalition except me and regsitrator, work on data
        #    CS.get_common_space().games_directory[str(opponent.id)].get_agents()[1].setConfidence(True,


    def get_control_space (self):
        #s =
        return

    def run_all(self, inputs):
        for i in inputs:
            print(i)
            self.currentState = self.currentState.next(i)
            self.currentState.action()