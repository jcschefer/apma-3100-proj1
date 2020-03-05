from rng import rng, rvg

SIMULATION_TRIALS = 1000

T_DIAL = 6
T_DETECT_BUSY = 3
T_MAX_WAIT = 25
T_END_CALL = 1

w5 = 50
w6 = 60
w7 = 70

def main():
    # generate date
    trials = []
    for i in range(SIMULATION_TRIALS):
        trials.append(simulate_one_customer())
    
    # calculate statistics
    trials.sort()
    print('average:\t', sum(trials) / SIMULATION_TRIALS)
    print('median:\t\t', trials[SIMULATION_TRIALS // 2])
    print('25% quart:\t', trials[1 * SIMULATION_TRIALS // 4])
    print('75% quart:\t', trials[3 * SIMULATION_TRIALS // 4])

    print('P[W <= 15]:\t', sum(1 if trial <= 15 else 0 for trial in trials) / SIMULATION_TRIALS)
    print('P[W <= 20]:\t', sum(1 if trial <= 20 else 0 for trial in trials) / SIMULATION_TRIALS)
    print('P[W <= 30]:\t', sum(1 if trial <= 30 else 0 for trial in trials) / SIMULATION_TRIALS)
    print('P[W >  40]:\t', sum(1 if trial >  40 else 0 for trial in trials) / SIMULATION_TRIALS)

    print()
    print('TODO figure out w5, w6, w7')
    print('P[W >  w5]:\t', sum(1 if trial > w5 else 0 for trial in trials) / SIMULATION_TRIALS)
    print('P[W >  w6]:\t', sum(1 if trial > w6 else 0 for trial in trials) / SIMULATION_TRIALS)
    print('P[W >  w7]:\t', sum(1 if trial > w7 else 0 for trial in trials) / SIMULATION_TRIALS)


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
