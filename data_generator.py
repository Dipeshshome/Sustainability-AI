"""
Sample data generator for YourCarbonFootprint Bangladesh application.
Creates realistic sample data based on common Bangladesh business scenarios.
"""

import pandas as pd
import json
from datetime import datetime, timedelta
import random
from pathlib import Path

def generate_bangladesh_sample_data():
    """
    Generate comprehensive sample data for Bangladesh businesses.
    Returns sample emissions data and company information.
    """
    
    # Sample company profiles for different Bangladesh industries
    sample_companies = {
        "rmg_exporter": {
            "name": "Dhaka Garments Ltd.",
            "industry": "Ready Made Garments (RMG)",
            "division": "Dhaka",
            "export_markets": ["European Union", "United States", "Canada"],
            "employee_count": 2500,
            "annual_export_earnings_usd": 15000000,
            "bida_registration": True,
            "etp_status": "Operational"
        },
        "textile_mill": {
            "name": "Chittagong Textile Mills",
            "industry": "Textiles", 
            "division": "Chittagong",
            "export_markets": ["Japan", "European Union", "Australia"],
            "employee_count": 1200,
            "annual_export_earnings_usd": 8000000,
            "bida_registration": True,
            "etp_status": "Operational"
        },
        "jute_processor": {
            "name": "Bangladesh Jute Industries",
            "industry": "Jute & Jute Products",
            "division": "Khulna",
            "export_markets": ["European Union", "India", "United States"],
            "employee_count": 800,
            "annual_export_earnings_usd": 3000000,
            "bida_registration": True,
            "etp_status": "Under Construction"
        },
        "pharmaceutical": {
            "name": "Pharma Solutions Bangladesh",
            "industry": "Pharmaceuticals",
            "division": "Dhaka",
            "export_markets": ["United States", "European Union", "Other"],
            "employee_count": 500,
            "annual_export_earnings_usd": 12000000,
            "bida_registration": True,
            "etp_status": "Operational"
        }
    }
    
    # Generate sample emissions data
    sample_emissions = []
    
    # Base date for sample data (last 12 months)
    base_date = datetime.now() - timedelta(days=365)
    
    # RMG Factory Sample Data
    rmg_activities = [
        # Scope 1 - Direct emissions
        {"scope": "Scope 1", "category": "Stationary Combustion", "activity": "Diesel Generator", 
         "quantity_range": (800, 1200), "unit": "liter", "factor": 2.68787, "frequency": "monthly"},
        {"scope": "Scope 1", "category": "Mobile Combustion", "activity": "Company Vehicle", 
         "quantity_range": (200, 300), "unit": "liter", "factor": 2.31495, "frequency": "monthly"},
        {"scope": "Scope 1", "category": "Refrigerants", "activity": "AC System", 
         "quantity_range": (2, 5), "unit": "kg", "factor": 1430.0, "frequency": "quarterly"},
        
        # Scope 2 - Electricity 
        {"scope": "Scope 2", "category": "Electricity", "activity": "Bangladesh Grid", 
         "quantity_range": (45000, 55000), "unit": "kWh", "factor": 0.6815, "frequency": "monthly"},
        
        # Scope 3 - Other indirect
        {"scope": "Scope 3", "category": "Business Travel", "activity": "Domestic Flight", 
         "quantity_range": (2000, 4000), "unit": "passenger-km", "factor": 0.15298, "frequency": "monthly"},
        {"scope": "Scope 3", "category": "Employee Commuting", "activity": "Bus", 
         "quantity_range": (15000, 20000), "unit": "passenger-km", "factor": 0.10471, "frequency": "monthly"},
        {"scope": "Scope 3", "category": "Waste Management", "activity": "Landfill (Mixed Waste)", 
         "quantity_range": (1500, 2000), "unit": "kg", "factor": 0.45727, "frequency": "monthly"},
        {"scope": "Scope 3", "category": "Purchased Goods & Services", "activity": "Cotton Textiles", 
         "quantity_range": (8000, 12000), "unit": "kg", "factor": 5.89, "frequency": "monthly"},
        {"scope": "Scope 3", "category": "Water and Wastewater", "activity": "Water Supply", 
         "quantity_range": (800, 1200), "unit": "cubic meter", "factor": 0.298, "frequency": "monthly"}
    ]
    
    # Textile Mill Sample Data
    textile_activities = [
        # Scope 1
        {"scope": "Scope 1", "category": "Stationary Combustion", "activity": "Natural Gas", 
         "quantity_range": (15000, 20000), "unit": "kWh", "factor": 0.18316, "frequency": "monthly"},
        {"scope": "Scope 1", "category": "Stationary Combustion", "activity": "Diesel Generator", 
         "quantity_range": (400, 600), "unit": "liter", "factor": 2.68787, "frequency": "monthly"},
        
        # Scope 2
        {"scope": "Scope 2", "category": "Electricity", "activity": "Bangladesh Grid", 
         "quantity_range": (35000, 45000), "unit": "kWh", "factor": 0.6815, "frequency": "monthly"},
        
        # Scope 3
        {"scope": "Scope 3", "category": "Purchased Goods & Services", "activity": "Cotton (Raw)", 
         "quantity_range": (5000, 8000), "unit": "kg", "factor": 3.8, "frequency": "monthly"},
        {"scope": "Scope 3", "category": "Freight Transportation", "activity": "Truck (Diesel)", 
         "quantity_range": (2000, 3000), "unit": "tonne-km", "factor": 0.62068, "frequency": "monthly"}
    ]
    
    # Jute Processing Sample Data
    jute_activities = [
        # Scope 1
        {"scope": "Scope 1", "category": "Stationary Combustion", "activity": "Biomass", 
         "quantity_range": (2000, 3000), "unit": "kg", "factor": 0.0, "frequency": "monthly"},
        {"scope": "Scope 1", "category": "Stationary Combustion", "activity": "Diesel Generator", 
         "quantity_range": (200, 400), "unit": "liter", "factor": 2.68787, "frequency": "monthly"},
        
        # Scope 2
        {"scope": "Scope 2", "category": "Electricity", "activity": "Bangladesh Grid", 
         "quantity_range": (8000, 12000), "unit": "kWh", "factor": 0.6815, "frequency": "monthly"},
        
        # Scope 3
        {"scope": "Scope 3", "category": "Purchased Goods & Services", "activity": "Jute Fiber", 
         "quantity_range": (10000, 15000), "unit": "kg", "factor": 0.82, "frequency": "monthly"}
    ]
    
    # Pharmaceutical Sample Data
    pharma_activities = [
        # Scope 1
        {"scope": "Scope 1", "category": "Stationary Combustion", "activity": "Natural Gas", 
         "quantity_range": (8000, 12000), "unit": "kWh", "factor": 0.18316, "frequency": "monthly"},
        
        # Scope 2
        {"scope": "Scope 2", "category": "Electricity", "activity": "Bangladesh Grid", 
         "quantity_range": (25000, 35000), "unit": "kWh", "factor": 0.6815, "frequency": "monthly"},
        
        # Scope 3
        {"scope": "Scope 3", "category": "Purchased Goods & Services", "activity": "Pharmaceuticals", 
         "quantity_range": (500, 800), "unit": "kg", "factor": 12.5, "frequency": "monthly"}
    ]
    
    # Company and activity mapping
    company_activities = {
        "Dhaka Garments Ltd.": rmg_activities,
        "Chittagong Textile Mills": textile_activities,
        "Bangladesh Jute Industries": jute_activities,
        "Pharma Solutions Bangladesh": pharma_activities
    }
    
    # Generate 12 months of data for each company
    for company_name, activities in company_activities.items():
        company_info = next(comp for comp in sample_companies.values() if comp["name"] == company_name)
        
        for month in range(12):
            current_date = base_date + timedelta(days=30 * month)
            
            # Seasonal adjustments for Bangladesh
            season = get_bangladesh_season(current_date.month)
            seasonal_multiplier = get_seasonal_multiplier(season)
            
            for activity in activities:
                # Generate entry based on frequency
                if activity["frequency"] == "monthly" or \
                   (activity["frequency"] == "quarterly" and month % 3 == 0):
                    
                    quantity = random.uniform(*activity["quantity_range"]) * seasonal_multiplier
                    emissions = quantity * activity["factor"]
                    
                    # Add some business context
                    business_unit = get_business_unit(company_info["industry"])
                    project = get_project_type(activity["scope"])
                    facility = f"{company_info['division']} {get_facility_type(company_info['industry'])}"
                    
                    sample_emissions.append({
                        "date": current_date.strftime("%Y-%m-%d"),
                        "business_unit": business_unit,
                        "project": project,
                        "scope": activity["scope"],
                        "category": activity["category"], 
                        "activity": activity["activity"],
                        "country": "Bangladesh",
                        "facility": facility,
                        "responsible_person": get_responsible_person(business_unit),
                        "quantity": round(quantity, 2),
                        "unit": activity["unit"],
                        "emission_factor": activity["factor"],
                        "emissions_kgCO2e": round(emissions, 2),
                        "data_quality": get_data_quality(),
                        "verification_status": get_verification_status(),
                        "notes": get_sample_notes(activity, company_info["industry"])
                    })
    
    return sample_emissions, sample_companies

def get_bangladesh_season(month):
    """Get Bangladesh season based on month."""
    if month in [6, 7, 8, 9]:  # June to September
        return "monsoon"
    elif month in [12, 1, 2]:  # December to February
        return "winter"
    else:
        return "summer"

def get_seasonal_multiplier(season):
    """Get seasonal adjustment multiplier for Bangladesh."""
    multipliers = {
        "monsoon": 0.9,   # Reduced activity during monsoon
        "winter": 1.1,    # Peak production season
        "summer": 1.0     # Normal activity
    }
    return multipliers.get(season, 1.0)

def get_business_unit(industry):
    """Get appropriate business unit based on industry."""
    units = {
        "Ready Made Garments (RMG)": random.choice(["Production", "Cutting", "Sewing", "Finishing"]),
        "Textiles": random.choice(["Spinning", "Weaving", "Dyeing", "Finishing"]),
        "Jute & Jute Products": random.choice(["Processing", "Spinning", "Weaving"]),
        "Pharmaceuticals": random.choice(["Manufacturing", "R&D", "Quality Control"])
    }
    return units.get(industry, "Corporate")

def get_project_type(scope):
    """Get project type based on emission scope."""
    projects = {
        "Scope 1": random.choice(["Energy Efficiency", "Fuel Switching", "Operational"]),
        "Scope 2": random.choice(["Renewable Energy", "Energy Efficiency", "Grid Improvement"]),
        "Scope 3": random.choice(["Supply Chain", "Waste Reduction", "Transport Optimization"])
    }
    return projects.get(scope, "Not Applicable")

def get_facility_type(industry):
    """Get facility type based on industry."""
    facilities = {
        "Ready Made Garments (RMG)": "Garment Factory",
        "Textiles": "Textile Mill",
        "Jute & Jute Products": "Processing Plant",
        "Pharmaceuticals": "Manufacturing Facility"
    }
    return facilities.get(industry, "Facility")

def get_responsible_person(business_unit):
    """Get sample responsible person names."""
    bangladeshi_names = [
        "Rahman Ahmed", "Fatima Khan", "Abdul Karim", "Rashida Begum",
        "Mohammad Ali", "Nasreen Akter", "Aminul Islam", "Salma Khatun",
        "Rafiqul Hasan", "Ruma Parvin", "Shahidul Islam", "Rehana Begum"
    ]
    return random.choice(bangladeshi_names)

def get_data_quality():
    """Get random data quality level."""
    return random.choice(["High", "Medium", "Low"])

def get_verification_status():
    """Get random verification status."""
    return random.choice(["Unverified", "Internally Verified", "Third-Party Verified"])

def get_sample_notes(activity, industry):
    """Generate contextual notes based on activity and industry."""
    notes_templates = {
        "Diesel Generator": f"Backup power during load shedding - common in {industry}",
        "Bangladesh Grid": "Monthly electricity consumption from national grid",
        "Company Vehicle": "Fleet vehicle fuel consumption for business operations",
        "AC System": "Refrigerant top-up for factory air conditioning",
        "Cotton Textiles": "Raw material procurement for production",
        "Jute Fiber": "Local jute fiber for eco-friendly product manufacturing",
        "Natural Gas": "Industrial heating and steam generation",
        "Business Travel": "Executive travel for export market development",
        "Employee Commuting": "Daily staff transportation to factory",
        "Waste Management": "Industrial waste disposal and treatment"
    }
    
    activity_name = activity["activity"]
    return notes_templates.get(activity_name, f"Regular {activity_name} consumption for {industry} operations")

def save_sample_data(emissions_data, company_data, output_dir="sample_data"):
    """Save sample data to files."""
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Save emissions data as JSON
    with open(f"{output_dir}/sample_emissions.json", "w") as f:
        json.dump(emissions_data, f, indent=2)
    
    # Save emissions data as CSV
    df = pd.DataFrame(emissions_data)
    df.to_csv(f"{output_dir}/sample_emissions.csv", index=False)
    
    # Save company data
    with open(f"{output_dir}/sample_companies.json", "w") as f:
        json.dump(company_data, f, indent=2)
    
    # Create separate CSV files for each company
    df = pd.DataFrame(emissions_data)
    for company_name in df['facility'].str.split().str[0].unique():
        company_df = df[df['facility'].str.contains(company_name)]
        company_df.to_csv(f"{output_dir}/sample_{company_name.lower()}_emissions.csv", index=False)
    
    print(f"Sample data saved to {output_dir}/ directory")
    print(f"Generated {len(emissions_data)} emission entries")
    print(f"Companies: {len(company_data)}")

if __name__ == "__main__":
    # Generate sample data
    emissions, companies = generate_bangladesh_sample_data()
    
    # Save to files
    save_sample_data(emissions, companies)
    
    # Print summary
    df = pd.DataFrame(emissions)
    print("\n=== Sample Data Summary ===")
    print(f"Total Emissions: {df['emissions_kgCO2e'].sum():.2f} kgCO2e")
    print(f"By Scope:")
    print(df.groupby('scope')['emissions_kgCO2e'].sum())
    print(f"\nBy Industry (Facility):")
    facility_summary = df.groupby(df['facility'].str.split().str[0])['emissions_kgCO2e'].sum()
    print(facility_summary)
    print(f"\nData Quality Distribution:")
    print(df['data_quality'].value_counts())