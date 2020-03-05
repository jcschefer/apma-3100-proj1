from rng import rng, rvg

SIMULATION_TRIALS = 1000

T_DIAL = 6
T_DETECT_BUSY = 3
T_MAX_WAIT = 25
T_END_CALL = 1

def main():
    # generate date
    trials = []
    for i in range(SIMULATION_TRIALS):
        trials.append(simulate_one_customer())
    
    # calculate statistics


def simulate_one_customer():
    '''
    Performs one trial of the simulation and returns w,
    the total time spent by the representative on calling one customer.
    '''
    time_spent = 0
    for call_attempt in range(4):
        time_spent += T_DIAL 
        customer_available_selector = rng()
        if customer_available_selector < 0.2:
            # customer using the line already
            time_spent += T_DETECT_BUSY
        elif customer_available_selector < 0.5:
            # customer unavailable to answer call
            time_spent += T_MAX_WAIT
        else:
            # customer is available
            time_to_pickup = rvg()
            if time_to_pickup < T_MAX_WAIT:
                # customer picks up, process over
                time_spent += time_to_pickup
                return time_spent
            else:
                # customer took too long and representative hangs up
                time_spent += T_MAX_WAIT

        time_spent += T_END_CALL

    return time_spent


if __name__ == '__main__':
    main()
