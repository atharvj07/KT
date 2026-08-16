import json
import os
import re
from typing import List, Dict, Any

import pandas as pd


def extract_text_outputs_from_notebook(nb_path: str) -> List[str]:
    """Load a Jupyter notebook as JSON and collect all text outputs from cells."""
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    text_lines: List[str] = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for output in cell.get("outputs", []):
            # Stream outputs
            if output.get("output_type") == "stream":
                text = output.get("text")
                if isinstance(text, list):
                    text_lines.extend(text)
                elif isinstance(text, str):
                    text_lines.extend(text.splitlines(True))
            # display_data or execute_result with text/plain
            elif output.get("output_type") in {"display_data", "execute_result"}:
                data = output.get("data", {})
                text = data.get("text/plain")
                if isinstance(text, list):
                    text_lines.extend(text)
                elif isinstance(text, str):
                    text_lines.extend(text.splitlines(True))
    # Normalize newlines and strip trailing newlines while keeping content per line
    return [line.rstrip("\n") for line in text_lines]


def parse_metrics_from_lines(lines: List[str]) -> Dict[str, Any]:
    """Parse training/validation and testing metrics from text lines."""
    # Patterns
    epoch_header_re = re.compile(r"^Epoch\s+(\d+)\/(\d+):")
    train_loss_re = re.compile(r"^\s*Train\s+Loss:\s*([0-9]*\.?[0-9]+)")
    val_line_re = re.compile(r"^\s*Val\s+Loss:\s*([0-9]*\.?[0-9]+),\s*Val\s+Accuracy:\s*([0-9]*\.?[0-9]+)")
    best_val_checkpoint_re = re.compile(r"Best model saved to .* with validation accuracy:\s*([0-9]*\.?[0-9]+)")
    best_loaded_re = re.compile(r"Best model loaded from epoch\s+(\d+)\s+with validation accuracy\s+([0-9]*\.?[0-9]+)")

    num_test_samples_re = re.compile(r"^Number of testing samples:\s*(\d+)")
    test_line_re = re.compile(r"^Test\s+Loss:\s*([0-9]*\.?[0-9]+),\s*Test\s+Accuracy:\s*([0-9]*\.?[0-9]+)")

    # Containers
    val_rows: List[Dict[str, Any]] = []
    test_rows: List[Dict[str, Any]] = []

    current_epoch = None
    total_epochs = None
    pending_test_samples = None

    for line in lines:
        # Training/Epoch parsing
        m_epoch = epoch_header_re.search(line)
        if m_epoch:
            current_epoch = int(m_epoch.group(1))
            total_epochs = int(m_epoch.group(2))
            continue

        m_train = train_loss_re.search(line)
        if m_train and current_epoch is not None:
            # Create a row with train loss; val might be filled by subsequent line
            val_rows.append({
                "epoch": current_epoch,
                "total_epochs": total_epochs,
                "train_loss": float(m_train.group(1)),
                "val_loss": None,
                "val_accuracy": None,
            })
            continue

        m_val = val_line_re.search(line)
        if m_val:
            val_loss = float(m_val.group(1))
            val_acc = float(m_val.group(2))
            # Attach to the last row of the same epoch if present; else create
            if val_rows and val_rows[-1].get("epoch") == current_epoch:
                val_rows[-1]["val_loss"] = val_loss
                val_rows[-1]["val_accuracy"] = val_acc
            else:
                val_rows.append({
                    "epoch": current_epoch,
                    "total_epochs": total_epochs,
                    "train_loss": None,
                    "val_loss": val_loss,
                    "val_accuracy": val_acc,
                })
            continue

        # Best model info (optional)
        m_best_loaded = best_loaded_re.search(line)
        if m_best_loaded:
            # Record as a separate sheet later via metadata
            # For simplicity, we capture it at dataframe level
            # We'll attach to a metadata dict
            pass

        # Testing parsing
        m_num = num_test_samples_re.search(line)
        if m_num:
            pending_test_samples = int(m_num.group(1))
            continue

        m_test = test_line_re.search(line)
        if m_test:
            test_loss = float(m_test.group(1))
            test_acc = float(m_test.group(2))
            test_rows.append({
                "test_run": len(test_rows) + 1,
                "num_samples": pending_test_samples,
                "test_loss": test_loss,
                "test_accuracy": test_acc,
            })
            pending_test_samples = None
            continue

    # Sort by epoch if present
    if val_rows and "epoch" in val_rows[0]:
        val_rows = sorted(val_rows, key=lambda r: (r.get("epoch") or 0))

    return {
        "validation": val_rows,
        "testing": test_rows,
    }


def build_excel(nb_path: str, out_path: str) -> str:
    lines = extract_text_outputs_from_notebook(nb_path)
    metrics = parse_metrics_from_lines(lines)

    val_df = pd.DataFrame(metrics.get("validation", []))
    test_df = pd.DataFrame(metrics.get("testing", []))

    # Ensure output directory exists
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    # Write to Excel; require openpyxl, otherwise raise a helpful error
    try:
        with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
            if not val_df.empty:
                val_df.to_excel(writer, index=False, sheet_name="Validation")
            if not test_df.empty:
                test_df.to_excel(writer, index=False, sheet_name="Testing")
    except ImportError as e:
        raise SystemExit(
            "openpyxl is required to write .xlsx files. Install with: pip install openpyxl"
        ) from e

    return out_path


def main() -> None:
    nb_path = os.path.abspath("run.ipynb")
    out_path = os.path.abspath("results.xlsx")
    written = build_excel(nb_path, out_path)
    print(f"Wrote Excel to: {written}")


if __name__ == "__main__":
    main()


