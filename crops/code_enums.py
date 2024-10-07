from enum import Enum

# Define Enums for drought risk categories
class DroughtRisk(Enum):
    VERY_LOW = 'Very Low'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    VERY_HIGH = 'Very High'


class VeryLowDroughtRisk(Enum):
    CACTUS = 'Cactus'
    CASSAVA = 'Cassava'
    SWEET_POTATO = 'Sweet Potato'
    WATERCRESS = 'Watercress'
    CABBAGE = 'Cabbage'
    LETTUCE = 'Lettuce'


class LowDroughtRisk(Enum):
    MILLET = 'Millet'
    SORGHUM = 'Sorghum'
    PEANUT = 'Peanut'
    CHICKPEA = 'Chickpea'
    PIGEON_PEA = 'Pigeon Pea'
    QUINOA = 'Quinoa'
    TEFF = 'Teff'
    FENNEL = 'Fennel'
    KALE = 'Kale'


class MediumDroughtRisk(Enum):
    TOMATO = 'Tomato'
    CORN = 'Corn'
    CUCUMBER = 'Cucumber'
    SPINACH = 'Spinach'
    ZUCCHINI = 'Zucchini'
    PUMPKIN = 'Pumpkin'
    BARLEY = 'Barley'
    OATS = 'Oats'
    LENTILS = 'Lentils'
    EGGPLANT = 'Eggplant'


class HighDroughtRisk(Enum):
    WHEAT = 'Wheat'
    RICE = 'Rice'
    POTATO = 'Potato'
    SUGARCANE = 'Sugarcane'
    BROCCOLI = 'Broccoli'
    ONION = 'Onion'
    RED_ONION = 'Red Onion'
    BELL_PEPPER = 'Bell Pepper'
    CARROT = 'Carrot'
    RADISH = 'Radish'


class VeryHighDroughtRisk(Enum):
    BANANA = 'Banana'
    PAPAYA = 'Papaya'
    COCOA = 'Cocoa'
    GRAPE = 'Grape'
    ORANGE = 'Orange'
    COTTON = 'Cotton'
    SWEET_CORN = 'Sweet Corn'
    POPCORN = 'Popcorn'
    SOYBEAN = 'Soybean'


class PlantingPeriod(Enum):
    BEFORE = "Before planting period"
    DURING = "During planting period"
    AFTER = "After planting period"
