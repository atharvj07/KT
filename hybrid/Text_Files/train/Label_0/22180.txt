#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n, m;
  cin >> n >> m;
  int A[n][m], row[n], col[m];
  char c;
  memset(row, 0, sizeof(row));
  memset(col, 0, sizeof(col));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cin >> c;
      if (c == '.')
        A[i][j] = 0;
      else
        A[i][j] = 1;
    }
  }
  for (int i = 0; i < n; ++i) {
    if (row[i] == 0) {
      for (int j = 0; j < m; ++j) {
        if (A[i][j] == 1 && col[j]) {
          cout << "No" << endl;
          return 0;
        }
      }
      vector<int> X;
      for (int j = i + 1; j < n; ++j) {
        int ans = 1;
        if (row[j]) continue;
        for (int k = 0; k < m; ++k) {
          if (A[i][k] != A[j][k]) {
            ans = 0;
            break;
          }
        }
        if (ans == 1) X.push_back(j);
      }
      for (int j = 0; j < X.size(); ++j) row[X[j]] = 1;
      for (int j = 0; j < m; ++j)
        if (A[i][j]) col[j] = 1;
    }
  }
  cout << "Yes" << endl;
  return 0;
}
