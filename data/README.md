# Data requirements

Supply an authorised local workbook at `data/market_macro_data.xlsx`.

The original analysis used Bloomberg-derived equity and CPI observations and
policy-rate and nominal effective exchange-rate inputs documented in the
notebook. Reproduction requires the corresponding observations and conventions.
Data access and redistribution depend on the applicable source permissions.

All input sheets have headers on Excel row 3 and observations from row 4.

| Worksheet | Required columns |
|---|---|
| `Daily_Prices` | `Date`, `Siemens_adjusted_level`, `DAX_level` |
| `Monthly_Equity` | `Month`, followed by the eight country names below |
| `Monthly_Inflation` | `Month`, followed by the eight country names below |
| `Monthly_Policy` | `Month`, followed by the eight country names below |
| `Monthly_NEER` | `Month`, followed by the eight country names below |
| `TR_Austria`, `TR_Finland`, `TR_Italy` | `Date`, `PX_LAST` |

The country columns must appear in this order: Germany, Austria, Brazil, Finland,
Israel, Italy, Norway and Poland. Monthly equity and NEER inputs are levels.
Inflation and policy rates are percentages. The notebook defines the changes,
lags, samples and missing-value treatment and validates the input structure.

The first cell of each supplementary TR sheet must identify its ticker,
respectively `ATXTR Index`, `OMXH25GI Index` and `TFTSEMIB Index`.
Historical observations preceding the estimation windows are needed to construct
the initial returns and lags. The notebook reports coverage requirements and
retains assertions for consecutive months and the matched TR comparison.

The local workbook and generated tables, figures and executed notebooks are
excluded by `.gitignore`.
