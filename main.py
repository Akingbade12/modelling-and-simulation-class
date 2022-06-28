import pandas as pd
import numpy as np

#Set predefined values
earliestArrival = 8.00 #Bank opening time
LatestArrival = 16.00 #Bank closing time
minServiceTime = 0.03 #Minimum time it takes server to attend to customer
MaxServiceTime = 0.06 #time in minutes on a 24 hour clock
walkingDistance = 0.01 #time in minutes to walk from door to the server

#Initial states
arrival = 0
served = 0
inQueue = 0
departed = 0

#to populate
columns = ["SN","event","arrival time","departure time","number in queue","service time","waiting time"]

SimResults = pd.DataFrame(columns=columns)




