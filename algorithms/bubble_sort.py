"""
Bubble sort that records each step in a simple format,
suitable for HTML-based visualization.
Includes early-exit optimization.
"""

def bubble_sort_steps(arr):
    a = list(arr)
    steps = []

    # Initial state
    steps.append({"array": a.copy(), "compare": None, "swapped": None})

    n = len(a)
    for i in range(n):

        swapped_any = False

        for j in range(0, n - i - 1):

            # Compare these two indices
            steps.append({
                "array": a.copy(),
                "compare": (j, j + 1),
                "swapped": False
            })

            # Swap if needed
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped_any = True

                steps.append({
                    "array": a.copy(),
                    "compare": (j, j + 1),
                    "swapped": True
                })

        # End of one full pass
        steps.append({
            "array": a.copy(),
            "compare": None,
            "swapped": swapped_any
        })

        # EARLY EXIT — no swaps in this full pass
        if not swapped_any:
            steps.append({
                "array": a.copy(),
                "compare": None,
                "swapped": "early_exit"
            })
            break

    # Final state
    steps.append({"array": a.copy(), "compare": None, "swapped": False})
    return steps
