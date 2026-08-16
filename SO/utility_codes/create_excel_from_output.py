import pandas as pd
import re

def create_excel_from_output(output_text, excel_filename="codebert_test_results.xlsx"):
    data = []
    test_folder = None
    metrics = {}

    for line in output_text.splitlines():
        if line.startswith("Results for Test_"):
            if test_folder is not None:
                data.append({"Test Folder": test_folder, **metrics})
            test_folder = line.replace("Results for ", "").replace(":", "").strip()
            metrics = {}
        elif "Accuracy:" in line:
            metrics["Accuracy"] = float(re.search(r"Accuracy: ([0-9.]+)", line).group(1))
        elif "Precision:" in line:
            metrics["Precision"] = float(re.search(r"Precision: ([0-9.]+)", line).group(1))
        elif "Recall:" in line:
            metrics["Recall"] = float(re.search(r"Recall: ([0-9.]+)", line).group(1))
        elif "F1-Score:" in line:
            metrics["F1-Score"] = float(re.search(r"F1-Score: ([0-9.]+)", line).group(1))

    if test_folder is not None:
        data.append({"Test Folder": test_folder, **metrics})

    df = pd.DataFrame(data)
    df.to_excel(excel_filename, index=False)
    print(f"Results saved to {excel_filename}")

if __name__ == "__main__":
    output_text = """
Results for Test_0:
  Accuracy: 0.7760
  Precision: 0.8151
  Recall: 0.7140
  F1-Score: 0.7612
Loading test data for Test_1...
Results for Test_1:
  Accuracy: 0.7750
  Precision: 0.8132
  Recall: 0.7140
  F1-Score: 0.7604
Loading test data for Test_2...
Results for Test_2:
  Accuracy: 0.7493
  Precision: 0.7628
  Recall: 0.7140
  F1-Score: 0.7376
Loading test data for Test_3...
Results for Test_3:
  Accuracy: 0.7510
  Precision: 0.7711
  Recall: 0.7140
  F1-Score: 0.7414
Loading test data for Test_4...
Results for Test_4:
  Accuracy: 0.7820
  Precision: 0.8264
  Recall: 0.7140
  F1-Score: 0.7661
Loading test data for Test_5...
Results for Test_5:
  Accuracy: 0.8180
  Precision: 0.9015
  Recall: 0.7140
  F1-Score: 0.7969
Loading test data for Test_6...
Results for Test_6:
  Accuracy: 0.7450
  Precision: 0.7612
  Recall: 0.7140
  F1-Score: 0.7368
Loading test data for Test_7...
Results for Test_7:
  Accuracy: 0.6930
  Precision: 0.6852
  Recall: 0.7140
  F1-Score: 0.6993
Loading test data for Test_8...
Results for Test_8:
  Accuracy: 0.7450
  Precision: 0.7612
  Recall: 0.7140
  F1-Score: 0.7368
Loading test data for Test_9...
Results for Test_9:
  Accuracy: 0.6930
  Precision: 0.6852
  Recall: 0.7140
  F1-Score: 0.6993
    """
    create_excel_from_output(output_text)


