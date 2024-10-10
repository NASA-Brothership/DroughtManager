from enum import Enum

# Define Enums for drought risk categories
class DroughtRisk(Enum):
    VERY_LOW = 'Very Low'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    VERY_HIGH = 'Very High'


class DroughtRiskValue(Enum):
    VERY_LOW = 0
    LOW = 0.25
    MEDIUM = 0.5
    HIGH = 0.75
    VERY_HIGH = 1


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
    BEFORE = "Before"
    DURING = "During"
    AFTER = "After"


class Recommendation(Enum):
    VERY_LOW_RISK_WITH_CROPS = (
        "Very low risk. Favorable conditions, with no signs of imminent water stress. "
        "The likelihood of drought affecting production is minimal. Suggested action: Continue with standard agricultural management.; "
        "Routinely monitor soil moisture and plant conditions; however, no significant changes are required.; "
        "Use conservation practices, such as soil cover, to ensure moisture retention."
    )
    
    LOW_RISK_WITH_CROPS = (
        "Low risk. Although the risk is low, taking light preventive measures can help avoid increased water stress if weather conditions change unexpectedly. "
        "Suggested action: Continue monitoring soil and plant health, with a focus on the crop growth stage.; "
        "Check the efficiency of the irrigation system and make preventive adjustments if necessary.; "
        "Implement water retention practices in the soil, such as mulching or soil preparation that minimizes moisture loss."
    )
    
    MEDIUM_RISK_WITH_CROPS_WITH_IRRIGATION = (
        "Medium risk. There is a considerable risk of water stress, which justifies more direct interventions to prevent productivity losses. "
        "Suggested action: Adjust the irrigation plan, ensuring that water is applied efficiently, especially in the most critical areas of the field.; "
        "In addition to the irrigation system, consider alternative strategies such as supplemental sprinkler or drip irrigation.; "
        "Evaluate the use of biostimulants that help plants cope better with water stress.; "
        "Encourage the use of soil cover to reduce evaporation and improve moisture retention."
    )
    
    MEDIUM_RISK_WITH_CROPS_WITHOUT_IRRIGATION = (
        "Medium risk. The suggested actions primarily aim to conserve soil moisture and minimize evapotranspiration, "
        "as the plants may be starting to experience water stress, but there is still room to prevent severe damage. "
        "Water retention through soil cover and the use of cover crops helps extend moisture availability, while careful management of weeding prevents the soil from drying out more quickly. "
        "Suggested action: Use of Soil Cover (Mulching), apply straw, crop residues, or vegetative cover on the soil around plants to reduce water evaporation. "
        "This can also help maintain lower soil temperatures and reduce competition from weeds for water.; Selective Weeding, avoid excessive removal of weeds that may serve as natural cover, "
        "but eliminate those that directly compete with the crop for water. Selective weeding can help conserve soil moisture.; "
        "Increase the Density of Cover Crops, using fast-growing cover crops between the rows of the main crop can help conserve soil moisture while also improving soil quality in the medium term.; "
        "Use of Water Retaining Additives (Polymers), if available, apply water-retaining polymers to the soil, which can increase the soil's capacity to store water for plants during periods of water stress."
    )
    
    HIGH_RISK_WITH_CROPS_WITH_IRRIGATION = (
        "High risk. The situation of water deficit is imminent, and more intensive actions are necessary to prevent severe losses. "
        "Suggested Action: Apply immediate irrigation in the most critical areas, prioritizing the use of efficient systems, such as drip irrigation, to minimize water waste.; "
        "If possible, adjust the management calendar by advancing harvests in perennial crops or modifying fertilization to help plants cope with water stress."
    )
    
    HIGH_RISK_WITH_CROPS_WITHOUT_IRRIGATION = (
        "High risk. At this level, water stress is a real threat, and the actions aim to concentrate the limited water resources on the most important plants. "
        "Thinning reduces competition for water, while management adjustments, such as early harvesting, help prevent significant losses. "
        "Containment barriers and strategic weeding minimize evaporation and water runoff. Suggested Actions: Thinning (Plant Reducing), "
        "reduce plant density by removing some of them to decrease competition for water. This may be a drastic measure, but in high-risk conditions, "
        "it can help the remaining plants survive with the limited available water.; Strategic Weeding, avoid intensive soil disturbance during weeding, "
        "as this can expose the soil to more sunlight and increase evaporation. Perform weeding only where absolutely necessary.; Soil and Water Conservation, "
        "create barriers or containment furrows to hold as much water as possible that may still be in the soil or that may be received from light rainfall, preventing surface runoff.; "
        "Reduced Fertilization, decrease the amount of nitrogen fertilization or suspend the use of fertilizers that may require more soil water for plant assimilation, as this can increase water stress.; "
        "Adjustment of Management Calendar, if possible, advance the harvest or pruning of perennial crops to reduce water demand during critical phases, "
        "especially when the plants are already in advanced stages of growth."
    )
    
    VERY_HIGH_RISK_WITH_CROPS_WITH_IRRIGATION = (
        "Very high risk. The likelihood of significant losses is very high, necessitating swift and decisive responses to minimize the impact of drought on crops. "
        "Suggested Action: Implement emergency irrigation, prioritizing areas and crops of higher economic value or those more sensitive to water scarcity.; "
        "Reduce plant density in critical cases, if possible, to decrease competition for water resources.; Immediately adjust any operations that consume or expose the soil to additional water losses, "
        "such as frequent weeding or unplanned fertilization.; If feasible, consider implementing contingency strategies, such as adopting drought management techniques (e.g., pruning or thinning plants to reduce water demand)."
    )
    
    VERY_HIGH_RISK_WITH_CROPS_WITHOUT_IRRIGATION = (
        "Very high risk. In situations of very high risk, the primary goal is to save as much production as possible with extremely limited resources. "
        "Sacrificing part of the crop and emergency pruning reduce water demand, while the application of organic matter to the soil retains the little remaining moisture. "
        "These measures, although drastic, are necessary to ensure that at least part of the crop survives or is harvested before total collapse. Suggested Actions: "
        "Sacrifice Part of the Crop, in extreme cases, the producer may need to choose to sacrifice part of the crop to concentrate resources (available water in the soil and nutrients) in the more productive areas. "
        "This can help save part of the production.; Pruning or Early Cutting, for perennial crops, such as fruit trees, emergency pruning may be an option. "
        "This reduces leaf area and, consequently, water demand, helping the plant survive until conditions improve.; Reduction in Input Use, suspend the application of inputs that may increase the water demand of plants, "
        "such as nitrogen fertilizers, and reduce any practices that involve intensive crop management.; Application of Organic Materials to the Soil, spreading organic compost, manure, or other plant residues "
        "can help improve the soil's ability to retain the little available moisture, in addition to providing nutrients that can help plants cope with water stress.; "
        "Alter Harvesting Scheme, in cases of very high risk, it is essential to adjust the harvest to minimize losses. Harvesting crops that are close to maturity early can prevent total losses."
    )
