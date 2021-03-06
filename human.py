from probability import sample_item_from_dictionary
from uuid import uuid4
from misc_functions import deepcopy


class Human:
    def __init__(
        self,
        uid,
        market_role_distribution,
        market_role_production_distribution_dict,
        market_item_happiness_distribution_dict,
    ):
        self.uid = uid
        self.role = self.assign_role(market_role_distribution)
        self.personal_production = self.compute_personal_production(
            market_role_production_distribution_dict
        )
        self.items = {}
        self.personal_item_happiness_dict = self.compute_personal_item_happiness_dict(
            market_item_happiness_distribution_dict
        )

    def assign_role(self, market_role_distribution):
        """based on market role distribution, sample this specific human's role

        Args:
            market_role_distribution (TODO): TODO

        Returns: TODO

        """
        role = sample_item_from_dictionary(market_role_distribution)
        return role

    def compute_personal_production(self, market_role_production_distribution_dict):
        """Based on market production rates for each role, sample this specific human's
        production rate based on o's role

        Args:
            market_role_production_distribution_dict (TODO): TODO

        Returns: TODO

        """
        personal_production = {}
        for item in market_role_production_distribution_dict[self.role]:
            personal_production[item] = market_role_production_distribution_dict[
                self.role
            ][item].sample()
        return personal_production

    def compute_personal_item_happiness_dict(self, market_item_happiness_distribution_dict):
        """Based on distribution of how happy each item makes humans, sample how happy each
        item makes this specific human

        Args:
            market_item_happiness_distribution_dict (TODO): TODO

        Returns: personal item happiness dictionary object

        """
        personal_item_happiness_dict = {}
        for item in market_item_happiness_distribution_dict:
            personal_item_happiness_dict[
                item
            ] = market_item_happiness_distribution_dict[item].sample()
        return personal_item_happiness_dict

    def compute_happiness(self, items=None):
        """compute happiness based on how many and the variety of items"""
        happiness = 0
        if items is None:
            items = self.items
        for item in items:
            happiness += (
                self.items[item] * self.personal_item_happiness_dict[item] ** 0.5
            )
        return happiness

    def produce_items(self):
        """produces a certain number of items based on the personal production
        rate

        Returns: TODO

        """
        if self.items == {}:
            self.items = self.personal_production
        else:
            for item in self.items:
                self.items[item] += self.personal_production[item]

    def generate_item_subsets(self):
        items = deepcopy(self.items)
        self.items_subsets = set()
        self._generate_item_subsets(items, self.items_subsets)

    def _generate_item_subsets(self, items, items_subsets):
        """given the human's posessions (items dictionary), generate all possible
        combinations of givable posessions (items) WITH QUANTITY that could be the
        LHS of a LimitTransaction

        Args:
            items (dict): dictionary (item_name: number). Make sure initial argument is
            DEEPCOPIED (since it will be modified otherwise)

        Returns (set[dict]): a set of all combinations of items possesed

        """
        if sum([count for count in items.values()]) == 0:
            return
        items_subsets.add(tuple(items.items()))

        for item in items:
            if items[item] > 0:
                items_cpy = deepcopy(items)
                items_cpy[item] -= 1
                if tuple(items_cpy.items()) not in items_subsets:
                    self._generate_item_subsets(items_cpy, items_subsets)
