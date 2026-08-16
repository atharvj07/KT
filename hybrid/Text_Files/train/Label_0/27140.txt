#include <bits/stdc++.h>
using namespace std;
inline long long read() {
  long long x = 0, f = 1;
  char c = getchar();
  while ((c < '0' || c > '9') && (c != '-')) c = getchar();
  if (c == '-') f = -1, c = getchar();
  while (c >= '0' && c <= '9') x = x * 10 + c - '0', c = getchar();
  return x * f;
}
const int N = 110;
int n, a[N], c[N];
unsigned long long f[N][N * N], C[N][N];
int main() {
  n = read();
  int cnt = 0;
  for (register int i = (1); i <= (n); i++) {
    a[i] = read(), c[a[i]]++;
    cnt += (c[a[i]] == 1);
  }
  if (cnt == 2) return printf("%d\n", n), 0;
  f[0][0] = 1;
  int s = 0, S = 0;
  for (register int i = (1); i <= (100); i++)
    for (register int j = (1); j <= (c[i]); j++) {
      for (register int p = (s + 1); p >= (1); p--)
        for (register int q = (S + i); q >= (i); q--) {
          f[p][q] += f[p - 1][q - i];
        }
      s++, S += i;
    }
  C[0][0] = 1;
  for (register int i = (1); i <= (100); i++) {
    C[i][0] = 1;
    for (register int j = (1); j <= (i); j++)
      C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
  }
  int ans = 0;
  for (register int i = (1); i <= (100); i++) {
    for (register int j = (1); j <= (c[i]); j++)
      if (f[j][j * i] == C[c[i]][j]) ans = max(ans, j);
  }
  printf("%d\n", ans);
}
