# dummy-buggy-repo

A dummy Python repository intentionally containing various code bugs for testing an **Autonomous CI/CD Healing Agent**.

## Purpose

This repository is used as a test target for the RIFT 2026 Hackathon CI/CD Healing Agent. The agent should:
1. Clone this repository
2. Detect all bugs by running tests and linters
3. Generate targeted fixes for each bug
4. Commit fixes with `[AI-AGENT]` prefix
5. Push to a new branch with the format `TEAM_NAME_LEADER_NAME_AI_Fix`

## Bug Types Present

| Bug Type | File | Line | Description |
|---|---|---|---|
| LINTING | `src/utils.py` | 15 | Unused import `os` |
| LOGIC | `src/utils.py` | 61 | `factorial()` base case wrong (`n <= 0` should be `n <= 1`) |
| SYNTAX | `src/validator.py` | 8 | Missing colon after function definition |
| IMPORT | `src/data_processor.py` | 7 | `import numpy` — not in requirements, causes ImportError |
| LOGIC | `src/data_processor.py` | 29 | `filter_by_value` uses `<` instead of `>` |
| TYPE_ERROR | `src/config.py` | 45 | `get_port()` returns `str` instead of `int` when env var is set |
| INDENTATION | `src/formatter.py` | 7 | `format_name` uses 2-space indent instead of 4-space |
| INDENTATION | `src/formatter.py` | 28 | `truncate_string` has extra indentation (12 spaces instead of 8) |

**Total: 8 bugs across 5 files**

## Project Structure

```
dummy-buggy-repo/
├── src/
│   ├── utils.py          # LINTING + LOGIC errors
│   ├── validator.py      # SYNTAX error
│   ├── data_processor.py # IMPORT + LOGIC errors
│   ├── config.py         # TYPE_ERROR
│   └── formatter.py      # INDENTATION errors
├── tests/
│   ├── test_utils.py
│   ├── test_validator.py
│   ├── test_data_processor.py
│   ├── test_config.py
│   └── test_formatter.py
├── requirements.txt
├── error_summary.txt     # Complete list of all bugs for reference
└── README.md
```

## Running Tests

```bash
pip install -r requirements.txt
pytest tests/ -v
```

## Running Linter

```bash
flake8 src/ --max-line-length=100
```

## Expected Failures (Before Agent Fix)

- `test_validator.py` — **SyntaxError** (cannot even import validator.py)
- `test_data_processor.py` — **ImportError** (numpy not installed)
- `test_utils.py::test_factorial` — **RecursionError** (infinite recursion due to logic bug)
- `test_config.py::test_get_port_returns_int` — **AssertionError** (str returned instead of int)
- Flake8: **F401** unused import `os` in utils.py
