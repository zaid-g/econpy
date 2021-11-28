from probability import sample_item_from_dictionary
from uuid import uuid4
from misc_functions import deepcopy
from human import Human


class LimitTransaction:
    def __init__(self, items_give: dict, items_take: dict):
        self.items_give = items_give
        self.items_take = items_take


