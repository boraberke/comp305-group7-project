# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                               #
# @authors: Ahmet Talha Akgül                                   #
#           Bora Berke Şahin                                    #
#           Pınar Erbil                                         #
#           Ufkun Özalp                                         #
#                                                               #        
# Copyright © 2021 Dream Team - All Rights Reserved             #
#  You may use, distribute, and modify this code under the      #
#  terms of the Dream Team license, which unfortunately will    #
#  not be written for another century.                          #
#                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys
import time
start_time = time.time()
course_centers = []
optimum_course_centers = []
test_name = "test" + sys.argv[1] +".txt"
f = open(test_name, "r")
N = int(f.readline()) 
max_dist,min_fee,max_fee = f.readline().split(" ")
max_dist,min_fee,max_fee = int(max_dist),int(min_fee),int(max_fee)
for i in range(N):
    dist,fee = f.readline().split(" ")
    dist,fee = int(dist),int(fee)
    # a course center should be less than max_dist and fee should be in between min_fee,max_fee.
    if dist <= max_dist and fee <= max_fee and fee >= min_fee: 
        course_centers.append((dist,fee))
course_centers.sort() #sort points according to distance of the course centers.
current_dist,current_fee = course_centers[0]
optimum_course_centers.append((current_dist,current_fee)) #first one must be added anyway
for dist,fee in course_centers:
    #if their distance is not equal, take the one with smallest fee
    # our list is sorted so the next element should be bigger in distance and smaller in fee to be a candidate
    if fee < current_fee and dist != current_dist:
        optimum_course_centers.append((dist, fee))
        current_dist = dist
        current_fee = fee

print("OPTIMUM COURSE CENTERS")
print(optimum_course_centers)
print("Count of course centers: ", len(optimum_course_centers))

print("\n--- Method 1 -O(nlgn)-: %s seconds ---" % (time.time() - start_time))






 
