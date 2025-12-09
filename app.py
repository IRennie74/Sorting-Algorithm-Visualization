import gradio as gr
import time
import random

from algorithms.bubble_sort import bubble_sort_steps
from algorithms.insertion_sort import insertion_sort_steps
from algorithms.selection_sort import selection_sort_steps
from algorithms.binary_search import binary_search_steps

from utils.visualizer import render_single_step_html

# -------------------------------------------------------
# PAUSE / RESUME CONTROLLER
# -------------------------------------------------------
is_paused = False

def pause_sort():
    global is_paused
    is_paused = True

def resume_sort():
    global is_paused
    is_paused = False

# -------------------------------------------------------
# Sanitized Parsing (HARDENED)
# -------------------------------------------------------
def parse_array(text: str):
    if not text or text.strip() == "":
        raise ValueError("Input array is empty.")

    parts = [p.strip() for p in text.split(",") if p.strip() != ""]

    if len(parts) == 0:
        raise ValueError("No valid numbers found. Enter a comma-separated list like: 4, 6, 1, 8")

    arr = []
    for p in parts:
        if "." in p:
            raise ValueError("Floats are not allowed. Only integers are supported.")
        try:
            val = int(p)
        except:
            raise ValueError(f"Invalid number: {p}")

        if val < 1:
            raise ValueError("Values must be >= 1 (no negatives or zero).")
        if val > 999:
            val = 999  # clamp: safely cap at 999 so bars don’t break CSS

        arr.append(val)

    return arr


def generate_random_array(n):
    # Always generate safe values 1–99
    return [random.randint(1, 99) for _ in range(n)]


# -------------------------------------------------------
# STREAM SORT (HARDENED)
# -------------------------------------------------------
def stream_sort(algo, array_text, speed_ms, search_target, use_random, random_size):
    global is_paused
    is_paused = False

    # Force speed into safe range server-side
    speed_ms = max(30, min(2000, speed_ms))
    delay = speed_ms / 1000.0

    # Safe array building
    if use_random:
        arr = generate_random_array(max(3, min(200, random_size)))
    else:
        try:
            arr = parse_array(array_text)
        except Exception as e:
            yield f"<div style='color:red; font-size:18px;'>Error: {e}</div>"
            return

    # Binary Search = must sort array
    if algo == "Binary Search":
        if search_target is None:
            yield "<div style='color:red; font-size:18px;'>Binary Search requires a target number.</div>"
            return

        # Block floats, zero, negative, huge target
        try:
            search_target = int(search_target)
            if search_target < 1:
                raise ValueError
        except:
            yield "<div style='color:red; font-size:18px;'>Binary Search target must be a positive integer.</div>"
            return

        arr = sorted(arr)  # visual + logical consistency
        steps = binary_search_steps(arr, search_target)

    # Sorting algorithms
    elif algo == "Bubble Sort":
        steps = bubble_sort_steps(arr)
    elif algo == "Insertion Sort":
        steps = insertion_sort_steps(arr)
    elif algo == "Selection Sort":
        steps = selection_sort_steps(arr)
    else:
        yield "<div style='color:red;'>Unknown algorithm.</div>"
        return

    # Stream steps safely
    for i, step in enumerate(steps):
        while is_paused:
            time.sleep(0.05)
        yield render_single_step_html(step, i)
        time.sleep(delay)


# -------------------------------------------------------
# UI
# -------------------------------------------------------
with gr.Blocks(title="Sorting/Searching Visualization") as demo:

    gr.Markdown("# 🔍 Algorithm Visualizer (Real-Time, Safe & Hardened)")
    gr.Markdown("Enter only positive integers. Random arrays are auto-sanitized.")

    with gr.Row():
        algo_dd = gr.Dropdown(
            label="Algorithm",
            choices=["Bubble Sort", "Insertion Sort", "Selection Sort", "Binary Search"],
            value="Bubble Sort"
        )
        use_random = gr.Checkbox(label="Use random array", value=False)
        random_size = gr.Slider(label="Random array size", minimum=3, maximum=50, step=1, value=10)
        array_input = gr.Textbox(
            label="Input Array",
            value="8, 3, 7, 4, 9, 1",
            interactive=True
        )
        speed = gr.Slider(
            label="Speed (ms per step)",
            minimum=30,
            maximum=2000,
            step=10,
            value=300
        )

    search_target = gr.Number(
        label="Binary Search Target",
        value=4,
        interactive=True,
        visible=False
    )

    # Auto-update for random mode
    def update_array(use_random_val, size, current_value):
        if use_random_val:
            arr = generate_random_array(max(3, min(200, size)))
            return gr.update(value=", ".join(str(x) for x in arr))
        return gr.update(value=current_value)

    use_random.change(update_array, inputs=[use_random, random_size, array_input], outputs=[array_input])
    random_size.change(update_array, inputs=[use_random, random_size, array_input], outputs=[array_input])

    # Toggle visibility for Binary Search
    def toggle_target(algo_value):
        return gr.update(visible=(algo_value == "Binary Search"))

    algo_dd.change(toggle_target, inputs=[algo_dd], outputs=[search_target])

    run_btn = gr.Button("Run Visualization")

    with gr.Row():
        pause_btn = gr.Button("Pause")
        resume_btn = gr.Button("Resume")

    pause_btn.click(pause_sort, inputs=None, outputs=None)
    resume_btn.click(resume_sort, inputs=None, outputs=None)

    output = gr.HTML(label="Visualization")

    run_btn.click(
        stream_sort,
        inputs=[algo_dd, array_input, speed, search_target, use_random, random_size],
        outputs=[output]
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=None)
