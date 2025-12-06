def bubble_sort(arr):
    steps = []
    a = arr.copy()

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
            steps.append(a.copy())  # record each step
    return steps
