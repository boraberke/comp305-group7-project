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

## Method 1: Sort and Compare ##
**Time Complexity:** O(nlgn)

## Method 2: The Best Solution ##
**Time Complexity:** O(n)

## Method 3: Convex Hull -A Promising Alternative Algorithm- ##
**Time Complexity:** O(nlgn)

### Date : 13.05.2021 Thursday ###
In the first meeting, we tried to analyze the problem. We came up with a non-brute-force implementation idea which is based on sorting (Method 1) and therefore due to the cost of sorting algorithms, its time complexity is O(nlgn).

### Date 14.05.2021 Friday ###
In the second meeting, we tried to find alternative solutions to the one we came up yesterday. The main goal was to come up with an algorithm which does not require sorting process so that we can reduce the time complexity to O(sqrt(n)), O(n) or O(lgn). We came up with "Convex Hull" implementation idea which does not require sorting but based on the nodes on the outter boundaries of convex hull. However, even though this idea is independent from sorting algorithms, due to the nature of convex hull implementation, time complexity of the new algorithm remanins O(nlgn).

### Date 16.05.2021: Saturday ###

In the third meeting, we stil tried to find a better solution, in other words, find a better algorithm which has smaller time complexity. As we realized yesterday, the main obstacle that we faced is sorting obligation. So, we asked ourselves "what if we select the nodes we want and put them in a list while reading from the file, instead of sorting afterwards?". In the light of this question, we came up with our the latest implementation, method 2 which has O(n) time complexity. Furthermore, we also did our best to reduce such complexity even more (O(sqrt(n)),O(lgn),etc), by using divide and conquer methods. If we would have already sorted list, or information about minimum and maximum distances and fees in the list, It would be possible to decrease the time complexity even more. 
