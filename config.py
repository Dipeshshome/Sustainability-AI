"""
Configuration settings for YourCarbonFootprint Bangladesh application.
Tailored for Bangladesh's business environment and regulatory context.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application settings
APP_NAME = "YourCarbonFootprint Bangladesh"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "A comprehensive carbon accounting and reporting tool for Bangladesh SMEs and exporters"
APP_AUTHOR = "GxDx Solutions"
APP_CONTACT = "dipesh.cse@gmail.com"
APP_COUNTRY = "Bangladesh"
APP_CURRENCY = "BDT"

# API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Data settings
DATA_DIR = "data"
EMISSIONS_FILE = os.path.join(DATA_DIR, "emissions.json")
COMPANY_INFO_FILE = os.path.join(DATA_DIR, "company_info.json")

# Supported languages for Bangladesh
SUPPORTED_LANGUAGES = ["English", "Bengali"]

# Emission scopes
EMISSION_SCOPES = ["Scope 1", "Scope 2", "Scope 3"]

# Bangladesh-specific scope descriptions
SCOPE_DESCRIPTIONS = {
    "Scope 1": "Direct emissions from owned sources (generators, vehicles, boilers)",
    "Scope 2": "Indirect emissions from purchased electricity from Bangladesh grid",
    "Scope 3": "Value chain emissions (transport, materials, waste, business travel)"
}

# Bangladesh divisions
BANGLADESH_DIVISIONS = [
    "Dhaka",
    "Chittagong", 
    "Rajshahi",
    "Khulna",
    "Barisal",
    "Sylhet",
    "Rangpur",
    "Mymensingh"
]

# Major Bangladesh industries
BANGLADESH_INDUSTRIES = [
    "Ready Made Garments (RMG)",
    "Textiles",
    "Jute & Jute Products", 
    "Leather & Leather Goods",
    "Pharmaceuticals",
    "Steel & Engineering",
    "Cement",
    "Agriculture & Food Processing",
    "Fisheries & Aquaculture",
    "Information Technology",
    "Banking & Financial Services",
    "Chemicals & Fertilizers",
    "Ship Building",
    "Tea",
    "Ceramics",
    "Other"
]

# Bangladesh-specific units
BANGLADESH_UNITS = [
    "kWh",
    "MWh", 
    "liter",
    "kg",
    "tonne",
    "maund",  # Traditional Bengali unit
    "seer",   # Traditional Bengali unit
    "km",
    "passenger-km",
    "tonne-km",
    "cubic meter",
    "square meter",
    "piece",
    "dozen",
    "BDT",
    "USD",
    "hour",
    "day",
    "month"
]

# Major export markets for Bangladesh
EXPORT_MARKETS = [
    "European Union",
    "United States", 
    "Japan",
    "China",
    "India",
    "Canada",
    "Australia",
    "South Korea",
    "Russia",
    "Turkey",
    "Other"
]

# Regulatory frameworks affecting Bangladesh
REGULATORY_FRAMEWORKS = {
    "EU CBAM": {
        "full_name": "EU Carbon Border Adjustment Mechanism",
        "start_date": "2026-01-01",
        "affects": ["Steel", "Cement", "Fertilizers", "Aluminum", "Electricity"],
        "impact_on_bangladesh": "High - affects industrial exports"
    },
    "US Sustainability Requirements": {
        "full_name": "US Sustainability and ESG Requirements",
        "start_date": "Ongoing",
        "affects": ["Textiles", "Apparel", "Leather Goods"],
        "impact_on_bangladesh": "High - affects major export sectors"
    },
    "Japan Voluntary Carbon Labeling": {
        "full_name": "Japan Voluntary Carbon Footprint Labeling",
        "start_date": "Ongoing", 
        "affects": ["All products"],
        "impact_on_bangladesh": "Medium - voluntary but competitive advantage"
    },
    "Bangladesh NDC": {
        "full_name": "Bangladesh Nationally Determined Contributions",
        "start_date": "2021",
        "affects": ["All sectors"],
        "impact_on_bangladesh": "Medium - national commitments"
    },
    "Mujib Climate Prosperity Plan": {
        "full_name": "Mujib Climate Prosperity Plan",
        "start_date": "2021",
        "affects": ["All sectors"],
        "impact_on_bangladesh": "High - national climate strategy"
    }
}

# Bangladesh government agencies and support organizations
SUPPORT_ORGANIZATIONS = {
    "BSTI": {
        "full_name": "Bangladesh Standards and Testing Institution",
        "role": "Standards and certification",
        "contact": "www.bsti.gov.bd"
    },
    "BGMEA": {
        "full_name": "Bangladesh Garment Manufacturers and Exporters Association",
        "role": "RMG industry support",
        "contact": "www.bgmea.com.bd"
    },
    "BKMEA": {
        "full_name": "Bangladesh Knitwear Manufacturers and Exporters Association", 
        "role": "Knitwear industry support",
        "contact": "www.bkmea.com"
    },
    "EPB": {
        "full_name": "Export Promotion Bureau",
        "role": "Export facilitation",
        "contact": "www.epb.gov.bd"
    },
    "DIFE": {
        "full_name": "Department of Environment",
        "role": "Environmental regulation",
        "contact": "www.doe.gov.bd"
    },
    "IDCOL": {
        "full_name": "Infrastructure Development Company Limited",
        "role": "Green financing",
        "contact": "www.idcol.org"
    },
    "BIDA": {
        "full_name": "Bangladesh Investment Development Authority",
        "role": "Investment facilitation",
        "contact": "www.bida.gov.bd"
    }
}

# Common business challenges in Bangladesh relevant to carbon accounting
BANGLADESH_CHALLENGES = [
    "Frequent power outages requiring diesel backup",
    "Load shedding during peak hours",
    "Monsoon season disruptions",
    "Limited access to renewable energy",
    "High cost of energy-efficient equipment",
    "Limited availability of emission factors for local materials",
    "Complex export compliance requirements",
    "Limited technical expertise for carbon accounting",
    "Seasonal variations in production",
    "Infrastructure limitations for clean transport"
]

# Bangladesh-specific reporting periods
REPORTING_PERIODS = {
    "fiscal_year": "July 1 - June 30",
    "calendar_year": "January 1 - December 31",
    "export_season": "October - March (peak season)",
    "monsoon_impact": "June - September"
}

# Default data quality levels
DATA_QUALITY_LEVELS = {
    "High": {
        "description": "Measured/metered data with high accuracy",
        "examples": ["Smart meter readings", "Direct fuel measurements", "Verified invoices"],
        "confidence": 95
    },
    "Medium": {
        "description": "Calculated from bills/invoices",
        "examples": ["Electricity bills", "Fuel receipts", "Transport logs"],
        "confidence": 80
    },
    "Low": {
        "description": "Estimated or proxy data",
        "examples": ["Industry averages", "Estimates", "Incomplete records"],
        "confidence": 60
    }
}

# Verification status options
VERIFICATION_STATUS = [
    "Unverified",
    "Internally Verified", 
    "Third-Party Verified",
    "Audited"
]

# Common fuel types used in Bangladesh
BANGLADESH_FUELS = [
    "Natural Gas",
    "Diesel",
    "Furnace Oil",
    "Coal",
    "Biomass",
    "Jute Waste",
    "Rice Husk",
    "Petrol/Gasoline",
    "CNG",
    "LPG",
    "Kerosene"
]

# Transport modes common in Bangladesh
BANGLADESH_TRANSPORT = [
    "Car (Petrol)",
    "Car (Diesel)", 
    "Car (CNG)",
    "Motorcycle",
    "Bus",
    "Truck",
    "Rickshaw (CNG)",
    "Rickshaw (Manual)",
    "Train",
    "Launch/Ferry",
    "Bicycle",
    "Walking"
]

# Local carbon offset opportunities in Bangladesh
BANGLADESH_OFFSET_OPTIONS = {
    "Reforestation": {
        "types": ["Mangrove restoration", "Hill forest restoration", "Urban forestry"],
        "cost_range": "5-15 USD/tCO2e",
        "co_benefits": ["Biodiversity", "Flood protection", "Livelihood"]
    },
    "Renewable Energy": {
        "types": ["Solar installations", "Biogas plants", "Small hydro"],
        "cost_range": "8-20 USD/tCO2e", 
        "co_benefits": ["Energy access", "Job creation", "Energy security"]
    },
    "Energy Efficiency": {
        "types": ["Efficient cookstoves", "LED lighting", "Efficient motors"],
        "cost_range": "3-12 USD/tCO2e",
        "co_benefits": ["Cost savings", "Health benefits", "Productivity"]
    },
    "Agriculture": {
        "types": ["Improved rice cultivation", "Organic farming", "Agroforestry"],
        "cost_range": "6-18 USD/tCO2e",
        "co_benefits": ["Food security", "Soil health", "Rural income"]
    },
    "Waste Management": {
        "types": ["Waste-to-energy", "Composting", "Methane capture"],
        "cost_range": "4-16 USD/tCO2e", 
        "co_benefits": ["Waste reduction", "Sanitation", "Energy generation"]
    }
}

# Exchange rates (approximate - should be updated regularly)
EXCHANGE_RATES = {
    "USD_TO_BDT": 110.0,  # Approximate rate - update regularly
    "EUR_TO_BDT": 120.0,
    "GBP_TO_BDT": 135.0,
    "JPY_TO_BDT": 0.75
}

# Create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# Default company information template for Bangladesh
DEFAULT_COMPANY_INFO = {
    "name": "",
    "industry": "",
    "location": "",
    "division": "",
    "export_markets": [],
    "contact_person": "",
    "email": "",
    "phone": "",
    "address": "",
    "business_registration_number": "",
    "export_registration_number": "",
    "bida_registration": False,
    "etp_status": "Not Applicable",
    "annual_export_earnings_usd": 0,
    "employee_count": 0,
    "reporting_year": 2025,
    "fiscal_year_start": "July",
    "primary_export_products": [],
    "sustainability_certifications": [],
    "green_initiatives": []
}

# Sustainability certifications common in Bangladesh
SUSTAINABILITY_CERTIFICATIONS = [
    "LEED (Green Building)",
    "HIGG Index (Apparel)",
    "BCI (Better Cotton Initiative)", 
    "GOTS (Global Organic Textile Standard)",
    "OEKO-TEX",
    "FSC (Forest Stewardship Council)",
    "Rainforest Alliance",
    "Fairtrade",
    "ISO 14001 (Environmental Management)",
    "ISO 50001 (Energy Management)",
    "None"
]

# Common green initiatives in Bangladesh
GREEN_INITIATIVES = [
    "Solar panel installation",
    "Energy-efficient lighting (LED)",
    "Rainwater harvesting",
    "Waste segregation and recycling",
    "Energy-efficient motors",
    "Green building design",
    "Tree plantation",
    "Water conservation",
    "Sustainable packaging",
    "Green transportation",
    "None"
]

def get_exchange_rate(from_currency, to_currency="BDT"):
    """
    Get exchange rate for currency conversion.
    
    Args:
        from_currency (str): Source currency
        to_currency (str): Target currency (default: BDT)
        
    Returns:
        float: Exchange rate or 1.0 if not found
    """
    rate_key = f"{from_currency}_TO_{to_currency}"
    return EXCHANGE_RATES.get(rate_key, 1.0)

def convert_currency(amount, from_currency, to_currency="BDT"):
    """
    Convert amount from one currency to another.
    
    Args:
        amount (float): Amount to convert
        from_currency (str): Source currency
        to_currency (str): Target currency (default: BDT)
        
    Returns:
        float: Converted amount
    """
    if from_currency == to_currency:
        return amount
    
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate