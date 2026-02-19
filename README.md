# dummy-buggy-repo

Dummy Python repo with intentional bugs — test target for **RIFT 2026 Autonomous CI/CD Healing Agent**.

## Verified Bug Results

Run with: `python run_tests.py` (uses `--continue-on-collection-errors`)

### pytest — 3 failed, 26 passed, 2 errors (verified)

| # | Result | Test | Bug Type | Root Cause |
|---|--------|------|----------|------------|
| 1 | ERROR | `test_data_processor.py` (collection) | IMPORT | `data_processor.py:7` — `import ci_cd_test_pkg_missing` → `ModuleNotFoundError` |
| 2 | ERROR | `test_validator.py` (collection) | SYNTAX | `validator.py:6` — `def validate_email(email)` missing `:` → `SyntaxError` |
| 3 | FAILED | `test_utils.py::test_factorial` | LOGIC | `utils.py:53` — uses `+` instead of `*` → `factorial(5)` returns `15`, not `120` |
| 4 | FAILED | `test_config.py::test_get_port_returns_int` | TYPE_ERROR | `config.py:45` — `get_port()` returns `'9000'` (str), not `9000` (int) |
| 5 | FAILED | `test_data_processor.py::test_filter_*` | LOGIC | `data_processor.py:22` — `<` instead of `>` (only visible after Bug #1 fixed) |

### flake8 — verified warnings (`flake8 src/ --max-line-length=100`)

```
src/data_processor.py:7:1:  F401 'ci_cd_test_pkg_missing' imported but unused
src/formatter.py:7:3:       E111 indentation is not a multiple of 4
src/formatter.py:8:3:       E111 indentation is not a multiple of 4
src/formatter.py:9:3:       E111 indentation is not a multiple of 4
src/formatter.py:29:13:     E117 over-indented
src/utils.py:6:1:           F401 'os' imported but unused
src/validator.py:6:27:      E999 SyntaxError: expected ':'
```

---

## All Bugs — 8 total across 5 files

| # | File | Line | Bug Type | Description | Detected By |
|---|------|------|----------|-------------|-------------|
| 1 | `src/utils.py` | 6 | LINTING | Unused import `os` | flake8 F401 |
| 2 | `src/utils.py` | 53 | LOGIC | `factorial` uses `+` not `*` → wrong results | pytest FAILED |
| 3 | `src/validator.py` | 6 | SYNTAX | Missing `:` after function def | pytest ERROR + flake8 E999 |
| 4 | `src/data_processor.py` | 7 | IMPORT | `import ci_cd_test_pkg_missing` → ModuleNotFoundError | pytest ERROR |
| 5 | `src/data_processor.py` | 22 | LOGIC | `filter_by_value` uses `<` not `>` | pytest FAILED (after Bug #4 fixed) |
| 6 | `src/config.py` | 45 | TYPE_ERROR | `get_port()` returns `str` not `int` | pytest FAILED |
| 7 | `src/formatter.py` | 7–9 | INDENTATION | `format_name()` uses 2-space indent | flake8 E111 |
| 8 | `src/formatter.py` | 29 | INDENTATION | `raise TypeError` over-indented | flake8 E117 |

> **Problem statement test cases exactly matched:**  
> `src/utils.py:6` unused import `os` → LINTING  
> `src/validator.py:6` missing colon → SYNTAX

## Project Structure

```
dummy-buggy-repo/
├── src/
│   ├── utils.py          # Bug 1 (LINTING) + Bug 2 (LOGIC)
│   ├── validator.py      # Bug 3 (SYNTAX)
│   ├── data_processor.py # Bug 4 (IMPORT) + Bug 5 (LOGIC)
│   ├── config.py         # Bug 6 (TYPE_ERROR)
│   └── formatter.py      # Bug 7 + 8 (INDENTATION)
├── tests/
│   ├── test_utils.py
│   ├── test_validator.py
│   ├── test_data_processor.py
│   ├── test_config.py
│   └── test_formatter.py
├── .github/workflows/ci.yml
├── run_tests.py           ← run this to see all bugs
├── requirements.txt
├── error_summary.txt
└── README.md
```

## Run Tests

```bash
pip install -r requirements.txt
python run_tests.py
```
