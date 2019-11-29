def checkInput(rate, n):
    N = len(rate)
    k = len(rate[0])
    assert all(len(rate[i]) == k for i in range(k)), "Row length != #categories)"
    assert all(isinstance(int(rate[i][j]), int) for i in range(N) for j in range(k)), "Element not integer"
    assert all(sum(row) == n for row in rate), "Sum of ratings != #raters)"


def kappa_data(reliability_data):
    global final_list, noted_samples
    final_list = []
    noted_samples = 0
    for item in reliability_data.transpose():
        temp_list = [0] * (reliability_data.max() + 1)
        for i in item:
            for j in range(len(temp_list)):
                if i == j + 1:
                    temp_list[j] = temp_list[j] + 1
        if sum(temp_list) == 5:  # only a few (around 200 out of 10000) are excluded
            final_list.append(temp_list)
            noted_samples += 1
    return final_list, noted_samples


def fleissKappa(reliability_data, n):
    rate, noted_samples = kappa_data(reliability_data)
    print("Skipped subjects: {}%".format(
        round(((reliability_data.shape[1] - noted_samples) / reliability_data.shape[1]) * 100, 4)))
    N = len(rate)
    k = len(rate[0])
    print("#raters = ", n, ", #subjects = ", N, ", #categories = ", k)
    checkInput(rate, n)
    # mean of the extent to which raters agree for the ith subject
    PA = sum([(sum([i ** 2 for i in row]) - n) / (n * (n - 1)) for row in rate]) / N
    print("PA = ", PA)
    # mean of squares of proportion of all assignments which were to jth category
    PE = sum([j ** 2 for j in [sum([rows[i] for rows in rate]) / (N * n) for i in range(k)]])
    print("PE =", PE)
    kappa = -float("inf")
    try:
        kappa = (PA - PE) / (1 - PE)
        kappa = float("{:.3f}".format(kappa))
    except ZeroDivisionError:
        print("Expected agreement = 1")
    print("Fleiss' Kappa =", kappa)
    return kappa
