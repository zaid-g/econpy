from probability import sample_item_from_dictionary
from misc_functions import deepcopy


class Human:
    def __init__(
        self, uid, role_distribution, world_role_production, world_item_happiness
    ):
        self.uid = uid
        self.assign_role_and_initialize_items(role_distribution, world_role_production)
        self.compute_personal_item_happiness(world_item_happiness)
        self.compute_happiness()  # self.happiness computed

    def compute_personal_item_happiness(self, world_item_happiness):
        """call once when initializing object"""
        self.personal_item_happiness = {}
        for item in world_item_happiness:
            self.personal_item_happiness[item] = world_item_happiness[item].sample()

    def compute_happiness(self):
        """compute happiness based on how many and the variety of items
        the human has

        """
        self.happiness = 0
        for item in self.items:
            self.happiness += (
                self.items[item] * self.personal_item_happiness[item] ** 0.5
            )

    def assign_role_and_initialize_items(
        self, role_distribution, world_role_production
    ):
        """assigns a role to the human and, based on the world production
        rate (and role), initializes (by sampling), how many of each item o has.

        Args:
            role_distribution (dict): TODO
            world_role_production (TODO): TODO

        Returns: TODO

        """
        self.role = sample_item_from_dictionary(role_distribution)
        self.items = {
            item: world_role_production[self.role][item].sample_discrete()
            for item in world_role_production[self.role]
        }

    def project_happiness(self, items: dict):
        """compute happiness that would result from having dictionary of items

        Args:
            items (dict): dictionary (item_name: number)

        Returns: TODO

        """
        happiness = 0
        print("computed ")
        for item in items:
            happiness += items[item] * self.personal_item_happiness[item] ** 0.5
        return happiness

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


class LimitTransaction:
    def __init__(self, items_give: dict, items_take: dict):
        self.items_give = items_give
        self.items_take = items_take


class Market:
    def __init__(self, humans):
        self.humans = humans
        self.compute_happiness()  # self.happiness computed

    def get_number_of_humans(self):
        return len(self.humans)

    def compute_happiness(self):
        """for each human in market, add the happiness"""
        self.happiness = 0
        for human in self.humans:
            human.compute_happiness()
            self.happiness += human.happiness

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
        other_humans = [
            human for human in self.humans if human != human
        ]


        import ipdb; ipdb.set_trace()
