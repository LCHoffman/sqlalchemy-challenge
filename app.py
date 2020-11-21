################################################
# IMPORT DEPENDENCIES
################################################

import numpy as numpy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

################################################
# DATABASE SETUP
################################################
engine = create_engine("SQLITE:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

################################################
#FLASK SET UP
################################################
app = Flask(__name__)

################################################
#FLASK SET UP
################################################

@app.route("/")
def welcome():
    """List available API routes"""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #create session and query precipation and date data
    session = Session(engine)

    results = session.query(measurement.date, measurement.prcp).all()

    session.close()

    #create dictionary from row data and append to a list
    precip = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip.append(precip_dict)
    
    return jsonify(precip)




if __name__ == '__main__':
    app.run(debug=True)