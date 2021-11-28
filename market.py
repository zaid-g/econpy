from probability import sample_item_from_dictionary
from uuid import uuid4
from misc_functions import deepcopy
from human import Human


class Market:
    def __init__(
        self,
        num_humans,
        market_role_distribution,
        market_role_production_distribution_dict,
        market_item_happiness_distribution_dict,
    ):
        self.market_role_distribution = market_role_distribution
        self.market_role_production_distribution_dict = (
            market_role_production_distribution_dict
        )
        self.market_item_happiness_distribution_dict = (
            market_item_happiness_distribution_dict
        )
        self.humans = self.init_humans(num_humans)
        self.happiness = self.compute_happiness()

    def init_humans(self, num_humans):
        """initialize humans in marketplace based on market settings"""
        humans = [
            Human(
                uuid4(),
                self.market_role_distribution,
                self.market_role_production_distribution_dict,
                self.market_item_happiness_distribution_dict,
            )
            for i in range(num_humans)
        ]
        return humans

    def get_number_of_humans(self):
        return len(self.humans)

    def compute_happiness(self):
        """for each human in market, add the happiness"""
        happiness = 0
        for human in self.humans:
            happiness += human.compute_happiness()
        return happiness

    def run_purchase_process_greedy(self, human_index):
        """lets the human identified by human_index interact and transact
        with all other humans in the market to maximize happiness. Trading
        strategy o follows is greedy, meaning that at each timestep he
        completes a transaction that maximizes the gain in happiness


        Args:
            human_index (TODO): TODO

        Returns: TODO

        """
        human = self.humans[human_index]
        other_humans = [human for human in self.humans if human != human]
