# Financial Econometrics Research

Python analysis of Siemens' daily exposure to the DAX and macroeconomic
associations with equity returns in an eight-country monthly panel. The notebook
examines historical associations with explicit assumptions and limitations.

The analysis includes:

- OLS market exposure, HAC inference, residual diagnostics and beta stability.
- Pooled and fixed-effects panel models with lagged macroeconomic variables.
- Euro-area NEER slope comparisons and country-clustered inference.
- Driscoll–Kraay covariance and global-recession-year sensitivity checks.
- Matched-sample comparisons using supplementary total-return indices.
- Leave-one-country-out diagnostics, residual correlations and CR2 sensitivity.

Open [the analysis notebook](analysis.ipynb) to inspect the implementation,
equations, validation checks, interpretation and references.

The workflow uses pandas, NumPy, SciPy, statsmodels and Matplotlib. All 43 code
cells were executed sequentially in a fresh Python 3.13 kernel using the supplied
local workbook. All 22 analytical tables matched the previously executed working
notebook at displayed precision. Thirteen existing CSV exports also matched after
parsing, with zero numerical differences. The software-version table differs
because the verification environment uses different package versions, recorded in
`requirements.txt`. The committed notebook has cleared outputs.

To reproduce the analysis, supply an authorised workbook as described in
[the data requirements](data/README.md), then run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run_analysis.py
```

The runner saves the executed notebook, tables and figures under
`analysis_outputs/`. Reproduction requires access to the input data.

Developed as individual university coursework. Course and external methodological
references are retained in the notebook.
