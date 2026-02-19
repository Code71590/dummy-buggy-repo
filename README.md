# dummy-buggy-repo

A dummy Python repository intentionally containing code bugs for testing an **Autonomous CI/CD Healing Agent**.

## Purpose

This repository is used as a test target for the RIFT 2026 Hackathon CI/CD Healing Agent. The agent should:
1. Clone this repository
2. Run tests and linter to detect all failures
3. Generate targeted fixes for each bug
4. Commit fixes with `[AI-AGENT]` prefix
5. Push to a new branch: `TEAM_NAME_LEADER_NAME_AI_Fix`

## Bug Summary (Verified by running pytest + flake8)

### pytest results — 2 collection errors, 2 test failures

| Test File | Failure Type | Bug | Root Cause |
|---|---|---|---|
| `tests/test_validator.py` | Collection Error — SyntaxError | SYNTAX | `validator.py:6` — missing `:` after `def validate_email(email)` |
| `tests/test_data_processor.py` | Collection Error — ImportError | IMPORT | `data_processor.py:7` — `import ci_cd_test_pkg_missing` does not exist |
| `tests/test_utils.py::test_factorial` | AssertionError | LOGIC | `utils.py:53` — `factorial` uses `+` instead of `*` → `factorial(5)` returns `15` not `120` |
| `tests/test_config.py::test_get_port_returns_int` | AssertionError | TYPE_ERROR | `config.py:45` — `get_port()` returns `str` from env var instead of `int` |

### flake8 results — 4 warnings

| File | Line | Code | Bug Type | Description |
|---|---|---|---|---|
| `src/utils.py` | 6 | F401 | LINTING | `'os' imported but unused` |
| `src/formatter.py` | 7–9 | E111 | INDENTATION | `format_name()` body uses 2-space indent (not 4) |
| `src/formatter.py` | 28 | E117 | INDENTATION | `raise TypeError` is over-indented (12 spaces instead of 8) |
| `src/validator.py` | 6 | E999 | SYNTAX | `SyntaxError: expected ':'` (also shown by pytest) |

---

## Total: 7 distinct bugs across 5 files

> `validator.py:6 SyntaxError` is counted once (appears in both pytest and flake8 output)

| # | File | Line | Bug Type | Description |
|---|------|------|----------|-------------|
| 1 | `src/utils.py` | 6 | LINTING | Unused import `os` |
| 2 | `src/utils.py` | 53 | LOGIC | `factorial()` uses `+` instead of `*` → `factorial(5)` = 15, not 120 |
| 3 | `src/validator.py` | 6 | SYNTAX | Missing `:` after `def validate_email(email)` |
| 4 | `src/data_processor.py` | 7 | IMPORT | `import ci_cd_test_pkg_missing` — package does not exist |
| 5 | `src/data_processor.py` | 22 | LOGIC | `filter_by_value` uses `<` instead of `>` |
| 6 | `src/config.py` | 45 | TYPE_ERROR | `get_port()` returns `str` instead of `int` when env var is set |
| 7 | `src/formatter.py` | 7–9 | INDENTATION | `format_name()` uses 2-space indent instead of 4-space |
| 8 | `src/formatter.py` | 28 | INDENTATION | `raise TypeError` over-indented (12 spaces, should be 8) |

> **Bugs #3 and #4 match the exact test case examples in the RIFT problem statement:**
> - `src/utils.py line 6: Unused import 'os'` → LINTING
> - `src/validator.py line 6: Missing colon` → SYNTAX

## Project Structure

```
dummy-buggy-repo/
├── src/
│   ├── utils.py          # LINTING (unused import) + LOGIC (factorial)
│   ├── validator.py      # SYNTAX (missing colon)
│   ├── data_processor.py # IMPORT (missing package) + LOGIC (wrong operator)
│   ├── config.py         # TYPE_ERROR (str vs int)
│   └── formatter.py      # INDENTATION (2 locations)
├── tests/
│   ├── test_utils.py
│   ├── test_validator.py
│   ├── test_data_processor.py
│   ├── test_config.py
│   └── test_formatter.py
├── .github/workflows/ci.yml
├── requirements.txt
├── error_summary.txt
└── README.md
```

## Running Tests

```bash
pip install -r requirements.txt
pytest tests/ -v
flake8 src/ --max-line-length=100
```
