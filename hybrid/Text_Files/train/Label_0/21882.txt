#include <bits/stdc++.h>
using namespace std;
const int maxn = 105;
inline int gi() {
  char c = getchar();
  while (c < '0' || c > '9') c = getchar();
  int sum = 0;
  while ('0' <= c && c <= '9') sum = sum * 10 + c - 48, c = getchar();
  return sum;
}
int n, A[maxn][maxn][maxn];
int main() {
  n = gi();
  if (n == 1) return puts("1"), 0;
  A[1][1][1] = 4;
  A[1][1][2] = 1;
  A[1][2][1] = 3;
  A[1][2][2] = 2;
  A[2][1][1] = 5;
  A[2][1][2] = 8;
  A[2][2][1] = 6;
  A[2][2][2] = 7;
  A[3][1][1] = 10;
  A[3][1][2] = 9;
  A[3][2][1] = 11;
  A[3][2][2] = 12;
  for (int i = 3; i <= n; ++i)
    if (i & 1) {
      int p1 = 1;
      for (int j = 1; j <= i; ++j) A[j][1][i] = --p1;
      for (int j = i; j; --j)
        if ((j - i) & 1)
          for (int k = 1; k <= i; ++k) A[j][0][k] = --p1;
        else
          for (int k = i; k; --k) A[j][0][k] = --p1;
      int p2 = A[i][i - 1][i - 1];
      for (int j = i - 1; j >= 2; --j) A[i][j][i] = ++p2;
      for (int j = 2; j < i; ++j)
        if (j & 1)
          for (int k = 1; k < i; ++k) A[k][j][i] = ++p2;
        else
          for (int k = i - 1; k; --k) A[k][j][i] = ++p2;
      for (int j = 1; j <= i; ++j)
        if (j & 1)
          for (int k = i; k; --k) A[j][i][k] = ++p2;
        else
          for (int k = 1; k <= i; ++k) A[j][i][k] = ++p2;
      for (int p = i + 1; p; --p)
        for (int x = 1; x <= i; ++x)
          for (int y = 1; y <= i; ++y) A[x][p][y] = A[x][p - 1][y] - p1 + 1;
      for (int x = 1; x <= i; ++x)
        for (int y = 1; y <= i + 1; ++y)
          for (int z = 1; z * 2 <= i; ++z) swap(A[x][y][z], A[x][y][i + 1 - z]);
    } else {
      int p1 = 1;
      for (int j = 1; j <= i; ++j) A[1][j][i] = --p1;
      for (int j = i; j; --j)
        if ((i - j) & 1)
          for (int k = 1; k <= i; ++k) A[0][j][k] = --p1;
        else
          for (int k = i; k; --k) A[0][j][k] = --p1;
      int p2 = A[i - 1][i][i - 1];
      for (int j = i; j; --j)
        if ((i - j) & 1)
          for (int k = 2; k < i; ++k) A[k][j][i] = ++p2;
        else
          for (int k = i - 1; k >= 2; --k) A[k][j][i] = ++p2;
      for (int j = 1; j <= i; ++j)
        if (j & 1)
          for (int k = i; k; --k) A[i][j][k] = ++p2;
        else
          for (int k = 1; k <= i; ++k) A[i][j][k] = ++p2;
      for (int p = i + 1; p; --p)
        for (int x = 1; x <= i; ++x)
          for (int y = 1; y <= i; ++y) A[p][x][y] = A[p - 1][x][y] - p1 + 1;
    }
  for (int y = 1; y <= n; ++y) {
    for (int z = n; z; --z) {
      for (int x = 1; x <= n; ++x) printf("%d ", A[x][y][z]);
      puts("");
    }
    puts("");
  }
  return 0;
}
