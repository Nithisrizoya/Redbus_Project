# Redbus Data Scraping with Selenium &amp; Dynamic Filtering using Streamlit
The "Redbus Data Scraping with Selenium &amp; Dynamic Filtering using Streamlit" project automates bus travel data collection using Selenium, stores it in a SQL database, and enables interactive filtering via a Streamlit app. Users can filter data like bus routes, prices, and seat availability for analysis and decision-making.

# skills take away from this project:
Web Scraping using Selenium, Python, Streamlit, SQL.

# Business Use Cases:
The solution can be applied to various business scenarios including:
1.Travel Aggregators: Providing real-time bus schedules and seat availability for customers.
2.Market Analysis: Analyzing travel patterns and preferences for market research.
3.Customer Service: Enhancing user experience by offering customized travel options based on data insights.
4.Competitor Analysis: Comparing pricing and service levels with competitors.

# Approach:
1.Data Scraping:
   Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.
2.Data Storage:
   Store the scraped data in a SQL database.
3.Streamlit Application:
   Develop a Streamlit application to display and filter the scraped data.
   Implement various filters such as bustype, route, price range, star rating, availability.
4.Data Analysis/Filtering using Streamlit:
   Use SQL queries to retrieve and filter data based on user inputs.
   Use Streamlit to allow users to interact with and filter the data through the application.
   
# Results:
You should aim to:
   1.Successfully scrape a minimum of 10 Government State Bus Transport data from Redbus website using Selenium. Also include the private bus information for the selected routes.
   2.Store the data in a structured SQL database.
   3.Develop an interactive Streamlit application for data filtering.
   4.Ensure the application is user-friendly and efficient.
   
# Technical Tags:
   Web Scraping
   Selenium
   Streamlit
   SQL
   Data Analysis
   Python
   Interactive Application
   
# Data Set:
   1.Source: Data will be scraped from the Redbus website.
   2.Link- https://www.redbus.in/
   3.Format: The scraped data will be stored in a SQL database.
   4.Required Fields: Bus routes Link,Bus route Name, Bus name, Bus Type(Sleeper/Seater),  Departing Time, Duration, Reaching_Time, Star-rating, Price, Seat_availability.
   
# Data Set Requirements & Explanation:
The scraped dataset for this project should contain detailed information about bus services available on Redbus, covering various aspects critical to travelers and service providers. Here is a breakdown of the fields required:
   1.Bus Routes Name: This field captures the start and end locations of each bus journey, providing crucial information about the routes serviced.
   2.Bus Routes Link: Link for all the route details.
   3.Bus Name: The name of the bus or the service provider, which helps in identifying the specific operator.
   4.Bus Type (Sleeper/Seater/AC/Non-AC): This field specifies whether the bus is a sleeper or seater type, indicating the seating arrangements and comfort level offered.
   5.Departing Time: The scheduled departure time of the bus, essential for planning travel schedules.
   6.Duration: The total duration of the journey from the departure point to the destination, helping passengers estimate travel time.
   7.Reaching Time: The expected arrival time at the destination, allowing for better planning of onward travel or activities.
   8.Star Rating: A rating provided by passengers, indicating the quality of service based on factors such as comfort, punctuality, and staff behavior.
   9.Price: The cost of the ticket for the journey, which can vary based on factors like bus type and demand.
   10.Seat Availability: The number of seats available at the time of data scraping, giving real-time insight into the occupancy levels.
   
# Database Schema:  
   Table: bus_routes.
   
# Project Deliverables:
   1.Source Code: Python scripts for data scraping, SQL database interaction, and Streamlit application.
   2.Documentation: Detailed documentation explaining the code, data collection, and application usage.
   3.Database Schema: SQL scripts to create and populate the database.
   4.Application using Streamlit : Screenshots or links to the Streamlit application showing data filtering/ analysis.
