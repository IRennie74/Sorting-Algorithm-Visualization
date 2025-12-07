"""
Selection sort step-by-step for visualization.
"""

def selection_sort_steps(arr):
    steps = []
    a = arr.copy()

    n = len(a)
    steps.append({"array": a.copy(), "compare": None, "swapped": None, "swapped_indices": None})

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            # Comparing current j with min
            steps.append({
                "array": a.copy(),
                "compare": (min_index, j),
                "swapped": False,
                "swapped_indices": None
            })

            if a[j] < a[min_index]:
                min_index = j

        # Swap smallest to front
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            steps.append({
                "array": a.copy(),
                "compare": (i, min_index),
                "swapped": True,
                "swapped_indices": (i, min_index)
            })
        else:
            # No swap
            steps.append({
                "array": a.copy(),
                "compare": None,
                "swapped": False,
                "swapped_indices": None
            })

    steps.append({"array": a.copy(), "compare": None, "swapped": None, "swapped_indices": None})
    return steps
