---
title: Sorting Algorithm Visualization
emoji: 📊
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
---


# Algorithm Name
Insertion Sort
Includes binary search, bubble sort, insertion sort, and selection sort

## Demo video/gif/screenshot of test
![Demo](assets/screen-capture.gif)

## Problem Breakdown & Computational Thinking (You can add a flowchart and write the four pillars of computational thinking briefly in bullets)
#### Decomposition
- Create sorting algorithm
- Build UI with Gradio
- Create environment and upload to Github and Huggingface
- Managing user inputs, array generation, and playback controls
#### Pattern Recognition
- Repeated comparison in elements
- Swapping or shifting values
- Iterative passes through the list
#### Abstraction
- Representing each array state as a simple list of numbers
- Only returning changes relevant to the visualization (colors, swaps, comparisons)
- Creating generalized visualization functions instead of separate ones for each algorithm
#### Algorithm Design
- Bubble Sort, Insertion Sort, Selection Sort, and Binary Search
- Capturing each meaningful step of the algorithm
- Rendering updates so users can visually follow the algorithm’s process
## Steps to Run
#### Clone the repository
- git clone https://github.com/IRennie74/Sorting-Algorithm-Visualization.git
- cd Sorting-Algorithm-Visualization
#### Create a virtual environment (optional but recommended)
- python -m venv venv
- venv\Scripts\activate
#### Install required dependencies
- pip install -r requirements.txt
#### Run the application
- python app.py
#### Visit the URL printed in the terminal (e.g., http://127.0.0.1:7860/) to use the visualizer.

## Edge Cases
When trying to break the random integers option of the sort, the program will never break. 
You can set the random integer to any number and it limits the parameters automatically so it will always have a usable integer.

Every sorting algorithm has a check for empty lists etc.

Safe against non integer values entered into list.





## Hugging Face Link
https://huggingface.co/spaces/Rennie44/Sorting-Algorithm-Visualization
## Author & Acknowledgment
Level 4 of AI use used.
Full AI assistance permitted, only with explicit instructor approval and full disclosure.
ChatGPT-5 was used during the building of this project.
