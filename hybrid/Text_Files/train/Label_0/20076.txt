#include <bits/stdc++.h>
using namespace std;
const long long MaxN = 5e2 + 10;
int main() {
  long long n, table[MaxN][MaxN];
  long long x = 0, y = 0;
  cin >> n;
  for (long long i = 0; i < n; ++i)
    for (long long j = 0; j < n; ++j) {
      cin >> table[i][j];
      if (table[i][j] == 0) {
        x = i;
        y = j;
      }
    }
  long long sumRow[MaxN], sumColumn[MaxN], sumDiag[2] = {};
  for (long long i = 0, j = 0; i < n; ++i)
    for (j = 0, sumRow[i] = 0, sumColumn[i] = 0; j < n; ++j) {
      sumColumn[i] += table[i][j];
      sumRow[i] += table[j][i];
      if (i == j) sumDiag[0] += table[i][j];
      if (i + j == n - 1) sumDiag[1] += table[i][j];
    }
  long long value = 0;
  if (y)
    value = sumRow[0];
  else
    value = sumRow[1];
  for (long long i = 0; i < n; ++i) {
    if (sumColumn[i] != value && i != x) {
      printf("-1");
      return 0;
    }
    if (sumRow[i] != value && i != y) {
      printf("-1");
      return 0;
    }
  }
  if (sumDiag[0] != value && x != y) {
    printf("-1");
    return 0;
  }
  if (sumDiag[1] != value && x + y != n - 1) {
    printf("-1");
    return 0;
  }
  long long restSum = -sumRow[y] + sumRow[(y) ? 0 : 1];
  if (restSum + sumColumn[x] != value) {
    printf("-1");
    return 0;
  }
  if (restSum + sumDiag[0] != value && x == y) {
    printf("-1");
    return 0;
  }
  if (restSum + sumDiag[1] != value && x + y == n - 1) {
    printf("-1");
    return 0;
  }
  if (n == 1) {
    cout << 1;
    return 0;
  }
  if (restSum > 0)
    cout << restSum;
  else {
    cout << -1;
    return 0;
  }
  return 0;
}
