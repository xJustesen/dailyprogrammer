import random  # for random number generation
import multiprocessing as mp  # for parallel for loop


def CountPointsInsideCircle(samples, output):
    ''' Given a number of samples, this function computes counts how many point lie within a circle
    of radius 1 in a square with side length 1. '''
    inside_circle = 0
    random.seed()
    for _ in range(samples):
        random_x = random.uniform(0.0, 1.0)
        random_y = random.uniform(0.0, 1.0)
        if random_x**2 + random_y**2 <= 1:
            inside_circle += 1
    output.put(inside_circle)


def CountPointsInsideSphere(samples, output):
    ''' Given a number of samples, this function computes counts how many point lie within a sphere
    of radius 1 in a square box with side length 1. '''
    inside_sphere = 0
    random.seed()
    for _ in range(samples):
        random_x = random.uniform(0.0, 1.0)
        random_y = random.uniform(0.0, 1.0)
        random_z = random.uniform(0.0, 1.0)
        if random_x**2 + random_y**2 + random_z**2 <= 1:
            inside_sphere += 1
    output.put(inside_sphere)


def main(geometry='circle', input_samples=1e6):
    '''  Estimate pi by counting points inside a quarter-circle or a quarter-sphere. '''
    output = mp.Queue()
    number_of_samples = int(input_samples)
    number_of_processes = 8
    total_samples = number_of_processes * number_of_samples

    if geometry == 'circle':
        processes = [mp.Process(target=CountPointsInsideCircle, args=(number_of_samples, output))
                     for i in range(number_of_processes)]
    else:
        processes = [mp.Process(target=CountPointsInsideSphere, args=(number_of_samples, output))
                     for i in range(number_of_processes)]

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()

    # Count total number of points inside
    total_counts_inside = 0
    for p in processes:
        total_counts_inside += output.get()

    # Estimate pi
    if geometry == 'circle':
        mc_pi = 4.0 * total_counts_inside / total_samples
    else:
        mc_pi = 6.0 * total_counts_inside / total_samples

    print('Used a {:s} to estimate pi as {:f} using {:d} samples.'.format(
        geometry, mc_pi, total_samples))


if __name__ == '__main__':
    give_input = input(
        "Do you want to specify input (yes/no)?\n")
    if give_input == 'yes':
        while (True):
            type_input = input(
                "Type 'circle' to use circle or 'sphere' to use sphere:\n")
            if (type_input == 'circle' or type_input == 'sphere'):
                break
            print('Illegal input given!')
        samples_input = input("Input number of samples:\n")
        main(type_input, samples_input)
    else:
        main()
