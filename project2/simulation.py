from rng import generate_sample_of_x

TRIALS_PER_N = 110

def main():
    sample_sizes = [10, 30, 50, 100, 150, 250, 500, 1000]
    print('trial, ', end='')
    print(', '.join('n=' + str(ss) for ss in sample_sizes))
    for i in range(TRIALS_PER_N):
        print(str(i + 1) + ', ', end='')
        print(', '.join(str(round(run_sample_mean_trial(ss), 4)) for ss in sample_sizes))
        

def run_sample_mean_trial(sample_size):
    tot = 0
    for i in range(sample_size):
        tot += generate_sample_of_x()
    return tot / sample_size


if __name__ == '__main__':
    main()
