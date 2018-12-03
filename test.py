import optimization

for i in range(100):

    # domain: the range of each value in the solution, the range is decided on how many choices of each pair of two places can be choosed 
    domain=[(0,3)]*(len(optimization.people)*2)

    # run the optimization
    s=optimization.annealingoptimize(domain,optimization.schedulecost)

    # print the cost of final solution
    # print('The schedule cost is ',optimization.schedulecost(s))
    print(optimization.schedulecost(s))
    # print()
    
    # print the final solution
    # optimization.printschedule(s)
