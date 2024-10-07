from crops.code_enums import VeryLowDroughtRisk, LowDroughtRisk, MediumDroughtRisk, HighDroughtRisk, VeryHighDroughtRisk

very_low_drought_risk = {enum_member.value for enum_member in VeryLowDroughtRisk}
low_drought_risk = {enum_member.value for enum_member in LowDroughtRisk}
medium_drought_risk = {enum_member.value for enum_member in MediumDroughtRisk}
high_drought_risk = {enum_member.value for enum_member in HighDroughtRisk}
very_high_drought_risk = {enum_member.value for enum_member in VeryHighDroughtRisk}

all_plants = very_low_drought_risk | \
             low_drought_risk | \
             medium_drought_risk | \
             high_drought_risk | \
             very_high_drought_risk