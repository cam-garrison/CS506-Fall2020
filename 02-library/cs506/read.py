import re


def read_csv(csv_file_path):
    """
    Given a path to a csv file, return a matrix (list of lists)
    in row major.
    """
    result = []
    # open files
    with open(csv_file_path, "r") as f:
        content = f.readlines()
        for line in content:
            line = line.split(",")
            for i in range(len(line)):
                line[i] = eval(line[i])
            result.append(line)
    return result
