#include <bits/stdc++.h>
using namespace std;
const int MaxN = 1010;
int n, m, k;
struct matrix {
  int n, m;
  long long a[MaxN][MaxN];
  long long sy[MaxN][MaxN];
  long long ty[MaxN][MaxN];
  long long sv[MaxN * 2][MaxN];
  long long tv[MaxN][MaxN];
  long long st[MaxN][MaxN];
  void set(int _n, int _m) {
    n = _n;
    m = _m;
  }
  long long getsy(int y, int L, int R) {
    long long p = sy[R][y];
    if (L >= 2) p -= sy[L - 1][y];
    return p;
  }
  long long getsv(int p, int L, int R) {
    if (p <= 1 || p > n + m) return 0;
    long long s = sv[p][min(R, n)];
    if (L >= 2) s -= sv[p][L - 1];
    return s;
  }
  void init() {
    for (int j = 1; j <= m; ++j)
      for (int i = 1; i <= n; ++i) sy[i][j] = sy[i - 1][j] + a[i][j];
    for (int j = 1; j <= m; ++j)
      for (int i = 1; i <= n; ++i)
        ty[i][j] = ty[i - 1][j] + (k + 1) * a[i][j] - getsy(j, i - k, i);
    for (int p = 2; p <= n + m; ++p)
      for (int i = 1; i <= n; ++i) {
        sv[p][i] = sv[p][i - 1];
        if (p - i >= 1 && p - i <= m) sv[p][i] += a[i][p - i];
      }
    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= m; ++j)
        tv[i][j] = tv[i][j - 1] + getsy(j, i - k + 1, i) -
                   getsv(i + j - k, i - k + 1, i);
    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= m; ++j)
        st[i][j] = st[i][j - 1] + ty[i][j] - tv[i][j - 1];
  }
  long long calc(int i, int j) { return st[i][j] - ty[i][j]; }
} T1, T2, T3, T4;
void init() {
  cin >> n >> m >> k;
  T1.set(n, m);
  T2.set(m, n);
  T3.set(n, m);
  T4.set(m, n);
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= m; ++j) {
      int x;
      scanf("%d", &x);
      T1.a[i][j] = T2.a[m - j + 1][i] = T3.a[n - i + 1][m - j + 1] =
          T4.a[j][n - i + 1] = x;
    }
  T1.init();
  T2.init();
  T3.init();
  T4.init();
}
void work() {
  long long ans = -1;
  int a = k, b = k;
  for (int i = k; i <= n - k + 1; ++i)
    for (int j = k; j <= m - k + 1; ++j) {
      long long p = T1.calc(i, j) + T2.calc(m - j + 1, i) +
                    T3.calc(n - i + 1, m - j + 1) + T4.calc(j, n - i + 1) +
                    k * T1.a[i][j];
      if (p > ans) {
        ans = p;
        a = i;
        b = j;
      }
    }
  cout << a << " " << b << endl;
}
int main() {
  init();
  work();
  return 0;
}
