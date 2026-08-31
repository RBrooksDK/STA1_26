---
tags:
    - Python
    - VS Code
    - Jupyter
    - Pandas
    - NumPy
    - Data
---

<h1 align="center">Getting Started with Python and Data</h1>

This page is **self-study**. There is no classroom session 00. Work through it before Session 01 so that class time can be spent on statistics, not on installing software.

You need three pieces that work together:

1. **Python** from [python.org](https://www.python.org/downloads/) — the program that runs your code.
2. **Visual Studio Code** from [code.visualstudio.com](https://code.visualstudio.com/download) — the editor.
3. The **Python** and **Jupyter** extensions in VS Code — so you can open `.ipynb` notebooks and run cells.

VS Code does not include Python. Install Python first, then the editor, then the extensions. When that works, install the course packages and load a CSV file from `data/`. Complete the installation below before Session 01. Use the section for your operating system, then continue with the shared VS Code and Jupyter steps.

The written steps are the course standard. The videos are optional extra help; follow the text if a video shows a slightly different Python version number.

### 1. Install Python

Download a **current Python 3.12 or newer** from the official site. The big yellow button on [python.org/downloads](https://www.python.org/downloads/) is the right file.

#### Windows

1. Open [python.org/downloads](https://www.python.org/downloads/) and download the Windows installer (64-bit).
2. Run the installer.
3. On the first page, tick **Add python.exe to PATH**. This is the step that usually goes wrong. Do it before you click Install.
4. Click **Install Now** and finish the wizard.
5. Close any terminal that was already open. Open a **new** Command Prompt or PowerShell.
6. Check the install:

```text
py --version
```

You should see a Python 3 version, for example `Python 3.13.5`. The Windows launcher `py` is more reliable than typing `python`, which can still open the Microsoft Store stub.

If `py` is not recognised, re-run the installer, choose **Modify**, and enable **Add python.exe to PATH**. Then open a new terminal and try again.

Do **not** install Python from the Microsoft Store for this course. Use python.org.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://www.youtube.com/embed/jfUMPHJpSdo"
        title="Install Python on Windows from python.org"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

#### macOS

macOS may already have a `python3` command. That system copy is **not** the one we want. Install a current Python from python.org.

1. Open [python.org/downloads](https://www.python.org/downloads/) and download the **macOS 64-bit universal installer**.
2. Open the `.pkg` file and click through Continue, Agree, and Install. Enter your Mac password when asked.
3. When the installer finishes, open the folder it shows. Double-click **Install Certificates.command** and wait until the Terminal window says the process completed. Then double-click **Update Shell Profile.command** if it is there. These two scripts make `pip` and HTTPS downloads work.
4. Quit Terminal completely and open a **new** Terminal window.
5. Check the install:

```text
python3 --version
```

You should see the version you just installed (3.12 or newer), not an old 3.9 leftover.

On a Mac, type `python3` and `pip3`. The command `python` often does nothing useful.

If `python3 --version` still shows an old version, close Terminal and open it again. The installer updates your shell profile only for new windows.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://www.youtube.com/embed/-J0RYcVR3T0"
        title="Install Python on macOS from python.org"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

### 2. Install Visual Studio Code

Download VS Code from [code.visualstudio.com/download](https://code.visualstudio.com/download). Pick the installer for your operating system.

#### Windows

1. Run the installer.
2. Tick **Add to PATH** (and the desktop icon if you want one).
3. Finish, then start VS Code from the Start menu.

#### macOS

1. Open the downloaded `.dmg` file and drag **Visual Studio Code** into **Applications**.
2. Open VS Code from Applications (right-click → Open the first time if macOS warns about an app from the internet).
3. Open the Command Palette with ++cmd+shift+p++ and run **Shell Command: Install 'code' command in PATH**. That lets you type `code .` in Terminal later.

### 3. Install the Python and Jupyter extensions

These steps are the same on Windows and macOS.

1. In VS Code, open Extensions with ++ctrl+shift+x++ (Windows) or ++cmd+shift+x++ (macOS).
2. Search for **Python** and install the extension published by **Microsoft** (`ms-python.python`). It usually offers the Jupyter extension as well.
3. Search for **Jupyter** and install the extension published by **Microsoft** (`ms-toolsai.jupyter`) if it is not already installed.

You now have an editor that can open notebooks. You still need a Python kernel and the course packages.

The video below shows the notebook editor in VS Code (creating a notebook, cells, and running code). Install Python first, as in the sections above, then follow the same clicks in your own VS Code.

The owner has disabled playback on other websites, so the embedded player will not start here. Click **Watch on YouTube** in the player, or open the [video on YouTube](https://www.youtube.com/watch?v=_C0vbLV6WdA) directly.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden;">
    <iframe
        src="https://www.youtube.com/embed/_C0vbLV6WdA"
        title="Jupyter notebooks in Visual Studio Code"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allow="autoplay; encrypted-media; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

### 4. Install the course packages

Open a terminal **inside VS Code**: Terminal → New Terminal.

**Windows:**

```text
py -m pip install --upgrade pip
py -m pip install numpy pandas matplotlib scipy statsmodels openpyxl ipykernel
```

**macOS:**

```text
python3 -m pip install --upgrade pip
python3 -m pip install numpy pandas matplotlib scipy statsmodels openpyxl ipykernel
```

`ipykernel` is what VS Code uses to run notebook cells. If a notebook offers no kernel, this package is usually missing.

### 5. Check that a notebook runs

1. In VS Code, use File → Open Folder and open the `STA1_26` course folder (or a new empty folder if you have not cloned the repository yet).
2. Open the Command Palette: ++ctrl+shift+p++ (Windows) or ++cmd+shift+p++ (macOS).
3. Run **Create: New Jupyter Notebook**.
4. In the top right, click **Select Kernel** → **Python Environments** and pick the Python 3.12+ interpreter you installed.
5. In the first cell, run:

```python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

print(sys.version)
print("numpy", np.__version__)
print("pandas", pd.__version__)
```

Use the play button to the left of the cell, or ++ctrl+enter++.

If the cell runs and prints version numbers, the setup is done. Save the notebook if you want; you do not need to keep it.

!!! warning "Kernel not found"

    If VS Code cannot see Python, close VS Code and open it again after the Python install. Then run **Python: Select Interpreter** from the Command Palette and choose the python.org install, not an old Apple or Store copy.

### Working with course data

You do not need Git. The CSV and Excel files live in the course `data` folder on GitHub. Download that folder onto your computer and point your notebook at it.

1. Download the folder: [Download data folder](https://download-directory.github.io/?url=https://github.com/RBrooksDK/STA1_26/tree/main/data).
2. Unzip the file. You should see files such as `sensor_thickness.csv`. If they are not already inside a folder named `data`, put them in one.
3. In VS Code, use File → Open Folder and open the folder that **contains** `data` (the parent folder, not a single CSV).

You can also browse the files on GitHub: [data/](https://github.com/RBrooksDK/STA1_26/tree/main/data).

The `data` folder will be updated during the semester as new files are added. If a tutorial or assignment asks for a file you do not have, download the folder again and replace your old `data` folder with the new one.

Then load a file:

```python
import pandas as pd
from pathlib import Path

DATA = Path("data")
df = pd.read_csv(DATA / "sensor_thickness.csv")
df.head()
```

If your notebook sits inside a session folder (`01_Data_and_Descriptive_Statistics` and so on), go one level up instead: `DATA = Path("../data")`. `openpyxl` is required for `.xlsx` files.

When you simulate, keep a seed: `rng = np.random.default_rng(2026)`. Write `ddof=1` when you use `np.std` or `np.var` on a **sample**. Never name a Python variable `lambda`. Put interpretation in a markdown cell after the code, not only in a `print`.

### Resources

[Datasets](../pages/datasets.md)

[Download data folder](https://download-directory.github.io/?url=https://github.com/RBrooksDK/STA1_26/tree/main/data)

[Python downloads](https://www.python.org/downloads/)

[Visual Studio Code](https://code.visualstudio.com/download)

[Jupyter in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

[Getting started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
