SIMULATION_TRIALS = 1000

T_DIAL = 6
T_DETECT_BUSY = 3
T_MAX_WAIT = 25
T_END_CALL = 1

def main():
    # generate date
    trials = []
    for i in range(SIMULATION_TRIALS):
        trials.append(simulate_one())
    
    # calculate statistics


def simulate_one():
    '''
    Performs one trial of the simulation and returns w,
    the total time spent by the representative on calling one customer.
    '''
    return 1.0

if __name__ == '__main__':
    main()
