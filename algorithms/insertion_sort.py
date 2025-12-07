"""
Insertion sort step-by-step for visualization.
"""

def insertion_sort_steps(arr):
    steps = []
    a = arr.copy()

    steps.append({"array": a.copy(), "compare": None, "swapped": None, "swapped_indices": None})

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Show initial comparison (inserting key)
        steps.append({"array": a.copy(), "compare": (i, j), "swapped": False, "swapped_indices": None})

        # Move elements one by one
        while j >= 0 and a[j] > key:

            # Swap-like shift (visualizing the movement)
            a[j + 1] = a[j]

            steps.append({
                "array": a.copy(),
                "compare": (j, j+1),
                "swapped": True,
                "swapped_indices": (j, j+1)
            })

            j -= 1

        # Insert the key back
        a[j + 1] = key
        steps.append({
            "array": a.copy(),
            "compare": None,
            "swapped": True,
            "swapped_indices": (j+1, i)
        })

    steps.append({"array": a.copy(), "compare": None, "swapped": None, "swapped_indices": None})
    return steps
