# Financial Econometrics Research

Python research into equity market exposure and macroeconomic associations across
eight national stock markets. The project combines financial data preparation,
econometric modelling, diagnostic checks and reproducible reporting.

[Explore the analysis notebook](analysis.ipynb).

The daily study examines Siemens' exposure to the DAX using **5,290 paired daily
returns** from January 2006 to October 2026. The monthly study uses **1,991
country-month observations** from January 2006 to September 2026 to examine
associations between equity returns, inflation, policy rates and exchange-rate
appreciation.

| Research component | Implementation |
|---|---|
| Market exposure and stability | OLS market model, conventional and HAC inference, residual diagnostics, interaction tests and rolling beta |
| Macroeconomic panel analysis | Four pooled and fixed-effects specifications, including country and calendar-month effects and a euro-area exchange-rate interaction |
| Robustness and uncertainty | Country-clustered inference, Driscoll–Kraay and CR2 sensitivity, recession-year exclusions and leave-one-country-out refits |
| Data comparability | Matched-sample comparisons between the original equity benchmarks and supplementary total-return indices |

The daily market model estimates a Siemens beta of approximately **1.15**. In the
monthly panel, the estimated euro-minus-non-euro exchange-rate slope difference
is negative and statistically inconclusive under the primary country-clustered
inference. The notebook interprets these findings as historical associations and
discusses the limitations of eight country clusters, CPI publication timing and
differences in benchmark dividend conventions.

The implementation uses **pandas, NumPy, SciPy, statsmodels and Matplotlib**.
Input checks validate dates, numerical entries, country coverage and consecutive
months. Further assertions check transformations, common estimation samples and
finite model results. Reusable functions handle repeated estimation and table
formatting, while figures and CSV exports support inspection of the results.

All **43 code cells** completed sequentially in a fresh Python 3.13 kernel with
the supplied local workbook. The 22 analytical tables matched the previously
executed working notebook at displayed precision, and 13 existing CSV exports
matched after parsing with zero numerical differences. Package versions for the
verification environment are recorded in `requirements.txt`. The repository
notebook has cleared outputs.

To reproduce the analysis, supply an authorised local workbook as described in
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
