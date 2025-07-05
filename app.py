import streamlit as st
import pandas as pd
import os
import json
import shutil
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
import base64
from io import BytesIO

# Load environment variables
load_dotenv()

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Set page config for wide layout
st.set_page_config(page_title="YourCarbonFootprint Bangladesh", page_icon="🇧🇩", layout="wide")

# Initialize session state variables if they don't exist
if 'language' not in st.session_state:
    st.session_state.language = 'English'
if 'emissions_data' not in st.session_state:
    # Load data if exists, otherwise create empty dataframe
    if os.path.exists('data/emissions.json'):
        try:
            with open('data/emissions.json', 'r') as f:
                data = f.read().strip()
                if data:  # Check if file is not empty
                    try:
                        st.session_state.emissions_data = pd.DataFrame(json.loads(data))
                    except json.JSONDecodeError:
                        # Create a backup of the corrupted file
                        backup_file = f'data/emissions_backup_{int(time.time())}.json'
                        shutil.copy('data/emissions.json', backup_file)
                        st.warning(f"Corrupted emissions data file found. A backup has been created at {backup_file}")
                        # Create empty dataframe
                        st.session_state.emissions_data = pd.DataFrame(columns=[
                            'date', 'scope', 'category', 'activity', 'quantity', 
                            'unit', 'emission_factor', 'emissions_kgCO2e', 'notes',
                            'business_unit', 'project', 'country', 'facility', 
                            'responsible_person', 'data_quality', 'verification_status'
                        ])
                else:
                    # Empty file, create new DataFrame
                    st.session_state.emissions_data = pd.DataFrame(columns=[
                        'date', 'scope', 'category', 'activity', 'quantity', 
                        'unit', 'emission_factor', 'emissions_kgCO2e', 'notes',
                        'business_unit', 'project', 'country', 'facility', 
                        'responsible_person', 'data_quality', 'verification_status'
                    ])
        except Exception as e:
            st.error(f"Error loading emissions data: {str(e)}")
            # Create empty dataframe if loading fails
            st.session_state.emissions_data = pd.DataFrame(columns=[
                'date', 'scope', 'category', 'activity', 'quantity', 
                'unit', 'emission_factor', 'emissions_kgCO2e', 'notes',
                'business_unit', 'project', 'country', 'facility', 
                'responsible_person', 'data_quality', 'verification_status'
            ])
            # Make sure data directory exists
            os.makedirs('data', exist_ok=True)
    else:
        st.session_state.emissions_data = pd.DataFrame(columns=[
            'date', 'scope', 'category', 'activity', 'quantity', 
            'unit', 'emission_factor', 'emissions_kgCO2e', 'notes',
            'business_unit', 'project', 'country', 'facility', 
            'responsible_person', 'data_quality', 'verification_status'
        ])
        # Make sure data directory exists
        os.makedirs('data', exist_ok=True)
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'
if 'active_page' not in st.session_state:
    st.session_state.active_page = "AI Insights"

# Translation dictionary (English and Bengali)
translations = {
    'English': {
        'title': 'YourCarbonFootprint Bangladesh',
        'subtitle': 'Carbon Accounting & Reporting Tool for Bangladesh SMEs',
        'dashboard': 'Dashboard',
        'data_entry': 'Data Entry',
        'reports': 'Reports',
        'settings': 'Settings',
        'about': 'About',
        'scope1': 'Scope 1 (Direct Emissions)',
        'scope2': 'Scope 2 (Indirect Emissions - Purchased Energy)',
        'scope3': 'Scope 3 (Other Indirect Emissions)',
        'date': 'Date',
        'scope': 'Scope',
        'category': 'Category',
        'activity': 'Activity',
        'quantity': 'Quantity',
        'unit': 'Unit',
        'emission_factor': 'Emission Factor',
        'emissions': 'Emissions (kgCO2e)',
        'notes': 'Notes',
        'add_entry': 'Add Entry',
        'upload_csv': 'Upload CSV',
        'download_report': 'Download Report',
        'total_emissions': 'Total Emissions',
        'emissions_by_scope': 'Emissions by Scope',
        'emissions_by_category': 'Emissions by Category',
        'emissions_over_time': 'Emissions Over Time',
        'language': 'Language',
        'save': 'Save',
        'cancel': 'Cancel',
        'success': 'Success!',
        'error': 'Error!',
        'entry_added': 'Entry added successfully!',
        'csv_uploaded': 'CSV uploaded successfully!',
        'report_downloaded': 'Report downloaded successfully!',
        'settings_saved': 'Settings saved successfully!',
        'no_data': 'No data available.',
        'welcome_message': 'Welcome to YourCarbonFootprint Bangladesh! Start by adding your emissions data or uploading a CSV file.',
        'custom_category': 'Custom Category',
        'custom_activity': 'Custom Activity',
        'custom_unit': 'Custom Unit',
        'entry_failed': 'Failed to add entry.'
    },
    'Bengali': {
        'title': 'আপনার কার্বন ফুটপ্রিন্ট বাংলাদেশ',
        'subtitle': 'বাংলাদেশী এসএমই-দের জন্য কার্বন অ্যাকাউন্টিং ও রিপোর্টিং টুল',
        'dashboard': 'ড্যাশবোর্ড',
        'data_entry': 'ডেটা এন্ট্রি',
        'reports': 'রিপোর্ট',
        'settings': 'সেটিংস',
        'about': 'সম্পর্কে',
        'scope1': 'স্কোপ ১ (প্রত্যক্ষ নিঃসরণ)',
        'scope2': 'স্কোপ ২ (পরোক্ষ নিঃসরণ - ক্রয়কৃত শক্তি)',
        'scope3': 'স্কোপ ৩ (অন্যান্য পরোক্ষ নিঃসরণ)',
        'date': 'তারিখ',
        'scope': 'স্কোপ',
        'category': 'বিভাগ',
        'activity': 'কার্যকলাপ',
        'quantity': 'পরিমাণ',
        'unit': 'একক',
        'emission_factor': 'নিঃসরণ ফ্যাক্টর',
        'emissions': 'নিঃসরণ (kgCO2e)',
        'notes': 'নোট',
        'add_entry': 'এন্ট্রি যোগ করুন',
        'upload_csv': 'CSV আপলোড করুন',
        'download_report': 'রিপোর্ট ডাউনলোড করুন',
        'total_emissions': 'মোট নিঃসরণ',
        'emissions_by_scope': 'স্কোপ অনুযায়ী নিঃসরণ',
        'emissions_by_category': 'বিভাগ অনুযায়ী নিঃসরণ',
        'emissions_over_time': 'সময়ের সাথে নিঃসরণ',
        'language': 'ভাষা',
        'save': 'সংরক্ষণ',
        'cancel': 'বাতিল',
        'success': 'সফল!',
        'error': 'ত্রুটি!',
        'entry_added': 'এন্ট্রি সফলভাবে যোগ করা হয়েছে!',
        'csv_uploaded': 'CSV সফলভাবে আপলোড হয়েছে!',
        'report_downloaded': 'রিপোর্ট সফলভাবে ডাউনলোড হয়েছে!',
        'settings_saved': 'সেটিংস সফলভাবে সংরক্ষিত হয়েছে!',
        'no_data': 'কোন ডেটা উপলব্ধ নেই।',
        'welcome_message': 'YourCarbonFootprint Bangladesh-এ স্বাগতম! আপনার নিঃসরণ ডেটা যোগ করে বা CSV ফাইল আপলোড করে শুরু করুন।',
        'custom_category': 'কাস্টম বিভাগ',
        'custom_activity': 'কাস্টম কার্যকলাপ',
        'custom_unit': 'কাস্টম একক',
        'entry_failed': 'এন্ট্রি যোগ করতে ব্যর্থ।'
    }
}

# Bangladesh-specific emission factors (in kgCO2e per unit)
BANGLADESH_EMISSION_FACTORS = {
    # Scope 1 - Direct emissions
    "Stationary Combustion": {
        "Natural Gas": {"factor": 0.18316, "unit": "kWh"},
        "Diesel": {"factor": 2.68787, "unit": "liter"},
        "Furnace Oil": {"factor": 3.15123, "unit": "liter"},
        "Coal": {"factor": 2.42287, "unit": "kg"},
        "Biomass": {"factor": 0.0, "unit": "kg"},  # Considered carbon neutral
    },
    "Mobile Combustion": {
        "Petrol/Gasoline": {"factor": 2.31495, "unit": "liter"},
        "Diesel": {"factor": 2.70553, "unit": "liter"},
        "CNG": {"factor": 2.53721, "unit": "kg"},
        "LPG": {"factor": 1.55537, "unit": "liter"},
    },
    "Refrigerants": {
        "R-410A": {"factor": 2088.0, "unit": "kg"},
        "R-134a": {"factor": 1430.0, "unit": "kg"},
        "R-404A": {"factor": 3922.0, "unit": "kg"},
        "R-407C": {"factor": 1774.0, "unit": "kg"},
    },
    
    # Scope 2 - Indirect emissions from purchased energy
    "Electricity": {
        "Bangladesh Grid": {"factor": 0.6815, "unit": "kWh"},  # Based on Bangladesh's electricity grid mix
        "Solar Power": {"factor": 0.041, "unit": "kWh"},
        "Hydropower": {"factor": 0.024, "unit": "kWh"},
        "Wind Power": {"factor": 0.011, "unit": "kWh"},
    },
    "Steam": {
        "Purchased Steam": {"factor": 0.19, "unit": "kg"},
    },
    
    # Scope 3 - Other indirect emissions
    "Business Travel": {
        "Domestic Flight": {"factor": 0.15298, "unit": "passenger-km"},
        "International Flight": {"factor": 0.19085, "unit": "passenger-km"},
        "Train": {"factor": 0.03694, "unit": "passenger-km"},
        "Bus": {"factor": 0.10471, "unit": "passenger-km"},
        "Rickshaw (CNG)": {"factor": 0.08545, "unit": "km"},
        "Taxi": {"factor": 0.14549, "unit": "km"},
    },
    "Employee Commuting": {
        "Car (Petrol)": {"factor": 0.17336, "unit": "km"},
        "Car (Diesel)": {"factor": 0.16844, "unit": "km"},
        "Motorcycle": {"factor": 0.11501, "unit": "km"},
        "Bus": {"factor": 0.10471, "unit": "passenger-km"},
        "Rickshaw (CNG)": {"factor": 0.08545, "unit": "passenger-km"},
        "Train": {"factor": 0.03694, "unit": "passenger-km"},
    },
    "Waste": {
        "Landfill": {"factor": 0.45727, "unit": "kg"},
        "Recycling": {"factor": 0.01042, "unit": "kg"},
        "Composting": {"factor": 0.01042, "unit": "kg"},
        "Incineration": {"factor": 0.01613, "unit": "kg"},
    },
    "Water": {
        "Water Supply": {"factor": 0.298, "unit": "cubic meter"},  # Adjusted for Bangladesh
        "Water Treatment": {"factor": 0.615, "unit": "cubic meter"},
    },
    "Purchased Goods & Services": {
        "Jute Products": {"factor": 0.82, "unit": "kg"},  # Bangladesh-specific
        "Cotton Textiles": {"factor": 5.89, "unit": "kg"},
        "Leather Products": {"factor": 17.0, "unit": "kg"},
        "Paper": {"factor": 0.919, "unit": "kg"},
        "Plastic": {"factor": 3.14, "unit": "kg"},
        "Steel": {"factor": 2.58, "unit": "kg"},
        "Cement": {"factor": 0.82, "unit": "kg"},
        "Rice": {"factor": 2.7, "unit": "kg"},  # Important staple food
        "Fish": {"factor": 5.4, "unit": "kg"},  # Major protein source
    },
}

# Function to get translated text
def t(key):
    lang = st.session_state.language
    return translations.get(lang, {}).get(key, key)

# Function to save emissions data
def save_emissions_data():
    try:
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Create a backup of the existing file if it exists
        if os.path.exists('data/emissions.json'):
            backup_path = 'data/emissions_backup.json'
            try:
                with open('data/emissions.json', 'r') as src, open(backup_path, 'w') as dst:
                    dst.write(src.read())
            except Exception:
                # Continue even if backup fails
                pass
        
        # Save data to JSON file with proper formatting
        with open('data/emissions.json', 'w') as f:
            if len(st.session_state.emissions_data) > 0:
                json.dump(st.session_state.emissions_data.to_dict('records'), f, indent=2)
            else:
                # Write empty array if no data
                f.write('[]')
                
        return True
    except Exception as e:
        st.error(f"Error saving data: {str(e)}")
        return False

# Function to add new emission entry
def add_emission_entry(date, business_unit, project, scope, category, activity, country, facility, responsible_person, quantity, unit, emission_factor, data_quality, verification_status, notes):
    """Add a new emission entry to the emissions data."""
    try:
        # Calculate emissions
        emissions_kgCO2e = float(quantity) * float(emission_factor)
        
        # Create new entry
        new_entry = pd.DataFrame([{
            'date': date.strftime('%Y-%m-%d'),
            'business_unit': business_unit,
            'project': project,
            'scope': scope,
            'category': category,
            'activity': activity,
            'country': country,
            'facility': facility,
            'responsible_person': responsible_person,
            'quantity': float(quantity),
            'unit': unit,
            'emission_factor': float(emission_factor),
            'emissions_kgCO2e': emissions_kgCO2e,
            'data_quality': data_quality,
            'verification_status': verification_status,
            'notes': notes
        }])
        
        # Add to existing data
        st.session_state.emissions_data = pd.concat([st.session_state.emissions_data, new_entry], ignore_index=True)
        
        # Save data and return success/failure
        return save_emissions_data()
    except Exception as e:
        st.error(f"Error adding entry: {str(e)}")
        return False

def delete_emission_entry(index):
    try:
        # Make a copy of the current data
        if len(st.session_state.emissions_data) > index:
            # Drop the row at the specified index
            st.session_state.emissions_data = st.session_state.emissions_data.drop(index).reset_index(drop=True)
            
            # Save data and return success/failure
            return save_emissions_data()
        else:
            st.error("Invalid index for deletion")
            return False
    except Exception as e:
        st.error(f"Error deleting entry: {str(e)}")
        return False

# Function to process uploaded CSV
def process_csv(uploaded_file):
    """Process uploaded CSV file and add to emissions data."""
    try:
        # Read CSV file
        df = pd.read_csv(uploaded_file)
        required_columns = ['date', 'scope', 'category', 'activity', 'quantity', 'unit', 'emission_factor']
        
        # Check if all required columns exist
        if not all(col in df.columns for col in required_columns):
            st.error(f"CSV must contain all required columns: {', '.join(required_columns)}")
            return False
        
        # Validate data types
        try:
            # Convert quantity and emission_factor to float
            df['quantity'] = df['quantity'].astype(float)
            df['emission_factor'] = df['emission_factor'].astype(float)
            
            # Validate dates
            df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        except Exception as e:
            st.error(f"Data validation error: {str(e)}")
            return False
        
        # Calculate emissions if not provided
        if 'emissions_kgCO2e' not in df.columns:
            df['emissions_kgCO2e'] = df['quantity'] * df['emission_factor']
        
        # Add enterprise fields if not present
        enterprise_fields = {
            'business_unit': 'Corporate',
            'project': 'Not Applicable',
            'country': 'Bangladesh',
            'facility': '',
            'responsible_person': '',
            'data_quality': 'Medium',
            'verification_status': 'Unverified',
            'notes': ''
        }
        
        # Add missing columns with default values
        for field, default_value in enterprise_fields.items():
            if field not in df.columns:
                df[field] = default_value
        
        # Append to existing data
        st.session_state.emissions_data = pd.concat([st.session_state.emissions_data, df], ignore_index=True)
        
        # Save data
        if save_emissions_data():
            st.success(f"Successfully added {len(df)} entries")
            return True
        else:
            st.error("Failed to save data")
            return False
    except Exception as e:
        st.error(f"Error processing CSV: {str(e)}")
        return False

# Custom CSS for Bangladesh theme
def local_css():
    st.markdown('''
    <style>
    /* Remove default Streamlit styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Base styling */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', 'Roboto', sans-serif;
    }
    
    /* Main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Sidebar styling with Bangladesh colors */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #006A4E 0%, #F42A41 100%) !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent !important;
        padding: 2rem 1rem;
    }
    
    /* Sidebar title with white text */
    [data-testid="stSidebar"] h1 {
        color: #ffffff !important;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Sidebar subtitle */
    [data-testid="stSidebar"] p {
        color: #000000 !important;  /* Keep black text on hover */
        font-size: 14px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Sidebar text elements */
    [data-testid="stSidebar"] .stSelectbox label {
        color: #ffffff !important;
        font-weight: 500;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Headings with Bangladesh green */
    h1, h2, h3, h4, h5, h6 {
        color: #006A4E;
        font-weight: 600;
    }
    
    h1 {
        font-size: 2rem;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        font-size: 1.5rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        font-size: 1.2rem;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }
    
    /* Card styling */
    .stCard {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        border-left: 4px solid #006A4E;
    }
    
    /* Metric cards with Bangladesh theme */
    .metric-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        border-left: 4px solid #006A4E;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        margin: 0.5rem 0;
        color: #006A4E;
    }
    
    .metric-label {
        font-size: 14px;
        color: #555555;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Buttons with Bangladesh colors */
    .stButton>button {
        background-color: #006A4E;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 0.5rem 1rem;
        font-size: 16px;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        background-color: #004D38;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    .stButton>button:focus {
        box-shadow: 0 0 0 2px rgba(0, 106, 78, 0.5);
    }
    
    /* Secondary buttons */
    .stButton>button[kind="secondary"] {
        background-color: #f8f9fa;
        color: #006A4E;
        border: 1px solid #006A4E;
    }
    
    .stButton>button[kind="secondary"]:hover {
        background-color: #f1f3f5;
    }
    
    /* Tabs with Bangladesh theme */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f8f9fa;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 16px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #006A4E !important;
        color: white !important;
    }
    
    /* Info boxes */
    .info-box {
        background-color: #E8F5E8;
        border-left: 4px solid #006A4E;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .warning-box {
        background-color: #FFF8E1;
        border-left: 4px solid #FFC107;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    /* Sidebar navigation buttons */
    [data-testid="stSidebar"] .stButton>button {
        width: 100%;
        text-align: left;
        background-color: rgba(255,255,255,0.1);
        color: #000000 !important;  /* Black text */
        border: 1px solid rgba(255,255,255,0.2);
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 4px;
        font-weight: normal;
        display: flex;
        align-items: center;
    }
    
    [data-testid="stSidebar"] .stButton>button:hover {
        background-color: rgba(255,255,255,0.2);
        color: #000000 !important;  /* Keep black text on hover */
        box-shadow: none;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        color: #ffffff;
        font-size: 12px;
        margin-top: 2rem;
        border-top: 1px solid rgba(255,255,255,0.2);
    }
    </style>
    ''', unsafe_allow_html=True)

# Navigation component
def render_navigation():
    nav_items = [
        {"icon": "🤖", "label": "AI Insights", "id": "AI Insights"},
        {"icon": "📝", "label": "Data Entry", "id": "Data Entry"},
        {"icon": "📊", "label": "Dashboard", "id": "Dashboard"},
        {"icon": "⚙️", "label": "Settings", "id": "Settings"}
    ]
    
    st.markdown("### Navigation")
    
    for item in nav_items:
        if st.sidebar.button(
            f"{item['icon']} {item['label']}", 
            key=f"nav_{item['id']}",
            help=f"Go to {item['label']}",
            use_container_width=True
        ):
            st.session_state.active_page = item["id"]
            st.rerun()

# Metric card component
def metric_card(title, value, description=None, icon=None, prefix="", suffix=""):
    st.markdown(f'''
    <div class="metric-card">
        {f'<div style="font-size: 24px;">{icon}</div>' if icon else ''}
        <div class="metric-label">{title}</div>
        <div class="metric-value">{prefix}{value}{suffix}</div>
        {f'<div style="color: #aaa; font-size: 12px;">{description}</div>' if description else ''}
    </div>
    ''', unsafe_allow_html=True)

# Apply custom CSS
local_css()

# Sidebar
with st.sidebar:
    st.markdown(f"<h1 style='margin-bottom: 0; font-size: 24px;'>{t('title')}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top: 0; color: #f0f0f0; font-size: 12px;'>{t('subtitle')}</p>", unsafe_allow_html=True)
    
    st.divider()
    
    # Language selector
    language = st.selectbox(t('language'), ['English', 'Bengali'])
    if language != st.session_state.language:
        st.session_state.language = language
        st.rerun()
    
    st.divider()
    
    # Navigation
    render_navigation()
    
    st.divider()
    
    # Footer
    st.markdown(
        "<div class='footer' style='color: #ffffff;'>© 2025 YourCarbonFootprint Bangladesh<br>Product Owner: GxDx Solutions<br>dipesh.cse@gmail.com</div>",
        unsafe_allow_html=True
    )

# Main content based on active page
if st.session_state.active_page == "Dashboard":
    st.markdown(f"<h1>🇧🇩 {t('dashboard')}</h1>", unsafe_allow_html=True)
    
    if len(st.session_state.emissions_data) == 0:
        st.markdown(f"<div class='info-box'>{t('welcome_message')}</div>", unsafe_allow_html=True)
    else:
        # Calculate metrics
        st.session_state.emissions_data['emissions_kgCO2e'] = pd.to_numeric(st.session_state.emissions_data['emissions_kgCO2e'], errors='coerce')
        st.session_state.emissions_data['emissions_kgCO2e'].fillna(0, inplace=True)
        
        total_emissions = st.session_state.emissions_data['emissions_kgCO2e'].sum()
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            metric_card(
                title=t('total_emissions'),
                value=f"{total_emissions:.2f}",
                suffix=" kgCO2e",
                icon="🇧🇩"
            )
        with col2:
            if 'date' in st.session_state.emissions_data.columns:
                st.session_state.emissions_data['date'] = pd.to_datetime(st.session_state.emissions_data['date'], errors='coerce')
                if not st.session_state.emissions_data['date'].isnull().all():
                    latest_date = st.session_state.emissions_data['date'].max().strftime('%Y-%m-%d')
                else:
                    latest_date = "No date data"
                metric_card(
                    title="Latest Entry",
                    value=latest_date,
                    icon="📅"
                )
        with col3:
            entry_count = len(st.session_state.emissions_data)
            metric_card(
                title="Total Entries",
                value=str(entry_count),
                icon="📊"
            )
        with col4:
            # Carbon intensity per taka (approximate)
            if total_emissions > 0:
                metric_card(
                    title="Carbon Intensity",
                    value=f"{total_emissions/1000:.3f}",
                    suffix=" tCO2e",
                    description="Tonnes CO2e",
                    icon="🏭"
                )
        
        # Charts
        st.markdown(f"<h2>{t('emissions_by_scope')}</h2>", unsafe_allow_html=True)
        
        if total_emissions > 0:
            scope_data = st.session_state.emissions_data.groupby('scope')['emissions_kgCO2e'].sum().reset_index()
            
            if not scope_data.empty and scope_data['emissions_kgCO2e'].sum() > 0:
                fig1 = px.pie(
                    scope_data, 
                    values='emissions_kgCO2e', 
                    names='scope', 
                    color='scope', 
                    color_discrete_map={'Scope 1': '#006A4E', 'Scope 2': '#F42A41', 'Scope 3': '#FFD700'},
                    hole=0.4
                )
                fig1.update_layout(
                    margin=dict(t=0, b=0, l=0, r=0),
                    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
                    height=400
                )
                st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})
            else:
                st.info("No emissions data available for scope breakdown.")
        else:
            st.info("No emissions data available for scope breakdown.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"<h2>{t('emissions_by_category')}</h2>", unsafe_allow_html=True)
            
            if total_emissions > 0:
                category_data = st.session_state.emissions_data.groupby('category')['emissions_kgCO2e'].sum().reset_index()
                category_data = category_data.sort_values('emissions_kgCO2e', ascending=False)
                
                if not category_data.empty and category_data['emissions_kgCO2e'].sum() > 0:
                    fig2 = px.bar(
                        category_data, 
                        x='category', 
                        y='emissions_kgCO2e', 
                        color='category',
                        color_discrete_sequence=['#006A4E', '#F42A41', '#FFD700', '#228B22', '#DC143C'],
                        labels={'emissions_kgCO2e': 'Emissions (kgCO2e)', 'category': 'Category'}
                    )
                    fig2.update_layout(
                        showlegend=False,
                        margin=dict(t=0, b=0, l=0, r=0),
                        height=400
                    )
                    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})
                else:
                    st.info("No emissions data available for category breakdown.")
            else:
                st.info("No emissions data available for category breakdown.")
        
        with col2:
            st.markdown(f"<h2>{t('emissions_over_time')}</h2>", unsafe_allow_html=True)
            
            if total_emissions > 0 and 'date' in st.session_state.emissions_data.columns:
                time_data = st.session_state.emissions_data.copy()
                time_data['date'] = pd.to_datetime(time_data['date'], errors='coerce')
                time_data = time_data.dropna(subset=['date'])
                
                if not time_data.empty:
                    time_data['month'] = time_data['date'].dt.strftime('%Y-%m')
                    time_data = time_data.groupby(['month', 'scope'])['emissions_kgCO2e'].sum().reset_index()
                    
                    if len(time_data['month'].unique()) > 0:
                        fig3 = px.line(
                            time_data, 
                            x='month', 
                            y='emissions_kgCO2e', 
                            color='scope', 
                            markers=True,
                            color_discrete_map={'Scope 1': '#006A4E', 'Scope 2': '#F42A41', 'Scope 3': '#FFD700'},
                            labels={'emissions_kgCO2e': 'Emissions (kgCO2e)', 'month': 'Month', 'scope': 'Scope'}
                        )
                        fig3.update_layout(
                            margin=dict(t=0, b=0, l=0, r=0),
                            xaxis_title="",
                            yaxis_title="kgCO2e",
                            legend_title="",
                            height=400
                        )
                        st.plotly_chart(fig3, use_container_width=True, config={'displayModeBar': False})
                    else:
                        st.info("Not enough time data to show emissions over time.")
                else:
                    st.info("No valid date data available for time series chart.")
            else:
                st.info("No emissions data available for time series chart.")

elif st.session_state.active_page == "Data Entry":
    st.markdown(f"<h1>📝 {t('data_entry')}</h1>", unsafe_allow_html=True)
    
    tabs = st.tabs(["✍️ Manual Entry", "📤 CSV Upload"])
    
    with tabs[0]:
        st.markdown("<h3>Add New Emission Entry</h3>", unsafe_allow_html=True)
        with st.form("emission_form", border=False):
            col1, col2 = st.columns(2)
            with col1:
                date = st.date_input(t('date'), datetime.now(), help="Date when the emission occurred")
                
                business_unit = st.selectbox(
                    "Business Unit", 
                    ["Corporate", "Manufacturing", "Textiles", "RMG", "Agriculture", "Fisheries", "IT", "Services", "Other"],
                    help="The business unit responsible for this emission"
                )
                if business_unit == "Other":
                    business_unit = st.text_input("Custom Business Unit", placeholder="Enter business unit name")
                
                project = st.selectbox(
                    "Project", 
                    ["Not Applicable", "Green Factory Initiative", "Energy Efficiency Program", "Renewable Energy", "Waste Reduction", "Other"],
                    help="The project or initiative associated with this emission"
                )
                if project == "Other":
                    project = st.text_input("Custom Project", placeholder="Enter project name")
                
                scope = st.selectbox(
                    t('scope'), 
                    ['Scope 1', 'Scope 2', 'Scope 3'],
                    help="Scope 1: Direct emissions\nScope 2: Purchased electricity\nScope 3: Value chain emissions"
                )
                
                category_options = {
                    'Scope 1': ['Stationary Combustion', 'Mobile Combustion', 'Refrigerants', 'Process Emissions', 'Other'],
                    'Scope 2': ['Electricity', 'Steam', 'Other'],
                    'Scope 3': ['Business Travel', 'Employee Commuting', 'Waste', 'Water', 'Purchased Goods & Services', 'Other']
                }
                category = st.selectbox(
                    t('category'), 
                    category_options[scope],
                    help="The category of emission source"
                )
                if category == 'Other':
                    category = st.text_input(t('custom_category'), placeholder="Enter custom category")
                
                country_options = ['Bangladesh', 'India', 'China', 'United States', 'United Kingdom', 'Other']
                country = st.selectbox(
                    "Country", 
                    country_options,
                    help="Country where the emission occurred"
                )
                if country == 'Other':
                    country = st.text_input("Custom Country", placeholder="Enter country name")
                
                facility = st.text_input(
                    "Facility/Location", 
                    placeholder="e.g., Dhaka Factory, Chittagong Port, etc.",
                    help="Specific facility or location where the emission occurred"
                )
                
                responsible_person = st.text_input(
                    "Responsible Person", 
                    placeholder="Person responsible for this emission source",
                    help="Name of the person accountable for managing this emission source"
                )
            
            with col2:
                # Activity options based on category
                activity_options = {
                    'Stationary Combustion': ['Natural Gas Boiler', 'Diesel Generator', 'Furnace Oil Boiler', 'Coal Furnace', 'Biomass Boiler', 'Other'],
                    'Mobile Combustion': ['Company Vehicle', 'Delivery Truck', 'Motorcycle', 'CNG Vehicle', 'Other'],
                    'Refrigerants': ['AC System', 'Cold Storage', 'Refrigerator', 'Other'],
                    'Electricity': ['Bangladesh Grid', 'Solar Power', 'Hydropower', 'Wind Power', 'Other'],
                    'Business Travel': ['Domestic Flight', 'International Flight', 'Train', 'Bus', 'Rickshaw (CNG)', 'Taxi', 'Other'],
                    'Employee Commuting': ['Car (Petrol)', 'Car (Diesel)', 'Motorcycle', 'Bus', 'Rickshaw (CNG)', 'Train', 'Other'],
                    'Waste': ['Landfill', 'Recycling', 'Composting', 'Incineration', 'Other'],
                    'Water': ['Water Supply', 'Water Treatment', 'Other'],
                    'Purchased Goods & Services': ['Jute Products', 'Cotton Textiles', 'Leather Products', 'Paper', 'Steel', 'Cement', 'Rice', 'Fish', 'Other'],
                    'Other': ['Custom Activity', 'Other']
                }
                
                activity_key = category if category != 'Other' else 'Other'
                activity_list = activity_options.get(activity_key, ['Other'])
                activity = st.selectbox(
                    "Activity", 
                    activity_list,
                    help="Specific activity that generated the emissions"
                )
                if activity == 'Other':
                    activity = st.text_input("Custom Activity", placeholder="Enter custom activity")
                
                quantity = st.number_input(
                    t('quantity'), 
                    min_value=0.0, 
                    format="%.2f",
                    help="The amount of activity (e.g., kWh used, liters consumed, etc.)"
                )
                
                unit_options = ['kWh', 'MWh', 'liter', 'kg', 'tonne', 'km', 'passenger-km', 'cubic meter', 'BDT', 'USD', 'Other']
                unit = st.selectbox(
                    t('unit'), 
                    unit_options,
                    help="The unit of measurement for the quantity"
                )
                if unit == 'Other':
                    unit = st.text_input(t('custom_unit'), placeholder="Enter custom unit")
                
                # Get default emission factor for Bangladesh
                default_factor = 0.0
                if category in BANGLADESH_EMISSION_FACTORS:
                    if activity in BANGLADESH_EMISSION_FACTORS[category]:
                        default_factor = BANGLADESH_EMISSION_FACTORS[category][activity]["factor"]
                
                st.info(f"💡 AI Suggestion: Emission factor for {activity} in Bangladesh: {default_factor:.4f} kgCO2e per {unit}")
                
                emission_factor = st.number_input(
                    t('emission_factor'), 
                    min_value=0.0, 
                    value=default_factor, 
                    format="%.4f",
                    help=f"Emission factor in kgCO2e per unit"
                )
                
                data_quality = st.select_slider(
                    "Data Quality",
                    options=["Low", "Medium", "High"],
                    value="Medium",
                    help="🔴 Low: Estimated\n🟡 Medium: From bills\n🟢 High: Measured"
                )
                
                verification_status = st.selectbox(
                    "Verification Status",
                    ["Unverified", "Internally Verified", "Third-Party Verified"],
                    help="Verification level of the data"
                )
                
                notes = st.text_area(
                    t('notes'), 
                    placeholder="Additional information, data sources, calculation methods, etc.",
                    help="Include relevant context and methodology"
                )
            
            # Form submission
            col1, col2 = st.columns([1, 1])
            with col1:
                submitted = st.form_submit_button(t('add_entry'), type="primary", use_container_width=True)
            with col2:
                clear = st.form_submit_button("Clear Form", type="secondary", use_container_width=True)
            
            if submitted:
                if quantity <= 0:
                    st.error("Quantity must be greater than zero.")
                else:
                    try:
                        if add_emission_entry(
                            date, business_unit, project, scope, category, activity, country, facility,
                            responsible_person, quantity, unit, emission_factor, data_quality, verification_status, notes
                        ):
                            st.success(t('entry_added'))
                            st.session_state.active_page = "Dashboard"
                            st.rerun()
                    except Exception as e:
                        st.error(f"{t('entry_failed')} {str(e)}")
    
    with tabs[1]:
        st.markdown("<h3>Upload CSV File</h3>", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(t('upload_csv'), type='csv')
        if uploaded_file is not None:
            if process_csv(uploaded_file):
                st.success(t('csv_uploaded'))
                st.session_state.active_page = "Dashboard"
                st.rerun()
            else:
                st.error("Failed to process CSV file. Please check the format.")
        
        # Sample CSV download for Bangladesh
        sample_data = {
            'date': ['2025-01-15', '2025-01-20'],
            'business_unit': ['Manufacturing', 'Corporate'],
            'project': ['Green Factory Initiative', 'Not Applicable'],
            'scope': ['Scope 2', 'Scope 1'],
            'category': ['Electricity', 'Mobile Combustion'],
            'activity': ['Bangladesh Grid', 'CNG Vehicle'],
            'country': ['Bangladesh', 'Bangladesh'],
            'facility': ['Dhaka Factory', 'Dhaka Office'],
            'responsible_person': ['Rahman Ahmed', 'Fatima Khan'],
            'quantity': [1000, 50],
            'unit': ['kWh', 'liter'],
            'emission_factor': [0.6815, 2.53721],
            'data_quality': ['High', 'Medium'],
            'verification_status': ['Internally Verified', 'Unverified'],
            'notes': ['Monthly electricity bill', 'Fleet vehicle fuel consumption']
        }
        sample_df = pd.DataFrame(sample_data)
        csv = sample_df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="Download Sample CSV (Bangladesh)",
            data=csv,
            file_name="sample_emissions_bangladesh.csv",
            mime="text/csv",
        )
    
    # Show existing data table
    if len(st.session_state.emissions_data) > 0:
        st.markdown("<h3>Existing Emissions Data</h3>", unsafe_allow_html=True)
        
        display_df = st.session_state.emissions_data.copy()
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.dataframe(
                display_df,
                column_config={
                    "date": st.column_config.DateColumn("Date"),
                    "business_unit": st.column_config.TextColumn("Business Unit"),
                    "scope": st.column_config.TextColumn("Scope"),
                    "category": st.column_config.TextColumn("Category"),
                    "activity": st.column_config.TextColumn("Activity"),
                    "country": st.column_config.TextColumn("Country"),
                    "facility": st.column_config.TextColumn("Facility"),
                    "quantity": st.column_config.NumberColumn("Quantity", format="%.2f"),
                    "unit": st.column_config.TextColumn("Unit"),
                    "emission_factor": st.column_config.NumberColumn("Emission Factor", format="%.4f"),
                    "emissions_kgCO2e": st.column_config.NumberColumn("Emissions (kgCO2e)", format="%.2f"),
                    "data_quality": st.column_config.TextColumn("Data Quality"),
                    "verification_status": st.column_config.TextColumn("Verification"),
                },
                use_container_width=True,
                hide_index=False
            )
        
        with col2:
            st.markdown("### Delete Entry")
            entry_to_delete = st.number_input("Select entry number to delete", min_value=0, 
                                           max_value=len(display_df)-1 if len(display_df) > 0 else 0, 
                                           step=1)
            
            if st.button("🗑️ Delete Selected Entry", type="primary"):
                if delete_emission_entry(entry_to_delete):
                    st.success(f"Entry {entry_to_delete} deleted successfully!")
                    st.rerun()

elif st.session_state.active_page == "Settings":
    st.markdown(f"<h1>⚙️ {t('settings')}</h1>", unsafe_allow_html=True)
    
    st.markdown("<h3>Company Information (Bangladesh)</h3>", unsafe_allow_html=True)
        
    with st.form("company_info_form"):
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company Name")
            industry = st.selectbox("Industry", [
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
                "Other"
            ])
            location = st.selectbox("Division", [
                "Dhaka",
                "Chittagong", 
                "Rajshahi",
                "Khulna",
                "Barisal",
                "Sylhet",
                "Rangpur",
                "Mymensingh"
            ])
        with col2:
            contact_person = st.text_input("Contact Person")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
        
        st.markdown("<h4>Export Markets</h4>", unsafe_allow_html=True)
        col1, col2, col3, col4, col5= st.columns(5)
        with col1:
            eu_market = st.checkbox("European Union")
        with col2:
            usa_market = st.checkbox("United States")
        with col3:
            japan_market = st.checkbox("Japan")
        with col4:
            india_market = st.checkbox("India")
        with col5:
            bd_market = st.checkbox("Bangladesh")
        
        st.markdown("<h4>Bangladesh-Specific Information</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            export_earnings = st.number_input("Annual Export Earnings (USD)", min_value=0.0, format="%.2f")
            employee_count = st.number_input("Number of Employees", min_value=0, step=1)
        with col2:
            bida_registered = st.checkbox("BIDA Registered")
            etp_status = st.selectbox("ETP Status", ["Not Applicable", "Planned", "Under Construction", "Operational"])
        
        submitted = st.form_submit_button("Save Settings")
        if submitted:
            st.success("Settings saved successfully!")

elif st.session_state.active_page == "AI Insights":
    st.markdown(f"<h1>🤖 AI Insights for Bangladesh</h1>", unsafe_allow_html=True)
    
    # Import AI agents
    try:
        from ai_agents import CarbonFootprintAgents
        
        if 'ai_agents' not in st.session_state:
            st.session_state.ai_agents = CarbonFootprintAgents()
        
        ai_tabs = st.tabs(["🔍 Data Assistant", "📊 Report Summary", "🌱 Offset Advisor", "📋 Regulation Radar", "⚡ Emission Optimizer"])
        
        with ai_tabs[0]:
            st.markdown("<h3>Data Entry Assistant</h3>", unsafe_allow_html=True)
            st.markdown("Get help with classifying emissions specific to Bangladesh industries.")
            
            data_description = st.text_area("Describe your emission activity", 
                                          placeholder="Example: We operate a jute processing mill in Dhaka. We use diesel generators during load shedding. How should I categorize this?")
            
            if st.button("Get Assistance", key="data_assistant_btn"):
                if data_description:
                    with st.spinner("AI assistant is analyzing your request..."):
                        try:
                            result = st.session_state.ai_agents.run_data_entry_crew(data_description)
                            result_str = str(result)
                            st.markdown(f"<div class='stCard'>{result_str}</div>", unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error: {str(e)}. Please check your API key and try again.")
                else:
                    st.warning("Please describe your emission activity first.")
        
        with ai_tabs[1]:
            st.markdown("<h3>Report Summary Generator</h3>", unsafe_allow_html=True)
            st.markdown("Generate Bangladesh-focused emissions summaries.")
            
            if len(st.session_state.emissions_data) == 0:
                st.warning("No emissions data available. Please add data first.")
            else:
                if st.button("Generate Summary", key="report_summary_btn"):
                    with st.spinner("Generating report summary..."):
                        try:
                            emissions_str = st.session_state.emissions_data.to_string()
                            result = st.session_state.ai_agents.run_report_summary_crew(emissions_str)
                            result_str = str(result)
                            st.markdown(f"<div class='stCard'>{result_str}</div>", unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error: {str(e)}. Please check your API key and try again.")
        
        with ai_tabs[2]:
            st.markdown("<h3>Carbon Offset Advisor</h3>", unsafe_allow_html=True)
            st.markdown("Get recommendations for carbon offset options available in Bangladesh.")
            
            col1, col2 = st.columns(2)
            with col1:
                location = st.selectbox("Location", [
                    "Dhaka", "Chittagong", "Rajshahi", "Khulna", 
                    "Barisal", "Sylhet", "Rangpur", "Mymensingh"
                ])
                industry = st.selectbox("Industry", [
                    "Ready Made Garments", "Textiles", "Jute Processing",
                    "Leather", "Pharmaceuticals", "Steel", "Cement",
                    "Agriculture", "Fisheries", "IT", "Other"
                ])
            
            if len(st.session_state.emissions_data) == 0:
                st.warning("No emissions data available. Please add data first.")
            else:
                total_emissions = st.session_state.emissions_data['emissions_kgCO2e'].sum()
                st.markdown(f"<p>Total emissions to offset: <strong>{total_emissions:.2f} kgCO2e</strong></p>", unsafe_allow_html=True)
                
                if st.button("Get Offset Recommendations", key="offset_advisor_btn"):
                    with st.spinner("Finding Bangladesh-specific offset options..."):
                        try:
                            result = st.session_state.ai_agents.run_offset_advice_crew(total_emissions, f"{location}, Bangladesh", industry)
                            result_str = str(result)
                            st.markdown(f"<div class='stCard'>{result_str}</div>", unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error: {str(e)}. Please check your API key and try again.")
        
        with ai_tabs[3]:
            st.markdown("<h3>Regulation Radar</h3>", unsafe_allow_html=True)
            st.markdown("Get insights on carbon regulations affecting Bangladesh exporters.")
            
            col1, col2 = st.columns(2)
            with col1:
                location = st.selectbox("Division", [
                    "Dhaka", "Chittagong", "Rajshahi", "Khulna", 
                    "Barisal", "Sylhet", "Rangpur", "Mymensingh"
                ], key="reg_location")
                industry = st.selectbox("Industry Sector", [
                    "Ready Made Garments", "Textiles", "Jute Processing",
                    "Leather", "Pharmaceuticals", "Steel", "Cement",
                    "Agriculture", "Fisheries", "IT", "Other"
                ], key="reg_industry")
            with col2:
                export_markets = st.multiselect("Export Markets", [
                    "European Union", "United States", "Japan", "Bangladesh","China", 
                    "India", "Canada", "Australia", "Other"
                ])
            
            if st.button("Check Bangladesh Regulations", key="regulation_radar_btn"):
                if len(export_markets) > 0:
                    with st.spinner("Analyzing regulatory requirements for Bangladesh..."):
                        try:
                            result = st.session_state.ai_agents.run_regulation_check_crew(
                                f"{location}, Bangladesh", industry, ", ".join(export_markets)
                            )
                            result_str = str(result)
                            st.markdown(f"<div class='stCard'>{result_str}</div>", unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error: {str(e)}. Please check your API key and try again.")
                else:
                    st.warning("Please select at least one export market.")
        
        with ai_tabs[4]:
            st.markdown("<h3>Emission Optimizer</h3>", unsafe_allow_html=True)
            st.markdown("Get AI-powered recommendations specific to Bangladesh context.")
            
            if len(st.session_state.emissions_data) == 0:
                st.warning("No emissions data available. Please add data first.")
            else:
                if st.button("Generate Bangladesh-Specific Recommendations", key="emission_optimizer_btn"):
                    with st.spinner("Analyzing your emissions data for Bangladesh context..."):
                        try:
                            emissions_str = st.session_state.emissions_data.to_string()
                            result = st.session_state.ai_agents.run_optimization_crew(emissions_str)
                            result_str = str(result)
                            st.markdown(f"<div class='stCard'>{result_str}</div>", unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error: {str(e)}. Please check your API key and try again.")
    
    except ImportError:
        st.error("AI agents module not found. Please ensure ai_agents.py is available.")
        st.info("You can still use the data entry and dashboard features without AI insights.")