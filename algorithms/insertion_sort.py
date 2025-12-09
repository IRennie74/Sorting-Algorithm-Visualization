def insertion_sort_steps(arr):
    steps = []
    a = arr.copy()

    # Initial state
    steps.append({
        "array": a.copy(),
        "action": "start",
        "compare": None,
        "swapped": None,
        "swapped_indices": None,
        "key": None
    })

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Show initial comparison (inserting key)
        steps.append({
            "array": a.copy(),
            "action": "compare",
            "compare": (i, j),
            "swapped": False,
            "swapped_indices": None,
            "key": key
        })

        moved = False
        while j >= 0 and a[j] > key:
            # Shift element right
            a[j + 1] = a[j]
            moved = True
            steps.append({
                "array": a.copy(),
                "action": "shift",
                "compare": (j, j+1),
                "swapped": True,
                "swapped_indices": (j, j+1),
                "key": key
            })
            j -= 1

        # Insert the key back
        a[j + 1] = key
        steps.append({
            "array": a.copy(),
            "action": "insert",
            "compare": None,
            "swapped": moved,
            "swapped_indices": (j+1, i) if moved else None,
            "key": key
        })

    # Final state
    steps.append({
        "array": a.copy(),
        "action": "done",
        "compare": None,
        "swapped": None,
        "swapped_indices": None,
        "key": None
    })
    return steps
