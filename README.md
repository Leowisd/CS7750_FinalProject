# CS7750_FinalProject

### Description

The project uses simulated annealing algorithm to make a flight schedule for people from different places going to a same place in a same day and leaving in a same day.

### Language Environment

Python3

### Issues

> optimization.py
>> main functions of this project, including simulated annealing algorithm, calculating cost of solution and so on. 

>test.py
>> the progress of running

>Schedule.txt
>> the flight data file

### How to run 

Under the code folder, open cmd and run

```
py test.py
```

#### Example

##### Input

```
py test.py
```

##### output

```
The schedule cost is  2625

                                             Flight Schedule
                                         The destination is STL
     Name          From    Departure Time    Arrive Time     Price    Departure Time    Arrive Time     Price
                                From Original Place                     Return to Original Place
    Seymour        BOS          13:21           19:13         145          7:21            14:31         145
    Franny         DAL          15:51           19:05         196          7:10            12:09         228
     Zooey         CAK          13:50           19:13         106          7:21            15:24         137
     Walt          MIA          14:31           17:23         191          7:21            14:22         119
     Buddy         LGA          16:59           19:55         141          6:45            9:11          141
      Zeo          IAD          12:47           17:57         113          12:05           16:02         106
```