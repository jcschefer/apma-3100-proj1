import random

def rng():
    # TODO implmenent rng instead of using the library
    return random.random()

def rvg():
    # TODO implmenent rvg
    return 0.5


if __name__ == '__main__':
    '''
    Do testing relating to expected first three terms, then print out the required terms.
    '''
    random_nums = [rng() for i in range(55)]
    assert abs(random_nums[0] - 0.6779) < 0.0001, 'First term ({}) incorrect'.format(random_nums[0])
    assert abs(random_nums[1] - 0.1701) < 0.0001, 'Second term ({}) incorrect'.format(random_nums[1])
    assert abs(random_nums[2] - 0.5096) < 0.0001, 'Third term ({}) incorrect'.format(random_nums[2])

    print('u_51:', random_nums[50]) # index is one lower because of zero based indexing
    print('u_52:', random_nums[51])
    print('u_53:', random_nums[52])
