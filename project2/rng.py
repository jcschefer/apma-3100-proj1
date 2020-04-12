import random
import math

rng_x = 1000
rng_a = 24693
rng_c = 3967
rng_K = 2 ** 17

def rng():
    '''
    samples a uniform random variable between 0 and 1 using the linear congruential thingy
    '''
    global rng_x
    rng_x = (rng_a * rng_x + rng_c) % rng_K
    return rng_x / rng_K

rayleigh_a = 1 / 57

def generate_sample_of_x():
    '''
    F_x(x) = 1 - e^(-1/2 * a^2 * x^2)
    therefore, compute the inverse as
    F^(-1)_x(x) = 1/a * sqrt(-2 * log(1 - x))
    '''
    uniform_random_sample = rng()
    return 1 / rayleigh_a * math.sqrt(-2 * math.log(1 - uniform_random_sample))


if __name__ == '__main__':
    '''
    Do testing related to expected first three terms, then print out the required terms.
    '''
    expected_first_terms = [0.4229, 0.8226, 0.6550]
    random_nums = [rng() for i in range(55)]
    assert abs(random_nums[0] - expected_first_terms[0]) < 0.0001, 'First term ({}) incorrect'.format(random_nums[0])
    assert abs(random_nums[1] - expected_first_terms[1]) < 0.0001, 'Second term ({}) incorrect'.format(random_nums[1])
    assert abs(random_nums[2] - expected_first_terms[2]) < 0.0001, 'Third term ({}) incorrect'.format(random_nums[2])

    print('assertions on first three terms passed')

    print('u_51:', random_nums[50]) # index is one lower because of zero based indexing
    print('u_52:', random_nums[51])
    print('u_53:', random_nums[52])

    try:
        N_POINTS = 10000
        import matplotlib.pyplot as plt
        exponential_trials = [generate_sample_of_x() for i in range(N_POINTS)]

        max_x = int(1 + max(exponential_trials))
        plot_x = [i*max_x/N_POINTS for i in range(N_POINTS)]
        uniform_trials = [rng() for i in range(N_POINTS)]
        plot_u = []

        for x_val in plot_x:
            plot_u.append(sum(1 if trial <= x_val else 0 for trial in exponential_trials) / N_POINTS)

        plt.plot(plot_x, plot_u)
        plt.title('CDF of X, a Rayleigh Random Variable')
        plt.xlabel('x')
        plt.ylabel('CDF of X: P[x < X]')
        plt.show()
    except ImportError:
        print('you don\'t have matplotlib :( can\'t graph the CDF')
