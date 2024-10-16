# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# Load bus details for each state
df_andhrapradesh = pd.read_csv("ap_bus_details.csv")
df_assam = pd.read_csv("assam_bus_details.csv")
df_chandigarh = pd.read_csv("chandigarh_bus_details.csv")
df_himachal = pd.read_csv("himachal_bus_details.csv")
df_kerala = pd.read_csv("kerala_bus_details.csv")
df_rajasthan = pd.read_csv("rajasthan_bus_details.csv")
df_southbengal = pd.read_csv("sb_bus_details.csv")
df_telengana = pd.read_csv("Telangana_bus_details.csv")
df_uttarpradesh = pd.read_csv("up_bus_details.csv")
df_westbengal = pd.read_csv("wb_bus_details.csv")
df_jammukashmir = pd.read_csv("jk_bus_details.csv")
df_kadamba = pd.read_csv("kadamba_bus_details.csv")

# Create lists of routes for each state
lists_AP = df_andhrapradesh["Route_Name"].unique().tolist()
lists_A = df_assam["Route_Name"].unique().tolist()
lists_C = df_chandigarh["Route_Name"].unique().tolist()
lists_H = df_himachal["Route_Name"].unique().tolist()
lists_K = df_kerala["Route_Name"].unique().tolist()
lists_R = df_rajasthan["Route_Name"].unique().tolist()
lists_SB = df_southbengal["Route_Name"].unique().tolist()
lists_T = df_telengana["Route_Name"].unique().tolist()
lists_UP = df_uttarpradesh["Route_Name"].unique().tolist()
lists_WB = df_westbengal["Route_Name"].unique().tolist()
lists_JK = df_jammukashmir["Route_Name"].unique().tolist()
lists_KD = df_kadamba["Route_Name"].unique().tolist()

def categorize_bus(state, bus_name):
    prefixes = {
        "Andhrapradesh": "apsrtc",
        "Assam": "astc",
        "Chandigarh": "ctu",
        "Himachal": "hrtc",
        "Kerala": "ksrtc",
        "Rajasthan": "rsrtc",
        "South Bengal": "sbstc",
        "Telengana": "tsrtc",
        "Uttar Pradesh": "upsrtc",
        "West Bengal": "wbstc",
        "Jammu kashmir": "jkstc",
        "Kadamba": "ktcl"
    }
    
    if bus_name.lower().startswith(prefixes[state].lower()):
        return "GovernmentBus"
    else:
        return "PrivateBus"

# Setting up Streamlit page
slt.set_page_config(layout="wide")

web = option_menu(menu_title="🚌OnlineBus",
                  options=["Home", "📍States and Routes"],
                  icons=["house", "info-circle"],
                  orientation="horizontal"
                 )

# Home page settings
if web == "Home":
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:]  Transportation")
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL, mysql-connector-python, Streamlit.")
    slt.subheader(":blue[Developed-by:]  Nithisri")

# States and Routes page setting
if web == "📍States and Routes":
    S = slt.selectbox("Lists of States", ["Andhrapradesh", "Assam", "Chandigarh", "Himachal", "Kerala", "Rajasthan", 
                                          "South Bengal", "Telengana", "Uttar Pradesh", "West Bengal", "Jammu kashmir", "Kadamba"])
    
    # Based on selected state, set the appropriate list of routes
    if S == "Andhrapradesh":
        selected_route = slt.selectbox("List of routes", lists_AP)
    elif S == "Assam":
        selected_route = slt.selectbox("List of routes", lists_A)
    elif S == "Chandigarh":
        selected_route = slt.selectbox("List of routes", lists_C)
    elif S == "Himachal":
        selected_route = slt.selectbox("List of routes", lists_H)
    elif S == "Kerala":
        selected_route = slt.selectbox("List of routes", lists_K)
    elif S == "Rajasthan":
        selected_route = slt.selectbox("List of routes", lists_R)
    elif S == "South Bengal":
        selected_route = slt.selectbox("List of routes", lists_SB)
    elif S == "Telengana":
        selected_route = slt.selectbox("List of routes", lists_T)
    elif S == "Uttar Pradesh":
        selected_route = slt.selectbox("List of routes", lists_UP)
    elif S == "West Bengal":
        selected_route = slt.selectbox("List of routes", lists_WB)
    elif S == "Jammu kashmir":
        selected_route = slt.selectbox("List of routes", lists_JK)
    elif S == "Kadamba":
        selected_route = slt.selectbox("List of routes", lists_KD)

    # Add Bus Category Selection
    bus_type = slt.selectbox("Select Bus Type", ["All", "GovernmentBus", "PrivateBus"])

    # Function to fetch bus details based on selected route and category
    def fetch_bus_details(route_name, state, bus_type):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        query = f'''
            SELECT * FROM bus_details 
            WHERE Route_name = "{route_name}"
            ORDER BY Price DESC, Departing_Time DESC
        '''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        conn.close()

        df = pd.DataFrame(out, columns=[
            "ID", "Route_name", "Route_link", "Bus_name", "Bus_type", "Departing_Time","Duration", "Reaching_Time",
            "Star_Rating", "Price", "Seats_Available"
        ])
        
        # Apply Bus Type Filtering
        df["Bus_Category"] = df["Bus_name"].apply(lambda x: categorize_bus(state, x))
        
        if bus_type != "All":
            df = df[df["Bus_Category"] == bus_type]

        return df

    # Fetch and display the bus details
    df_result = fetch_bus_details(selected_route, S, bus_type)
    slt.dataframe(df_result)