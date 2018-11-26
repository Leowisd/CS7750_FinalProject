import time
import random
import math
import fileinput

# Passanger infomation
people = [('Seymour','BOS'),
          ('Franny','DAL'),
          ('Zooey','CAK'),
          ('Walt','MIA'),
          ('Buddy','LGA'),
          ('Zeo','IAD')]
# Lambert St. Louis
destination='STL'
# Saving flights infomation in a dictionary
flights={}
for line in open('Schedule.txt'):
  origin,dest,depart,arrive,price=line.strip().split(',')
  flights.setdefault((origin,dest),[])

  # Add details to the list of possible flights
  flights[(origin,dest)].append((depart,arrive,int(price)))

# =========================================================================================
# Fcuntion: caculating flight time
# =========================================================================================
def getminutes(t):
  x=time.strptime(t,'%H:%M')
  return x[3]*60+x[4]

# =========================================================================================
# Fcuntion: print out the schedule list
# =========================================================================================
def printschedule(r):
  print('{:^105}'.format('Flight Schedule'))
  print('{:^105}'.format('The destination is '+ destination))
  print('{:^15s} {:^10s} {:^15s} {:^15s} {:^10s} {:^15s} {:^15s} {:^10s}'.format('Name','From','Departure Time','Arrive Time','Price','Departure Time','Arrive Time','Price'))
  print('{:^15s} {:^10s} {:^30s} {:^10s} {:^30s} {:^10s}'.format('','','From Original Place','','Return to Original Place',''))
  for d in range(len(r)//2):
    name=people[d][0]
    origin=people[d][1]
    out=flights[(origin,destination)][int(r[2*d])]
    ret=flights[(destination,origin)][int(r[2*d+1])]
    print('{:^15} {:^10} {:^15} {:^15} {:^10} {:^15} {:^15} {:^10}'.format(name,origin,out[0],out[1],out[2],ret[0],ret[1],ret[2]))

# =========================================================================================
# Function: caculating the cost of one solution
# =========================================================================================
def schedulecost(sol):
  totalprice=0
  latestarrival=0
  earliestdep=24*60
    
  for d in range(len(sol)//2):
    # Get the inbound and outbound flights
    origin=people[d][1]
    outbound=flights[(origin,destination)][int(sol[2*d])]
    returnf=flights[(destination,origin)][int(sol[2*d+1])]

    # Total price is the price of all outbound and return flights
    totalprice+=outbound[2]
    totalprice+=returnf[2]

    # Track the latest arrival and earliest departure
    if latestarrival<getminutes(outbound[1]): latestarrival=getminutes(outbound[1])
    if earliestdep>getminutes(returnf[0]): earliestdep=getminutes(returnf[0])

  # Every person must wait at the airport until the latest person arrives.
  # They also must arrive at the same time and wait for their flights.
  totalwait=0  
  for d in range(len(sol)//2):
    origin=people[d][1]
    outbound=flights[(origin,destination)][int(sol[2*d])]
    returnf=flights[(destination,origin)][int(sol[2*d+1])]
    totalwait+=latestarrival-getminutes(outbound[1])
    totalwait+=getminutes(returnf[0])-earliestdep  

  # Does this solution require an extra day of car rental? That'll be more $100!
  if latestarrival<earliestdep: totalprice+=100

  return totalprice+totalwait
 
# ===========================================================================================
# Function: annealing progress
# Args:
#   domain: the range of each value in the solution
#   consf: the function caculating cost
#   T: the initial temperature
#   cool: the speed of annealing
#   step: the step of each optimization
# Returns:
#   vec: the best solution after the optimization
# ===========================================================================================
def annealingoptimize(domain,costf,T=10000.0,cool=0.95,step=1):
  # Initialize the values randomly
  vec=[float(random.randint(domain[i][0],domain[i][1])) 
       for i in range(len(domain))]
  while T>0.1:
    # Choose one of the indices
    i=random.randint(0,len(domain)-1)

    # Choose a direction to change it
    dir=random.randint(-step,step)

    # Create a new list with one of the values changed
    vecb=vec[:]
    vecb[i]+=dir
    if vecb[i]<domain[i][0]: vecb[i]=domain[i][0]
    elif vecb[i]>domain[i][1]: vecb[i]=domain[i][1]

    # Calculate the current cost and the new cost
    ea=costf(vec)
    eb=costf(vecb)
    p=pow(math.e,-(eb-ea)/T)

    # Is it better, or does it make the probability
    # cutoff?
    if (eb<ea or random.random()<p):
      vec=vecb      

    # Decrease the temperature
    T=T*cool
  return vec