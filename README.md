# SQLAlchemy Homework

## Background
You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## SQLAlchemy Requirements
Precipitation Analysis - Design a query to retrieve the last 12 months of precipitation data.
 
Station Analysis - Design three queries:
     * Design a query to calculate the total number of stations.
     * Design a query to find the most active stations.
     * Design a query to retrieve the last 12 months of temperature observation data (TOBS).

## Climate App Requirements
Now that you have completed your initial analysis, design a Flask API with the following routes based on the queries that you have just developed.
 * Home page
 * JSON of precipitation data and value
 * JSON of stations
 * JSON of temperature observations for previous year
 * JSON of minimum temperature, average temperature and max temperature for given start and end dates
      *  User should be able to filter for specific date ranges. Enter dates in YYYY-MM-DD format for best results.
