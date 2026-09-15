# Getting Started with Jupyter and Anaconda

A practical setup guide for QADHPYTHON (Data Handling with Python). Follow this if you have
nothing installed yet. There are two routes - plain pip/venv, or Anaconda. Pick one; you do
not need both.

---

## Which should I pick?

**Plain pip + venv** is lighter, faster to install, and perfectly fine for this course - we
only need pandas, numpy, matplotlib, seaborn and Jupyter. If you are reasonably comfortable
with a terminal, use this route.

**Anaconda** is heavier (a multi-GB install) but bundles Python plus most of the scientific
stack in one installer, and its Navigator app gives you a point-and-click way to launch
Jupyter without touching a terminal. It is more forgiving for complete beginners, and it is
the more common choice in data science teams, so it is worth knowing even if you do not use
it day to day. If you are new to the command line, or your machine already has Anaconda,
use this route.

Either route ends up in the same place: a working Jupyter Notebook (or Lab) with the course
packages installed.

---

## Route A: Plain pip and venv

### 1. Check for Python

Windows (PowerShell):
```
python --version
```
If that fails, try:
```
py --version
```

Mac/Linux (Terminal):
```
python3 --version
```

You need Python 3.10 or newer. If it is missing or too old, install it:

- Windows: download the installer from https://www.python.org/downloads/ and run it. Tick
  "Add python.exe to PATH" on the first screen of the installer.
- Mac: download from https://www.python.org/downloads/ or install via Homebrew:
  `brew install python`
- Linux: use your package manager, e.g. `sudo apt install python3 python3-venv python3-pip`

### 2. Create a virtual environment

A venv keeps this course's packages separate from anything else on your machine.

Windows (PowerShell), from the folder where you want to work:
```
python -m venv qadhpython-venv
```

Mac/Linux:
```
python3 -m venv qadhpython-venv
```

### 3. Activate the venv

Windows (PowerShell):
```
qadhpython-venv\Scripts\Activate.ps1
```
Windows (Command Prompt):
```
qadhpython-venv\Scripts\activate.bat
```

Mac/Linux:
```
source qadhpython-venv/bin/activate
```

Your prompt should now show `(qadhpython-venv)` at the start of the line. Every `pip
install` you run from here on installs into this environment only.

### 4. Install the course packages

```
pip install jupyter pandas numpy matplotlib seaborn openpyxl
```

This also pulls in supporting packages (ipykernel, notebook server, etc.) automatically.

### 5. Launch Jupyter

Classic notebook interface:
```
jupyter notebook
```

Or the newer Jupyter Lab interface (tabs, file browser, more IDE-like):
```
jupyter lab
```

Either command opens a browser tab. If it does not open automatically, copy the URL printed
in the terminal (it includes a security token) into your browser.

### 6. Open a notebook

In the Jupyter file browser, navigate to the `.ipynb` file you want (for example one of the
files in this `Revision` folder) and click it. To create a new one instead, use
New > Python 3 (or the kernel name matching your venv) from the file browser.

---

## Route B: Anaconda

### What is Anaconda?

Anaconda is a Python distribution aimed at data science: one installer gives you Python,
Jupyter, and most of the common scientific packages (numpy, pandas, matplotlib, and more)
already installed, plus Anaconda Navigator, a desktop app for launching tools without a
terminal. Miniconda is the same idea but minimal - just Python and the `conda` package
manager, with nothing extra bundled, so you install only what you need.

Conda environments work like venvs but are managed by the `conda` command instead of
`python -m venv`, and can also manage non-Python dependencies (useful if a package needs
compiled libraries).

### 1. Download and install

- Anaconda (full, with Navigator): https://www.anaconda.com/download
- Miniconda (minimal): https://docs.conda.io/en/latest/miniconda.html

Run the installer with the default options. On Windows, when asked, you do not need to tick
"Add Anaconda to PATH" - use the "Anaconda Prompt" that the installer adds to the Start Menu
instead, which has conda ready to go.

### 2. Open a conda-aware terminal

- Windows: open "Anaconda Prompt" from the Start Menu.
- Mac/Linux: open a normal Terminal; the installer usually configures your shell so `conda`
  works directly. If not, see Troubleshooting below.

### 3. Create a conda environment for the course

```
conda create -n qadhpython python=3.12
```

### 4. Activate it

```
conda activate qadhpython
```

Your prompt should now show `(qadhpython)` at the start of the line.

### 5. Install the course packages

Using conda:
```
conda install jupyter pandas numpy matplotlib seaborn openpyxl
```

Or, if you prefer, pip inside the same conda environment works just as well:
```
pip install jupyter pandas numpy matplotlib seaborn openpyxl
```

### 6. Launch Jupyter

```
jupyter notebook
```
or
```
jupyter lab
```

Alternatively, open Anaconda Navigator (Start Menu / Applications), select the `qadhpython`
environment from the dropdown, and click Launch under Jupyter Notebook or JupyterLab.

### 7. Open a notebook

Same as Route A: use the Jupyter file browser to navigate to and open the `.ipynb` file.

---

## Troubleshooting

### "jupyter: command not found" or "'jupyter' is not recognized"

The environment where you installed Jupyter is not active, or its Scripts/bin folder is not
on PATH.

- Check you activated the right environment: the prompt should show `(qadhpython-venv)` or
  `(qadhpython)`.
- Re-run the install command inside the activated environment.
- Windows PATH issues: if `python` itself is not recognized either, reinstall Python and
  tick "Add python.exe to PATH", or manually add the Python and Scripts folders (e.g.
  `C:\Users\<you>\AppData\Local\Programs\Python\Python312\` and `...\Scripts\`) to PATH via
  Settings > System > About > Advanced system settings > Environment Variables.

### Notebook opens but the kernel does not match your venv

If Jupyter shows a different Python (missing packages, wrong version) than the venv you set
up, register your venv as its own kernel:

```
python -m ipykernel install --user --name=qadhpython-venv --display-name "Python (qadhpython-venv)"
```

Run this with the venv activated. Then in Jupyter, use Kernel > Change Kernel and pick
"Python (qadhpython-venv)". The same trick works for a conda environment - activate it first,
then run the same command with a matching `--name`.

### PowerShell blocks the venv activation script

If `Activate.ps1` fails with a message about execution policies, run PowerShell as
Administrator once and allow local scripts:
```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
Then retry activation in a normal (non-admin) PowerShell window.

### `conda` not recognized outside Anaconda Prompt

Run `conda init` once from the Anaconda Prompt (or from a Terminal where conda does work),
then restart your terminal. On Mac/Linux this adds a block to your `.bashrc` / `.zshrc`.

### I would rather use PyCharm than a browser notebook

PyCharm (Community edition is free) can open and run `.ipynb` files directly, or you can
work with the plain `.py` script versions instead:

1. Install PyCharm Community from https://www.jetbrains.com/pycharm/download/
2. Open the course folder as a PyCharm project.
3. File > Settings (Preferences on Mac) > Project > Python Interpreter > add the venv or
   conda environment you created above as the interpreter (point it at
   `qadhpython-venv\Scripts\python.exe` on Windows, or the conda environment's `python`).
4. Open a `.ipynb` file directly - PyCharm has a built-in Jupyter-style notebook editor - or
   open a `.py` demo file and run it with the green Run arrow; both use the interpreter you
   configured.

### Everything installed but plots do not appear

Make sure you are running inside an actual notebook cell with `%matplotlib inline` behaviour
on by default (modern Jupyter does this automatically) - if you are instead running a `.py`
script from a plain terminal with no display, plots will not pop up; that is expected, and
is why the demo scripts in this folder also save each figure to disk with `plt.savefig(...)`.
