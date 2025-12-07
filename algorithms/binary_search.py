"""
Binary search step-by-step visualization.
Visual fields:
- compare: (mid, None)
- swapped: always False
"""

def binary_search_steps(arr, target):
    steps = []
    a = arr.copy()

    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        # Show comparison
        steps.append({
            "array": a.copy(),
            "compare": (mid, None),
            "swapped": False,
            "swapped_indices": None
        })

        if a[mid] == target:
            steps.append({
                "array": a.copy(),
                "compare": (mid, None),
                "swapped": True,
                "swapped_indices": (mid, mid)
            })
            break

        if target < a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Final frame
    steps.append({"array": a.copy(), "compare": None, "swapped": False, "swapped_indices": None})
    return steps
