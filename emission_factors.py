"""
Bangladesh-specific emission factors database for YourCarbonFootprint application.
Based on Bangladesh's energy mix, industrial practices, and local conditions.
"""

# Bangladesh-specific emission factors (in kgCO2e per unit)
BANGLADESH_EMISSION_FACTORS = {
    # Scope 1 - Direct emissions
    "Stationary Combustion": {
        "Natural Gas": {"factor": 0.18316, "unit": "kWh", "source": "IPCC 2006"},
        "Diesel": {"factor": 2.68787, "unit": "liter", "source": "IPCC 2006"},
        "Furnace Oil": {"factor": 3.15123, "unit": "liter", "source": "IPCC 2006"},
        "Coal": {"factor": 2.42287, "unit": "kg", "source": "IPCC 2006"},
        "Biomass (Wood)": {"factor": 0.0, "unit": "kg", "source": "IPCC 2006 - Carbon neutral"},
        "Jute Waste": {"factor": 0.0, "unit": "kg", "source": "Local biomass - Carbon neutral"},
        "Rice Husk": {"factor": 0.0, "unit": "kg", "source": "Agricultural waste - Carbon neutral"},
    },
    "Mobile Combustion": {
        "Petrol/Gasoline": {"factor": 2.31495, "unit": "liter", "source": "IPCC 2006"},
        "Diesel": {"factor": 2.70553, "unit": "liter", "source": "IPCC 2006"},
        "CNG": {"factor": 2.53721, "unit": "kg", "source": "IPCC 2006"},
        "LPG": {"factor": 1.55537, "unit": "liter", "source": "IPCC 2006"},
        "Kerosene": {"factor": 2.52348, "unit": "liter", "source": "IPCC 2006"},
    },
    "Process Emissions": {
        "Cement Production": {"factor": 0.82, "unit": "kg cement", "source": "Industry standard"},
        "Steel Production": {"factor": 2.58, "unit": "kg steel", "source": "Industry standard"},
        "Fertilizer Production": {"factor": 2.4, "unit": "kg fertilizer", "source": "Industry standard"},
        "Jute Processing": {"factor": 0.15, "unit": "kg jute fiber", "source": "Local estimate"},
        "Leather Tanning": {"factor": 4.2, "unit": "kg leather", "source": "Industry estimate"},
    },
    "Refrigerants": {
        "R-410A": {"factor": 2088.0, "unit": "kg", "source": "IPCC AR5"},
        "R-134a": {"factor": 1430.0, "unit": "kg", "source": "IPCC AR5"},
        "R-404A": {"factor": 3922.0, "unit": "kg", "source": "IPCC AR5"},
        "R-407C": {"factor": 1774.0, "unit": "kg", "source": "IPCC AR5"},
        "R-22": {"factor": 1810.0, "unit": "kg", "source": "IPCC AR5"},
    },
    
    # Scope 2 - Indirect emissions from purchased energy
    "Electricity": {
        "Bangladesh Grid": {"factor": 0.6815, "unit": "kWh", "source": "Bangladesh grid emission factor 2023"},
        "Solar Power": {"factor": 0.041, "unit": "kWh", "source": "IPCC LCA"},
        "Hydropower": {"factor": 0.024, "unit": "kWh", "source": "IPCC LCA"},
        "Wind Power": {"factor": 0.011, "unit": "kWh", "source": "IPCC LCA"},
        "Biomass Power": {"factor": 0.018, "unit": "kWh", "source": "IPCC LCA"},
    },
    "Steam": {
        "Purchased Steam (Natural Gas)": {"factor": 0.19, "unit": "kg steam", "source": "Industry standard"},
        "Purchased Steam (Biomass)": {"factor": 0.02, "unit": "kg steam", "source": "Industry standard"},
    },
    
    # Scope 3 - Other indirect emissions
    "Business Travel": {
        "Domestic Flight": {"factor": 0.15298, "unit": "passenger-km", "source": "DEFRA 2023"},
        "International Flight (Short-haul)": {"factor": 0.15298, "unit": "passenger-km", "source": "DEFRA 2023"},
        "International Flight (Long-haul)": {"factor": 0.19085, "unit": "passenger-km", "source": "DEFRA 2023"},
        "Train": {"factor": 0.03694, "unit": "passenger-km", "source": "DEFRA 2023"},
        "Bus": {"factor": 0.10471, "unit": "passenger-km", "source": "DEFRA 2023"},
        "Rickshaw (CNG)": {"factor": 0.08545, "unit": "km", "source": "Local estimate"},
        "Taxi": {"factor": 0.14549, "unit": "km", "source": "DEFRA 2023"},
        "Launch/Ferry": {"factor": 0.05234, "unit": "passenger-km", "source": "Local estimate"},
    },
    "Employee Commuting": {
        "Car (Petrol)": {"factor": 0.17336, "unit": "km", "source": "DEFRA 2023"},
        "Car (Diesel)": {"factor": 0.16844, "unit": "km", "source": "DEFRA 2023"},
        "Motorcycle": {"factor": 0.11501, "unit": "km", "source": "DEFRA 2023"},
        "Bus": {"factor": 0.10471, "unit": "passenger-km", "source": "DEFRA 2023"},
        "Rickshaw (CNG)": {"factor": 0.08545, "unit": "passenger-km", "source": "Local estimate"},
        "Rickshaw (Manual)": {"factor": 0.0, "unit": "passenger-km", "source": "Zero emission"},
        "Train": {"factor": 0.03694, "unit": "passenger-km", "source": "DEFRA 2023"},
        "Walking": {"factor": 0.0, "unit": "km", "source": "Zero emission"},
        "Bicycle": {"factor": 0.0, "unit": "km", "source": "Zero emission"},
    },
    "Freight Transportation": {
        "Truck (Diesel)": {"factor": 0.62068, "unit": "tonne-km", "source": "DEFRA 2023"},
        "Rail Freight": {"factor": 0.02683, "unit": "tonne-km", "source": "DEFRA 2023"},
        "Ship (Inland)": {"factor": 0.03147, "unit": "tonne-km", "source": "DEFRA 2023"},
        "Ship (International)": {"factor": 0.01185, "unit": "tonne-km", "source": "DEFRA 2023"},
        "Air Freight": {"factor": 1.02, "unit": "tonne-km", "source": "DEFRA 2023"},
    },
    "Waste Management": {
        "Landfill (Mixed Waste)": {"factor": 0.45727, "unit": "kg", "source": "DEFRA 2023"},
        "Landfill (Food Waste)": {"factor": 0.34, "unit": "kg", "source": "DEFRA 2023"},
        "Recycling (Mixed)": {"factor": 0.01042, "unit": "kg", "source": "DEFRA 2023"},
        "Composting": {"factor": 0.01042, "unit": "kg", "source": "DEFRA 2023"},
        "Incineration": {"factor": 0.01613, "unit": "kg", "source": "DEFRA 2023"},
        "Open Burning": {"factor": 2.3, "unit": "kg", "source": "Local estimate - discouraged"},
    },
    "Water and Wastewater": {
        "Water Supply": {"factor": 0.298, "unit": "cubic meter", "source": "Adjusted for Bangladesh"},
        "Water Treatment": {"factor": 0.615, "unit": "cubic meter", "source": "Adjusted for Bangladesh"},
        "Wastewater Treatment": {"factor": 0.708, "unit": "cubic meter", "source": "Industry standard"},
        "Septic Tank": {"factor": 0.15, "unit": "cubic meter", "source": "Local estimate"},
    },
    "Purchased Goods & Services": {
        # Bangladesh-specific products
        "Jute Fiber": {"factor": 0.82, "unit": "kg", "source": "Local LCA study"},
        "Jute Products": {"factor": 1.15, "unit": "kg", "source": "Local LCA study"},
        "Cotton (Raw)": {"factor": 3.8, "unit": "kg", "source": "Global average"},
        "Cotton Textiles": {"factor": 5.89, "unit": "kg", "source": "Industry study"},
        "Leather (Raw)": {"factor": 14.2, "unit": "kg", "source": "Industry study"},
        "Leather Products": {"factor": 17.0, "unit": "kg", "source": "Industry study"},
        "Pharmaceuticals": {"factor": 12.5, "unit": "kg", "source": "Industry estimate"},
        
        # Food products (major in Bangladesh)
        "Rice": {"factor": 2.7, "unit": "kg", "source": "FAO study"},
        "Fish (Freshwater)": {"factor": 5.4, "unit": "kg", "source": "FAO study"},
        "Fish (Marine)": {"factor": 3.1, "unit": "kg", "source": "FAO study"},
        "Shrimp (Farmed)": {"factor": 18.0, "unit": "kg", "source": "FAO study"},
        "Tea": {"factor": 2.5, "unit": "kg", "source": "Industry study"},
        "Sugar": {"factor": 1.8, "unit": "kg", "source": "Industry study"},
        
        # Construction materials
        "Cement": {"factor": 0.82, "unit": "kg", "source": "Industry standard"},
        "Steel (Primary)": {"factor": 2.58, "unit": "kg", "source": "Industry standard"},
        "Steel (Secondary)": {"factor": 0.89, "unit": "kg", "source": "Industry standard"},
        "Bricks (Clay)": {"factor": 0.22, "unit": "kg", "source": "Local estimate"},
        "Bamboo": {"factor": 0.02, "unit": "kg", "source": "Local estimate"},
        
        # General materials
        "Paper": {"factor": 0.919, "unit": "kg", "source": "DEFRA 2023"},
        "Plastic (General)": {"factor": 3.14, "unit": "kg", "source": "DEFRA 2023"},
        "Glass": {"factor": 0.85, "unit": "kg", "source": "DEFRA 2023"},
        "Aluminum": {"factor": 11.46, "unit": "kg", "source": "DEFRA 2023"},
        "Copper": {"factor": 4.94, "unit": "kg", "source": "DEFRA 2023"},
        
        # Office supplies
        "Office Paper (A4)": {"factor": 4.6, "unit": "kg", "source": "DEFRA 2023"},
        "Computers": {"factor": 300.0, "unit": "piece", "source": "Industry estimate"},
        "Mobile Phones": {"factor": 70.0, "unit": "piece", "source": "Industry estimate"},
    },
    "Hotel Stays": {
        "Hotel (Budget)": {"factor": 12.2, "unit": "night", "source": "DEFRA 2023"},
        "Hotel (Mid-range)": {"factor": 24.3, "unit": "night", "source": "DEFRA 2023"},
        "Hotel (Luxury)": {"factor": 65.2, "unit": "night", "source": "DEFRA 2023"},
        "Guesthouse": {"factor": 8.5, "unit": "night", "source": "Local estimate"},
    },
}

# Scope categories mapping
BANGLADESH_SCOPE_CATEGORIES = {
    "Scope 1": [
        "Stationary Combustion",
        "Mobile Combustion", 
        "Process Emissions",
        "Refrigerants",
        "Fugitive Emissions"
    ],
    "Scope 2": [
        "Electricity",
        "Steam",
        "District Cooling",
        "District Heating"
    ],
    "Scope 3": [
        "Business Travel",
        "Employee Commuting",
        "Freight Transportation",
        "Waste Management",
        "Water and Wastewater",
        "Purchased Goods & Services",
        "Hotel Stays",
        "Capital Goods",
        "Fuel and Energy-Related Activities",
        "Upstream Transportation & Distribution",
        "Downstream Transportation & Distribution",
        "Use of Sold Products",
        "End-of-Life Treatment of Sold Products",
        "Leased Assets",
        "Franchises",
        "Investments"
    ]
}

# Industry-specific emission benchmarks for Bangladesh (kgCO2e per unit)
BANGLADESH_INDUSTRY_BENCHMARKS = {
    "Ready Made Garments": {
        "per_piece_garment": 5.2,  # kgCO2e per garment
        "per_kg_fabric": 8.1,     # kgCO2e per kg fabric processed
        "electricity_intensity": 2.5,  # kWh per garment
    },
    "Textiles": {
        "per_kg_yarn": 12.5,      # kgCO2e per kg yarn
        "per_kg_fabric": 15.8,    # kgCO2e per kg fabric
        "per_meter_fabric": 0.95, # kgCO2e per meter fabric
    },
    "Jute Processing": {
        "per_kg_raw_jute": 0.82,  # kgCO2e per kg raw jute processed
        "per_kg_jute_product": 1.15,  # kgCO2e per kg finished product
    },
    "Leather": {
        "per_sq_ft": 2.8,         # kgCO2e per sq ft leather
        "per_kg_leather": 17.0,   # kgCO2e per kg leather
    },
    "Pharmaceuticals": {
        "per_kg_product": 12.5,   # kgCO2e per kg pharmaceutical
        "per_vial": 0.15,         # kgCO2e per vial/unit
    },
    "Steel": {
        "per_tonne": 2580,        # kgCO2e per tonne steel
    },
    "Cement": {
        "per_tonne": 820,         # kgCO2e per tonne cement
    },
    "Food Processing": {
        "per_kg_rice": 2.7,       # kgCO2e per kg rice processed
        "per_kg_fish": 5.4,       # kgCO2e per kg fish processed
    }
}

def get_emission_factor(category, activity):
    """
    Get the emission factor for a specific activity within a category.
    
    Args:
        category (str): The emission category
        activity (str): The specific activity
        
    Returns:
        dict: Dictionary containing factor, unit, and source, or None if not found
    """
    if category in BANGLADESH_EMISSION_FACTORS and activity in BANGLADESH_EMISSION_FACTORS[category]:
        return BANGLADESH_EMISSION_FACTORS[category][activity]
    return None

def get_activities(category):
    """
    Get all activities for a specific category.
    
    Args:
        category (str): The emission category
        
    Returns:
        list: List of activities for the category, or empty list if category not found
    """
    if category in BANGLADESH_EMISSION_FACTORS:
        return list(BANGLADESH_EMISSION_FACTORS[category].keys())
    return []

def get_categories(scope):
    """
    Get all categories for a specific scope.
    
    Args:
        scope (str): The scope (Scope 1, Scope 2, or Scope 3)
        
    Returns:
        list: List of categories for the scope, or empty list if scope not found
    """
    if scope in BANGLADESH_SCOPE_CATEGORIES:
        return BANGLADESH_SCOPE_CATEGORIES[scope]
    return []

def get_unit(category, activity):
    """
    Get the unit for a specific activity within a category.
    
    Args:
        category (str): The emission category
        activity (str): The specific activity
        
    Returns:
        str: Unit for the activity, or None if not found
    """
    ef = get_emission_factor(category, activity)
    if ef:
        return ef["unit"]
    return None

def get_industry_benchmark(industry, metric):
    """
    Get industry benchmark for Bangladesh industries.
    
    Args:
        industry (str): The industry sector
        metric (str): The specific metric
        
    Returns:
        float: Benchmark value, or None if not found
    """
    if industry in BANGLADESH_INDUSTRY_BENCHMARKS and metric in BANGLADESH_INDUSTRY_BENCHMARKS[industry]:
        return BANGLADESH_INDUSTRY_BENCHMARKS[industry][metric]
    return None

def get_all_industries():
    """
    Get all available industries with benchmarks.
    
    Returns:
        list: List of industry names
    """
    return list(BANGLADESH_INDUSTRY_BENCHMARKS.keys())

def search_emission_factors(search_term):
    """
    Search for emission factors containing the search term.
    
    Args:
        search_term (str): Term to search for
        
    Returns:
        dict: Dictionary of matching categories and activities
    """
    results = {}
    search_lower = search_term.lower()
    
    for category, activities in BANGLADESH_EMISSION_FACTORS.items():
        matching_activities = {}
        for activity, data in activities.items():
            if (search_lower in category.lower() or 
                search_lower in activity.lower()):
                matching_activities[activity] = data
        
        if matching_activities:
            results[category] = matching_activities
    
    return results

# Common emission factor recommendations for Bangladesh
BANGLADESH_RECOMMENDATIONS = {
    "electricity": {
        "factor": 0.6815,
        "unit": "kWh",
        "note": "Bangladesh national grid average (2023). Consider solar panels to reduce emissions."
    },
    "diesel_generator": {
        "factor": 2.68787,
        "unit": "liter",
        "note": "Common backup power during load shedding. Consider battery storage with solar."
    },
    "cng_transport": {
        "factor": 2.53721,
        "unit": "kg",
        "note": "Cleaner than petrol/diesel for Bangladesh urban transport."
    },
    "jute_products": {
        "factor": 1.15,
        "unit": "kg",
        "note": "Bangladesh's eco-friendly fiber with low carbon footprint."
    },
    "rmg_production": {
        "factor": 5.2,
        "unit": "piece",
        "note": "Ready-made garment production - major Bangladesh export sector."
    }
}

def get_recommendation(key):
    """
    Get emission factor recommendation for common Bangladesh activities.
    
    Args:
        key (str): Recommendation key
        
    Returns:
        dict: Recommendation data or None if not found
    """
    return BANGLADESH_RECOMMENDATIONS.get(key)

# Regional emission factors within Bangladesh
BANGLADESH_REGIONAL_FACTORS = {
    "Dhaka": {
        "electricity_peak_demand": 1.2,  # Multiplier during peak hours
        "transport_congestion": 1.15,     # Traffic congestion factor
        "waste_management": 0.9,          # Better waste management
    },
    "Chittagong": {
        "electricity_peak_demand": 1.1,
        "transport_congestion": 1.05,
        "industrial_density": 1.25,       # Higher industrial emissions
        "port_activities": 1.3,           # Port-related emissions
    },
    "Rajshahi": {
        "electricity_peak_demand": 1.0,
        "agricultural_intensity": 0.8,    # Lower industrial emissions
        "biomass_availability": 0.7,      # More biomass options
    },
    "Khulna": {
        "electricity_peak_demand": 1.05,
        "shrimp_farming": 1.4,           # Aquaculture emissions
        "mangrove_carbon": 0.6,          # Carbon sequestration potential
    },
    "Sylhet": {
        "electricity_peak_demand": 1.0,
        "tea_industry": 0.9,             # Lower emission intensity
        "gas_availability": 0.85,        # Better access to natural gas
    }
}

def get_regional_factor(region, factor_type):
    """
    Get regional adjustment factor for Bangladesh divisions.
    
    Args:
        region (str): Bangladesh division name
        factor_type (str): Type of regional factor
        
    Returns:
        float: Regional adjustment factor, 1.0 if not found
    """
    if region in BANGLADESH_REGIONAL_FACTORS and factor_type in BANGLADESH_REGIONAL_FACTORS[region]:
        return BANGLADESH_REGIONAL_FACTORS[region][factor_type]
    return 1.0

# Seasonal adjustment factors for Bangladesh
BANGLADESH_SEASONAL_FACTORS = {
    "monsoon": {
        "electricity_demand": 0.85,      # Lower AC usage during monsoon
        "transport_efficiency": 1.2,     # Flooding increases transport emissions
        "industrial_output": 0.9,        # Some industries reduce during monsoon
    },
    "winter": {
        "electricity_demand": 0.75,      # Lowest electricity demand
        "transport_efficiency": 1.0,     # Normal transport
        "industrial_output": 1.1,        # Peak production season
    },
    "summer": {
        "electricity_demand": 1.4,       # High AC demand
        "transport_efficiency": 1.0,     # Normal transport
        "industrial_output": 1.0,        # Normal production
    }
}

def get_seasonal_factor(season, factor_type):
    """
    Get seasonal adjustment factor for Bangladesh.
    
    Args:
        season (str): Season name (monsoon, winter, summer)
        factor_type (str): Type of seasonal factor
        
    Returns:
        float: Seasonal adjustment factor, 1.0 if not found
    """
    if season in BANGLADESH_SEASONAL_FACTORS and factor_type in BANGLADESH_SEASONAL_FACTORS[season]:
        return BANGLADESH_SEASONAL_FACTORS[season][factor_type]
    return 1.0

# Export market carbon requirements for Bangladesh exporters
EXPORT_MARKET_REQUIREMENTS = {
    "European Union": {
        "cbam_sectors": ["steel", "cement", "fertilizers", "aluminum", "electricity"],
        "cbam_start_date": "2026-01-01",
        "reporting_required": True,
        "verification_needed": True,
        "documentation": "EU CBAM certificates required"
    },
    "United States": {
        "sustainability_requirements": ["textiles", "apparel", "leather"],
        "voluntary_standards": ["HIGG", "BCI", "GOTS"],
        "reporting_required": False,
        "buyer_specific": True,
        "documentation": "Sustainability scorecards"
    },
    "Japan": {
        "voluntary_carbon_labeling": True,
        "green_finance": True,
        "reporting_required": False,
        "documentation": "Carbon footprint labels"
    },
    "United Kingdom": {
        "modern_slavery_act": True,
        "environmental_due_diligence": True,
        "reporting_required": False,
        "documentation": "Sustainability reports"
    }
}

def get_export_requirements(market):
    """
    Get carbon-related export requirements for specific markets.
    
    Args:
        market (str): Export market name
        
    Returns:
        dict: Market requirements or None if not found
    """
    return EXPORT_MARKET_REQUIREMENTS.get(market)