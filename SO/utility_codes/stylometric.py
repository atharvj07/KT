import numpy as np

# Stylometric Features
def extract_stylometric_features(code: str) -> np.ndarray:
    lines = code.splitlines()
    avg_line_length = np.mean([len(line) for line in lines]) if lines else 0
    num_lines = len(lines)
    num_tokens = len(code.split())
    num_chars = len(code)
    return np.array([avg_line_length, num_lines, num_tokens, num_chars], dtype=np.float32)
