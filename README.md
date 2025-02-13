# Materials for the course "Fundamentals of Statistics with Python" for O'Reilly by Dr. Chester Ismay

# Course content

The major files in this repository are
- `slides_2025-02.pdf`: PDF version of the slides used in this course to motivate the code.
- `data_dev_survey.csv`: Data for code walkthroughs.
- `coffee_quality.csv`: Data for student exercises.
- `exercises.ipynb`: A Jupyter Notebook with pseudocode/instructions provide to be filled in for code walkthroughs and student exercises
- `exercises_solutions.ipynb`: A Jupyter Notebook with answers to the code walkthroughs and exercises. 

## Recommended instructions on getting set up with Python and Jupyter Notebook

If you aren't able to do this on your machine, you may want to check out [Google Colab](https://colab.research.google.com/). 
It's a free service that allows you to run Jupyter notebooks in the cloud. 
Alternatively, I've set up some temporary notebooks on Binder ([here](https://mybinder.org/v2/gh/ismayc/oreilly-fundamentals-of-statistics-with-python/main?urlpath=%2Fdoc%2Ftree%2Fexercises.ipynb) that you can work with online as well.

### Step 1: Install Python
- **Option 1: Anaconda Installation**:
  - **Download Anaconda**: Go to the [official Anaconda website](https://www.anaconda.com/products/distribution) and download the latest version of Anaconda for your operating system (Windows, macOS, or Linux). Anaconda conveniently installs Python, Jupyter Notebook, and many other commonly used packages for data science and machine learning.
- **Option 2: Python Installation**:
  - **Download Python**: Alternatively, you can download Python directly from the [official Python website](https://www.python.org/downloads/) and install the latest version for your operating system.

### Step 2: Launch Jupyter Notebook
- **Launch Jupyter Notebook**:
  - **Anaconda**: After installing Anaconda, open Anaconda Navigator from your Start Menu (Windows) or using the Anaconda Navigator application (macOS/Linux). In Anaconda Navigator, find Jupyter Notebook in the list of available applications and click on the "Launch" button. This will open Jupyter Notebook in your default web browser.
  - **Python Installation**: Open your command prompt (Windows) or terminal (macOS/Linux), and install Jupyter using pip:
    ```bash
    pip install notebook
    ```

### Step 3: Install Required Libraries
- **Open Anaconda Prompt (Windows) or Terminal (macOS/Linux)** (if using Anaconda), or **open your command prompt (Windows) or terminal (macOS/Linux)** (if using Python installation).
- **Install Required Libraries using conda (Anaconda)**:
   ```bash
   conda install numpy pandas scipy matplotlib seaborn statsmodels scikit-learn
   ```
- **Install Required Libraries using pip** (if not using Anaconda):
  ```bash
  pip install numpy pandas scipy matplotlib seaborn statsmodels scikit-learn
  ```

### Step 4: Launch Jupyter Notebook
- **Open your command prompt or terminal**.
- **Run Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
   This command will open Jupyter Notebook in your default web browser.

### Step 5: Verify Installation
- **Create a new notebook**: In the Jupyter Notebook interface, click on "New" and select "Python 3" to open a new notebook.
- **Test the installation of the libraries**:
   - Import the libraries in the first cell of your notebook:
     ```python
     import numpy as np
     import pandas as pd
     import scipy.stats as stats
     import matplotlib.pyplot as plt
     import seaborn as sns
     import statsmodels.api as sm
     ```
   - Run the cell (`Shift + Enter`). If no errors appear, the libraries are installed correctly.

### Additional Tips
- **Troubleshooting**: If you encounter any errors during installation, make sure that your pip is up to date (`pip install --upgrade pip`) and try the installation commands again. If issues persist, check for specific error messages online for troubleshooting tips.
- **Learning Resources**: Familiarize yourself with the Jupyter Notebook interface and basic functionality by reading tutorials or watching introductory videos about Jupyter Notebooks.
