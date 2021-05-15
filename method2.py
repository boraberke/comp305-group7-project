# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                               #
# @authors: Ahmet Talha Akgül 68631                             #
#           Bora Berke Şahin  64060                             #
#           Pınar Erbil       68904                             #
#           Ufkun Özalp       69222                             #
#                                                               #        
#  Copyright © 2021 Dream Team™ - All Rights Reserved           #
#  You may use, distribute, and modify this code under the      #
#  terms of the Dream Team license, which unfortunately will    #
#  not be written for another century.                          #
#                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import numpy as np
optimum_course_centers = []
f = open("test2.txt", "r")
N = int(f.readline()) 
max_dist,min_fee,max_fee = f.readline().split(" ")
max_dist,min_fee,max_fee = int(max_dist),int(min_fee),int(max_fee)
size = max_fee-min_fee
course_centers = np.zeros(size+1)

for i in range(N):
    dist,fee = f.readline().split(" ")
    dist,fee = int(dist),int(fee)
    if dist <= max_dist and fee <= max_fee and fee >= min_fee: 
        if course_centers[fee-min_fee] > dist or course_centers[fee-min_fee] == 0: 
            course_centers[fee-min_fee] = dist
j = 0
while course_centers[j] == 0: j += 1 # find the first non-empty distance
current_dist = course_centers[j]
optimum_course_centers.append((current_dist,j+min_fee))
for i in range(j,len(course_centers)):
    if course_centers[i] == 0: continue
    fee = i + min_fee
    dist = course_centers[i]
    if dist < current_dist:
        optimum_course_centers.append((dist, fee))
        current_dist = dist
        current_fee = fee
#course_centers[8] = ((0,0))
print(course_centers)
print("OPTIMUM COURSE CENTERS")
print(optimum_course_centers)
print("Count of course centers: ", len(optimum_course_centers))






 