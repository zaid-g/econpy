from pprint import pprint as pp
from uuid import uuid4
from classes import Human, LimitTransaction, Market
from probability import Poisson


SET_OF_ALL_ITEMS = {
    "apple",
    "horse",
    "shovel",
    "wood",
    "oil",
    "candle",
    "coat",
    "cow",
    "sheep",
}

WORLD_ITEM_HAPPINESS = {
    "apple": Poisson(6),
    "horse": Poisson(10),
    "shovel": Poisson(8),
    "wood": Poisson(7),
    "oil": Poisson(6.5),
    "candle": Poisson(3),
    "coat": Poisson(8),
    "cow": Poisson(9),
    "sheep": Poisson(10),
}

ROLE_DISTRIBUTION = {"farmer": 0.3, "herder": 0.3, "manufacturer": 0.4}

WORLD_ROLE_PRODUCTION = {
    "farmer": {"apple": Poisson(6), "oil": Poisson(6.5)},
    "herder": {"horse": Poisson(5), "cow": Poisson(4.5), "sheep": Poisson(6)},
    "manufacturer": {
        "shovel": Poisson(7),
        "wood": Poisson(7.3),
        "candle": Poisson(8),
        "coat": Poisson(4),
    },
}

market = Market(
    humans=[
        Human(id_, ROLE_DISTRIBUTION, WORLD_ROLE_PRODUCTION, WORLD_ITEM_HAPPINESS)
        for id_ in [uuid4() for i in range(10)]
    ]
)

for human in market.humans:
    human.generate_item_subsets()

import ipdb; ipdb.set_trace()
