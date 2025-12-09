def selection_sort_steps(arr):
    steps = []
    a = arr.copy()
    n = len(a)

    # Initial state
    steps.append({
        "array": a.copy(),
        "action": "start",
        "compare": None,
        "swapped": None,
        "swapped_indices": None,
        "min_index": None
    })

    for i in range(n):
        min_index = i

        # Compare with remaining elements
        for j in range(i + 1, n):
            steps.append({
                "array": a.copy(),
                "action": "compare",
                "compare": (min_index, j),
                "swapped": False,
                "swapped_indices": None,
                "min_index": min_index
            })

            if a[j] < a[min_index]:
                min_index = j
                steps.append({
                    "array": a.copy(),
                    "action": "select_min",
                    "compare": None,
                    "swapped": False,
                    "swapped_indices": None,
                    "min_index": min_index
                })

        # Swap smallest to front
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            steps.append({
                "array": a.copy(),
                "action": "swap",
                "compare": (i, min_index),
                "swapped": True,
                "swapped_indices": (i, min_index),
                "min_index": min_index
            })
        else:
            steps.append({
                "array": a.copy(),
                "action": "noswap",
                "compare": None,
                "swapped": False,
                "swapped_indices": None,
                "min_index": min_index
            })

    # Final state
    steps.append({
        "array": a.copy(),
        "action": "done",
        "compare": None,
        "swapped": None,
        "swapped_indices": None,
        "min_index": None
    })

    return steps
