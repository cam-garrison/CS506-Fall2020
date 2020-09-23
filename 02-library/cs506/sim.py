error_msg = "There is an error in input."


## NOTE: Used the pull request from RC-88 to make this file - all credit goes to them.
## Was implementing the kmeans file and wasn't sure if that would be dependent on this one.
## so I used their implementations. Only difference made was creating the error msg as a constant.


def euclidean_dist(x, y):
    if x == [] and y == []:
        return error_msg
    elif len(x) > len(y) or len(x) < len(y):
        return error_msg
    else:
        distancesum = 0

        for i in range(len(x)):
            distancesum += (x[i] - y[i]) ** 2

        d = distancesum ** (1 / 2)
        return d


def manhattan_dist(x, y):
    if x == [] and y == []:
        return error_msg
    elif len(x) > len(y) or len(x) < len(y):
        return error_msg
    else:
        d = 0

        for i in range(len(x)):
            d += abs(x[i] - y[i])

        return d


def jaccard_dist(x, y):
    if x == [] and y == []:
        return error_msg
    else:
        intersection = len(list(set(x).intersection(y)))
        union = len(list(set(x).union(y)))
        d = 1 - float(intersection / union)
        return d


def cosine_sim(x, y):
    if x == [] and y == []:
        return error_msg
    elif len(x) > len(y) or len(x) < len(y):
        return error_msg
    else:
        sumxx = 0
        sumyy = 0
        sumxy = 0

        for i in range(len(x)):
            sumxx += x[i] * x[i]
            sumyy += y[i] * y[i]
            sumxy += x[i] * y[i]

        d = sumxy / (sumxx * sumyy) ** (1 / 2)
        return d
