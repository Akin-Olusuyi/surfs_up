# Surf_Up

## Project Overview
Analyze temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Results
Here is the python code(jupyter notebook) base used for this analysis ![Code](https://github.com/Akin-Olusuyi/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

Taking at look at the summary statistics for June and December weather side by side there are a few differences we can point out.

<img src="https://github.com/Akin-Olusuyi/surfs_up/blob/main/June%20Summary%20Statistics.png" width="250"/> <img src="https://github.com/Akin-Olusuyi/surfs_up/blob/main/December%20Summary%20Statistics.png" width=""/>

- The average temprature in June from our data set is about 75 degrees compared to 71 degrees in December.
- The minimum temprature in December can be as low as 69 degrees whereas, in June the temperature could be as low as 64 degrees
- Looking at our summary statistics we can also say that, majority of the time, at least 75% of the time the weather in June will be around 77 degrees or higher and for December it will be 74 degrees or higher. 


## Summary
In summary, we can say that the surf and ice-cream shop business is sustainable year-round due to the warm temprature year round. However, temprature check is just one of many factors to consider. We should also dive a little deeper into our data set by running additional queries to help refine our analysis. Since our data is collected by multiple stations we can run queries to :

- Determine how many stations our available in our dataset :  *session.query(func.count(Station.station)).all()*

- What are the most active stations : *session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()*
        
 Then we can decided to use the most active station(s) for our summary statistics for both months. 

