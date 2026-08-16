#include <bits/stdc++.h>
using namespace std;
char board[4][4];
bool Valid(int x, int y) { return (x >= 0 && x < 4 && y >= 0 && y < 4); }
int main() {
  std::ios::sync_with_stdio(false);
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      cin >> board[i][j];
    }
  }
  bool valid = false;
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      if (board[i][j] == 'x') {
        if (Valid(i - 1, j) && board[i - 1][j] == 'x' && Valid(i - 2, j) &&
                board[i - 2][j] == '.' ||
            Valid(i - 1, j) && board[i - 1][j] == '.' && Valid(i - 2, j) &&
                board[i - 2][j] == 'x') {
          valid = true;
          break;
        } else if (Valid(i + 1, j) && board[i + 1][j] == 'x' &&
                       Valid(i + 2, j) && board[i + 2][j] == '.' ||
                   Valid(i + 1, j) && board[i + 1][j] == '.' &&
                       Valid(i + 2, j) && board[i + 2][j] == 'x') {
          valid = true;
          break;
        } else if (Valid(i, j - 1) && board[i][j - 1] == 'x' &&
                       Valid(i, j - 2) && board[i][j - 2] == '.' ||
                   Valid(i, j - 1) && board[i][j - 1] == '.' &&
                       Valid(i, j - 2) && board[i][j - 2] == 'x') {
          valid = true;
          break;
        } else if (Valid(i, j + 1) && board[i][j + 1] == 'x' &&
                       Valid(i, j + 2) && board[i][j + 2] == '.' ||
                   Valid(i, j + 1) && board[i][j + 1] == '.' &&
                       Valid(i, j + 2) && board[i][j + 2] == 'x') {
          valid = true;
          break;
        } else if (Valid(i + 1, j + 1) && board[i + 1][j + 1] == 'x' &&
                       Valid(i + 2, j + 2) && board[i + 2][j + 2] == '.' ||
                   Valid(i + 1, j + 1) && board[i + 1][j + 1] == '.' &&
                       Valid(i + 2, j + 2) && board[i + 2][j + 2] == 'x') {
          valid = true;
          break;
        } else if (Valid(i - 1, j - 1) && board[i - 1][j - 1] == 'x' &&
                       Valid(i - 2, j - 2) && board[i - 2][j - 2] == '.' ||
                   Valid(i - 1, j - 1) && board[i - 1][j - 1] == '.' &&
                       Valid(i - 2, j - 2) && board[i - 2][j - 2] == 'x') {
          valid = true;
          break;
        } else if (Valid(i - 1, j + 1) && board[i - 1][j + 1] == 'x' &&
                       Valid(i - 2, j + 2) && board[i - 2][j + 2] == '.' ||
                   Valid(i - 1, j + 1) && board[i - 1][j + 1] == '.' &&
                       Valid(i - 2, j + 2) && board[i - 2][j + 2] == 'x') {
          valid = true;
          break;
        } else if (Valid(i + 1, j - 1) && board[i + 1][j - 1] == 'x' &&
                       Valid(i + 2, j - 2) && board[i + 2][j - 2] == '.' ||
                   Valid(i + 1, j - 1) && board[i + 1][j - 1] == '.' &&
                       Valid(i + 2, j - 2) && board[i + 2][j - 2] == 'x') {
          valid = true;
          break;
        }
      }
    }
  }
  (valid) ? cout << "YES\n" : cout << "NO\n";
  return 0;
}
