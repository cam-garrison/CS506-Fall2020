from collections import defaultdict
from math import inf
import random
import csv

## NOTE: have implemented all but the cost function and the generate k++ function.
## NOTE: was unsure how to implement those without the lecture slides.


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)

    Returns a new point which is the center of all the points.
    """
    num_points = len(points)
    num_dims = len(points[0])
    avg = [0 for _ in range(num_dims)]  # initializing return value
    for dim in range(num_dims):  # looping thru dimensions
        dim_avg = 0  # initializing each dim value to avg
        for pt in points:  # looping thru each point
            dim_avg += pt[dim]  # adding each point to avg for that dim
        dim_avg = dim_avg / num_points
        avg[dim] = dim_avg
    return avg


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    new_ctrs = []
    for assignment in assignments:
        point_list = []
        for idx in assignment:
            point_list.append(dataset[idx])
        new_ctr = point_avg(point_list)
        new_ctrs.append(new_ctr)
    return new_ctrs


def assign_points(data_points, centers):
    """
    assign points to a cluster based on a list of center points
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    return the euchlidian distance b/w two points
    """
    if len(a) != len(b):
        raise ValueError("Error! lengths must be equal")
    result = sum([abs(a[i] - b[i]) ** 2 for i in range(len(a))]) ** (1 / 2)
    return result


def distance_squared(a, b):
    return distance(a, b) ** 2


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k)


def cost_function(clustering):
    raise NotImplementedError()


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    raise NotImplementedError()


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset) + 1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset) + 1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
