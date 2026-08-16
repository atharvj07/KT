#include <bits/stdc++.h>
using namespace std;
int n, m, k;
const int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
struct arr {
  int A[400006];
  int* operator[](int i) { return A + i * (m + 2); }
} S;
int as = 0;
int cal(int x, int y) {
  int re = 0;
  re += S[x + 1][y] & S[x][y - 1];
  re += S[x + 1][y] & S[x][y + 1];
  re += S[x - 1][y] & S[x][y - 1];
  re += S[x - 1][y] & S[x][y + 1];
  int las = S[x + dx[7]][y + dy[7]];
  for (int d = 0; d < 8; ++d) {
    int cur = S[x + dx[d]][y + dy[d]];
    if (las & cur) ++re;
    las = cur;
  }
  return re;
}
int flg = 0;
void add(int x, int y) {
  S[x][y] = 1;
  as += cal(x, y);
}
void era(int x, int y) {
  S[x][y] = 0;
  as -= cal(x, y);
}
void ot() {
  if (flg) {
    for (int i = (1), iend = (m); i <= iend; ++i) {
      for (int j = (1), jend = (n); j <= jend; ++j)
        putchar(S[j][i] ? '*' : '.');
      puts("");
    }
  } else {
    for (int i = (1), iend = (n); i <= iend; ++i) {
      for (int j = (1), jend = (m); j <= jend; ++j)
        putchar(S[i][j] ? '*' : '.');
      puts("");
    }
  }
  puts("");
}
void solve() {
  cin >> n >> m >> k;
  as = 0;
  if (n * m <= 16) {
    for (int s = 1; s < (1 << n * m); ++s) {
      as = 0;
      for (int i = (0), iend = ((n + 2) * (m + 2)); i <= iend; ++i) S.A[i] = 0;
      for (int i = (1), iend = (n); i <= iend; ++i)
        for (int j = (1), jend = (m); j <= jend; ++j)
          if (s & (1 << (i - 1) * m + j - 1)) add(i, j);
      if (as == k) {
        ot();
        return;
      }
    }
    return void(puts("-1\n"));
  }
  flg = 0;
  if (n > m) swap(n, m), flg = 1;
  for (int i = (0), iend = ((n + 2) * (m + 2)); i <= iend; ++i) S.A[i] = 0;
  int mx = (n - 1) * (m - 1) * 4;
  if (k > mx) return void(puts("-1\n"));
  for (int i = (1), iend = (n); i <= iend; ++i)
    for (int j = (1), jend = (m); j <= jend; ++j) add(i, j);
  if (k >= mx - 15) {
    if (n == 3 && k == mx - 8) {
      era(1, 1), era(2, 1), era(3, 1);
      ot();
      return;
    }
    if (k == mx - 1 || k == mx - 2 || k == mx - 4 || k == mx - 5 || k == mx - 8)
      return void(puts("-1\n"));
    int rem = mx - k;
    if (rem == 14) {
      era(1, 1);
      rem = 11;
    } else if (rem == 13 || rem == 10) {
      era(1, 1);
      if (rem == 13) era(1, m);
      rem = 7;
    }
    if (k == mx) {
      ot();
    } else if (rem == 7 || rem == 11 || rem == 15 || rem == 3) {
      era(n, m);
      if (rem >= 7) era(n, m - 1);
      if (rem >= 11) era(n, m - 2);
      if (rem >= 15) era(n, m - 3);
      ot();
    } else if (rem % 3 == 0) {
      int t = rem / 3;
      if (t >= 1) era(1, 1);
      if (t >= 2) era(1, m);
      if (t >= 3) era(n, 1);
      if (t >= 4) era(n, m);
      ot();
    }
    return;
  }
  int x = 0, y = 0;
  for (int i = (n), iend = (1); i >= iend; --i) {
    for (int j = (m), jend = (1); j >= jend; --j) {
      era(i, j);
      if (k - as <= 3 && k >= as) {
        x = i, y = j;
        break;
      }
    }
    if (k - as <= 3 && k >= as) break;
  }
  int rem = k - as, tl, tr;
  if (rem == 0) {
    ot();
    return;
  }
  if (y <= m - 4)
    tl = 0, tr = 5;
  else
    tl = y - (m - 4), tr = 5 - tl;
  if (rem == 1) {
    if (tr == 1)
      add(x + 1, m - 1);
    else
      add(x, m);
  } else if (rem == 2) {
    if (tr > tl)
      add(x, m - 1);
    else
      add(x + 1, m - 3);
  } else {
    if (tr >= 4)
      add(x, m), add(x, m - 2);
    else if (tr == 3)
      add(x, m - 1), add(x + 1, m - 3);
    else if (tr == 2)
      add(x, m), add(x + 1, m - 3);
    else if (tr == 1)
      add(x + 1, m - 1), add(x + 1, m - 3);
  }
  ot();
}
signed main() {
  int T;
  cin >> T;
  while (T--) solve();
}
