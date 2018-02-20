from tlon.agent_factory.abstract_agent import *


class SingleActionAgent(AbstractAgent):

    class AnAction(OneShotBehavior):
        def on_start(self):
            logging.info('Starting behaviour...')

        def _single_action(self):
            logging.info('I am a single action agent!')

        def on_end(self):
            logging.info('Ending behaviour...')

    def _setup(self):
        b = self.AnAction()
        self.add_behaviour(b, None)
        b.start()
