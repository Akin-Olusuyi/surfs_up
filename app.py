import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify

# Set up database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database into classes
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# create flask routes


@app.route('/')
def welcome():
    return(
        '''
    Welcome to the Climate Analysis API! <br>
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end <br>
    ''')


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query for the date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # Dict with date as the key and prcp as the value
    #precip = {date: prcp for date, prcp in precipitation}
    precip = list(np.ravel(precipitation))
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    results = session.query(Station.station).all()
    # Unravel results into a 1D array and convert to a list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the primary station for all tobs from the last year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    # Return the results
    return jsonify(temps=temps)


@app.route("/api/v1.0/temp/<startdate>")
@app.route("/api/v1.0/temp/<startdate>/<enddate>")
def stats(startdate=None, enddate=None):
    # Return TMIN, TAVG, TMAX
    # Select statement
    sql = [func.min(Measurement.tobs), func.avg(
        Measurement.tobs), func.max(Measurement.tobs)]
    if not enddate:
        # Calculate TMIN, TAVG, TMAX for dates greater than start
        results = session.query(*sql).\
            filter(Measurement.date >= startdate).all()
    else:
        # Calculate TMIN, TAVG, TMAX with start and stop
        results = session.query(*sql).\
            filter(Measurement.date >= startdate).\
            filter(Measurement.date <= enddate).all()
    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    # Results
    return jsonify(temps=temps)

# to run use the following the terminal
# export FLASK_APP=app.py
# python3 -m flask run


if __name__ == '__main__':
    app.run()
