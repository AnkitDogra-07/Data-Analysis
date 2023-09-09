import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Objective Functions

def rosenbrock(x, y):
    return 100 * (y - x**2)**2 + (1 - x)**2

def sphere(x, y):
    return x**2 + y**2

def ackley(x, y):
    return -20 * np.exp(-0.2 * np.sqrt(x**2 + y**2) / 2) - np.exp((np.cos(2*np.pi*x) + np.cos(2*np.pi*y)) / 2) + 20 + np.exp(1)

def beale(x, y):
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

def michalewicz(x, y):
    m = 10
    return -np.sin(x) * np.sin(1 * x**2 / np.pi)**(2*m) - np.sin(y) * np.sin(2 * y**2 / np.pi)**(2*m)

# Hill Climbing Algorithm

def hillclimbing(objective, bounds, n_iterations, step_size):
    # generate an initial point
    solution = np.array([bounds[i, 0] + np.random.rand() * (bounds[i, 1] - bounds[i, 0]) for i in range(bounds.shape[0])])
    # evaluate the initial point
    solution_eval = objective(*solution)
    # store the path taken by the hill climbing algorithm
    path = [solution]
    # run the hill climb
    for i in range(n_iterations):
        # take a step
        candidate = solution + np.random.randn(len(bounds)) * step_size
        # clip candidate values to be within bounds
        candidate = np.clip(candidate, bounds[:, 0], bounds[:, 1])
        # evaluate candidate point
        candidate_eval = objective(*candidate)
        # check if we should keep the new point
        if candidate_eval <= solution_eval:
            # store the new point
            solution, solution_eval = candidate, candidate_eval
            # add the new point to the path
            path.append(solution)
            # report progress
            print(f'>{i}, f({solution}) = {solution_eval}')
    return solution, solution_eval, path

# Plotting the Objective Function Landscape

def plot_objective_landscape(objective, bounds):
    x = np.linspace(bounds[0, 0], bounds[0, 1], 100)
    y = np.linspace(bounds[1, 0], bounds[1, 1], 100)
    X, Y = np.meshgrid(x, y)
    Z = objective(X, Y)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Objective Value')
    ax.set_title('Objective Function Landscape')

    plt.show()

# Example Usage

np.random.seed(5)

# Define range for input (bounds for each variable separately)
bounds = np.array([[-5.0, 5.0], [-5.0, 5.0]])

# Define the total iterations
n_iterations = 1000

# Define the maximum step size
step_size = 0.1

# Perform the hill climbing search for different objective functions
print("Rosenbrock Function:")
best, score, path = hillclimbing(rosenbrock, bounds, n_iterations, step_size)
print(f'Best solution: {best}')
print(f'Objective value at best solution: {score}')
plot_objective_landscape(rosenbrock, bounds)

print("\nSphere Function:")
best, score, path = hillclimbing(sphere, bounds, n_iterations, step_size)
print(f'Best solution: {best}')
print(f'Objective value at best solution: {score}')
plot_objective_landscape(sphere, bounds)

print("\nAckley Function:")
best, score, path = hillclimbing(ackley, bounds, n_iterations, step_size)
print(f'Best solution: {best}')
print(f'Objective value at best solution: {score}')
plot_objective_landscape(ackley, bounds)

print("\nBeale Function:")
best, score, path = hillclimbing(beale, bounds, n_iterations, step_size)
print(f'Best solution: {best}')
print(f'Objective value at best solution: {score}')
plot_objective_landscape(beale, bounds)

print("\nMichalewicz Function:")
best, score, path = hillclimbing(michalewicz, bounds, n_iterations, step_size)
print(f'Best solution: {best}')
print(f'Objective value at best solution: {score}')
plot_objective_landscape(michalewicz, bounds)
