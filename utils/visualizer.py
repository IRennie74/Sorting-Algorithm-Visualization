def render_single_step_html(step, idx):
    arr = step["array"]
    compare = step["compare"]
    swapped = step["swapped"]
    swapped_indices = step.get("swapped_indices")

    # Container wrapper (centering)
    html = f"""
    <div style="
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        width:100%;
        margin-top:20px;
        font-family:monospace;
        ">
        <h2 style='margin-bottom:10px;'>Step {idx}</h2>

        <div style="
            display:flex;
            gap:12px;
            padding:20px;
            justify-content:center;
            align-items:flex-end;
            background-color:#1a1a1a;
            border-radius:10px;
            width:90%;
            min-height:250px;
        ">
    """

    # Height multiplier = taller bars
    HEIGHT_MULT = 8  # increase to make bars even taller

    for i, val in enumerate(arr):

        # DEFAULT GRAY
        color = "#777"

        # SWAP takes priority (GREEN)
        if swapped and swapped_indices and (i in swapped_indices):
            color = "#4caf50"

        # COMPARISON (ORANGE)
        elif compare and (i == compare[0] or i == compare[1]):
            color = "#ffa500"

        bar_height = 20 + val * HEIGHT_MULT

        html += f"""
        <div style="
            height:{bar_height}px;
            width:35px;
            background:{color};
            border-radius:6px;
            display:flex;
            align-items:flex-end;
            justify-content:center;
            font-size:12px;
            color:#111;
        ">
            {val}
        </div>
        """

    # close bar container
    html += "</div>"

    # Explanation text under the graph
    if swapped and swapped_indices:
        html += "<div style='color:#4caf50; margin-top:12px; font-size:16px;'>Swap happened</div>"
    elif compare:
        html += f"<div style='color:#ffa500; margin-top:12px; font-size:16px;'>Comparing {compare[0]} and {compare[1]}</div>"
    else:
        html += "<div style='margin-top:12px; font-size:16px;'>Snapshot</div>"

    html += "</div>"  # close outer container

    return html
