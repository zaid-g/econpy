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

MARKET_ITEM_HAPPINESS_DISTRUBUTION_DICT = {
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

MARKET_ROLE_DISTRIBUTION = {"farmer": 0.3, "herder": 0.3, "manufacturer": 0.4}

MARKET_ROLE_PRODUCTION_DISTRIBUTION_DICT = {
    "farmer": {"apple": Poisson(6), "oil": Poisson(6.5)},
    "herder": {"horse": Poisson(5), "cow": Poisson(4.5), "sheep": Poisson(6)},
    "manufacturer": {
        "shovel": Poisson(7),
        "wood": Poisson(7.3),
        "candle": Poisson(8),
        "coat": Poisson(4),
    },
}

NUM_HUMANS = 10

market = Market(
    NUM_HUMANS,
    MARKET_ROLE_DISTRIBUTION,
    MARKET_ROLE_PRODUCTION_DISTRIBUTION_DICT,
    MARKET_ITEM_HAPPINESS_DISTRUBUTION_DICT,
)

for human in market.humans:
    human.generate_item_subsets()
