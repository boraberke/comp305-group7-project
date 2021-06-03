# COMP 305 Group 7 Project: Which Course Center Should I Select?
This is a group project for "COMP305: Algorithms and Complexity" class.
\
*Copyright © 2021 Dream Team™ - All Rights Reserved*
>*Ahmet Talha Akgül (68631)* \
>*Bora Berke Şahin (64060)*\
>*Pınar Erbil (68904)*\
>*Ufkun Özalp (69222)*

\
The main purpose of us in this project is to find a subset of incomperable nodes in terms of 2 attributes (distance and price) from a large set. We came up with 3 applicable and non-brute-force solutions which all have relatively small time complexities. The best algorithm we found (method 2) has O(n) time complexity.

### Method 1: Sort and Compare ##
**Time Complexity:** O(nlgn)

### Method 2: The Best Solution ##
**Time Complexity:** O(n)

### Method 3: Convex Hull -A Promising Alternative Algorithm- ##
**Time Complexity:** O(nlgn)

## Test Results and Runtimes for Method 1 and Method 2: ##
### Output for Test 1 file:
```python
OPTIMUM COURSE CENTERS
[(3, 4), (4, 3)]
Count of course centers:  2

--- Method 1 -O(nlgn)-: 0.002992391586303711 seconds ---

OPTIMUM COURSE CENTERS
[(4.0, 3), (3.0, 4)]
Count of course centers:  2

--- Method 2 -O(n)-: 0.0019943714141845703 seconds ---
```
### Output for Test 2 file:
```python
OPTIMUM COURSE CENTERS
[(10, 244), (12, 213), (19, 203), (36, 201), (51, 200)]
Count of course centers:  5

--- Method 1 -O(nlgn)-: 0.0029935836791992188 seconds ---

OPTIMUM COURSE CENTERS
[(51.0, 200), (36.0, 201), (19.0, 203), (12.0, 213), (10.0, 244)]
Count of course centers:  5

--- Method 2 -O(n)-: 0.0029904842376708984 seconds ---
```
### Output for Test 3 file:
```python
OPTIMUM COURSE CENTERS
[(20, 5614), (73, 4466), (90, 4287), (194, 4094), (405, 4090), (479, 4049), (658, 4041), (1619, 4031), (2611, 4013), (3735, 4009), (5860, 4001), (27933, 4000)]
Count of course centers:  12

--- Method 1 -O(nlgn)-: 0.19248557090759277 seconds ---

OPTIMUM COURSE CENTERS
[(27933.0, 4000), (5860.0, 4001), (3735.0, 4009), (2611.0, 4013), (1619.0, 4031), (658.0, 4041), (479.0, 4049), (405.0, 4090), (194.0, 4094), (90.0, 4287), (73.0, 4466), (20.0, 5614)]
Count of course centers:  12

--- Method 2 -O(n)-: 0.18450212478637695 seconds ---
```
### Output for Test 4 file:
```python
OPTIMUM COURSE CENTERS
[(12, 450819), (40, 412679), (52, 411748), (491, 405911), (1370, 403619), (1634, 401268), (3021, 400625), (5497, 400311), (25825, 400073), (73317, 400063), (175280, 400014), (615134, 400001)]
Count of course centers:  12
--- Method 1 -O(nlgn)-: 15.566096782684326 seconds ---

OPTIMUM COURSE CENTERS
[(615134.0, 400001), (175280.0, 400014), (73317.0, 400063), (25825.0, 400073), (5497.0, 400311), (3021.0, 400625), (1634.0, 401268), (1370.0, 403619), (491.0, 405911), (52.0, 411748), (40.0, 412679), (12.0, 450819)]
Count of course centers:  12

--- Method 2 -O(n)-: 13.906801700592041 seconds ---
```


## Test Files Google Drive Link: ##
https://drive.google.com/drive/u/1/folders/1TvGT8m2oo_83gGW3SNLJsdN8j6C_YuQv

## Project Journal: ##
### Date: 13.05.2021 Thursday ###
In the first meeting, we tried to analyze the problem. We came up with a non-brute-force implementation idea which is based on sorting (Method 1) and therefore due to the cost of sorting algorithms, its time complexity is O(nlgn).

### Date: 14.05.2021 Friday ###
In the second meeting, we tried to find alternative solutions to the one we came up yesterday. The main goal was to come up with an algorithm which does not require sorting process so that we can reduce the time complexity to O(sqrt(n)), O(n) or O(lgn). We came up with "Convex Hull" implementation idea which does not require sorting but based on the nodes on the outter boundaries of convex hull. However, even though this idea is independent from sorting algorithms, due to the nature of convex hull implementation, time complexity of the new algorithm remanins O(nlgn).

### Date: 16.05.2021 Saturday ###

In the third meeting, we stil tried to find a better solution, in other words, find a better algorithm which has smaller time complexity. As we realized yesterday, the main obstacle that we faced is sorting obligation. So, we asked ourselves "what if we select the nodes we want and put them in a list while reading from the file, instead of sorting afterwards?". In the light of this question, we came up with our the latest implementation, method 2 which has O(n) time complexity. Furthermore, we also did our best to reduce such complexity even more (O(sqrt(n)),O(lgn),etc), by using divide and conquer methods. If we would have already sorted list, or information about minimum and maximum distances and fees in the list, It would be possible to decrease the time complexity even more. 
