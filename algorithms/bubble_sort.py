"""
Bubble sort that records each step in a simple format,
suitable for HTML-based visualization.
"""

def bubble_sort_steps(arr):
    a = list(arr)
    steps = []

    steps.append({"array": a.copy(), "compare": None, "swapped": None})

    n = len(a)
    for i in range(n):
        swapped_any = False

        for j in range(0, n - i - 1):
            steps.append({"array": a.copy(), "compare": (j, j+1), "swapped": False})

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped_any = True
                steps.append({"array": a.copy(), "compare": (j, j+1), "swapped": True})

        steps.append({"array": a.copy(), "compare": None, "swapped": swapped_any})

        if not swapped_any:
            break

    steps.append({"array": a.copy(), "compare": None, "swapped": False})
    return steps
