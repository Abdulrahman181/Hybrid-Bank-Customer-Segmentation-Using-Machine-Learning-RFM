"""Static validation for the repository notebook; does not require the dataset."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "Bank_Customer_Segmentation.ipynb"
FORBIDDEN_PATH_MARKERS = ("/content/", "C:\\", "\\\\content\\")


def validate_notebook(path: Path = NOTEBOOK) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read valid notebook JSON: {exc}"]

    if notebook.get("nbformat") != 4:
        errors.append("expected nbformat 4")

    for index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        try:
            ast.parse(source, filename=f"{path}:cell-{index}")
        except SyntaxError as exc:
            errors.append(f"cell {index} has syntax error: {exc}")
        if cell.get("outputs"):
            errors.append(f"cell {index} contains saved outputs")
        if cell.get("execution_count") is not None:
            errors.append(f"cell {index} contains an execution count")
        for marker in FORBIDDEN_PATH_MARKERS:
            if marker in source:
                errors.append(f"cell {index} contains non-portable path marker {marker!r}")

    return errors


def main() -> int:
    errors = validate_notebook()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {NOTEBOOK.name} passed static notebook validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
