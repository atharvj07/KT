#include <bits/stdc++.h>
using namespace std;
const int maxn = 5000 + 10;
int a[maxn];
int b[maxn];
int c[maxn];
int cnt[maxn];
int n, m;
bool mark[maxn];
int q[maxn][5];
bool Bomb;
int main() {
  cin >> n >> m;
  for (int i = 1; i <= m; i++) {
    cin >> q[i][1];
    if (q[i][1] == 1) {
      cin >> q[i][2] >> q[i][3] >> q[i][4];
      for (int j = q[i][2]; j <= q[i][3]; j++) cnt[j] += q[i][4];
    } else {
      cin >> q[i][2] >> q[i][3] >> q[i][4];
      bool flag = 0;
      for (int j = q[i][2]; j <= q[i][3]; j++) {
        if (!mark[j]) {
          flag = true;
          a[j] = q[i][4] - cnt[j];
          b[j] = q[i][4];
          mark[j] = true;
          cnt[j] = 0;
        } else {
          if (cnt[j] + b[j] >= q[i][4]) {
            flag = true;
            int t = b[j] + cnt[j];
            t -= q[i][4];
            a[j] -= t;
            b[j] = q[i][4];
          } else
            b[j] += cnt[j];
          cnt[j] = 0;
        }
      }
      if (!flag) Bomb = true;
    }
  }
  for (int i = 1; i <= n; i++) c[i] = a[i];
  if (Bomb) {
    cout << "NO";
    return 0;
  } else {
    for (int i = 1; i <= m; i++) {
      if (q[i][1] == 1)
        for (int j = q[i][2]; j <= q[i][3]; j++) a[j] += q[i][4];
      else {
        int mx = -1000000001;
        for (int j = q[i][2]; j <= q[i][3]; j++) mx = max(mx, a[j]);
        if (mx != q[i][4]) Bomb = true;
      }
    }
    if (Bomb) {
      cout << "NO";
      return 0;
    } else {
      bool F = 0;
      for (int i = 1; i <= n; i++)
        if (c[i] > 1000000000 || c[i] < -1000000000) F = true;
      if (F) {
        cout << "NO";
        return 0;
      }
      cout << "YES" << endl;
      for (int i = 1; i <= n; i++) cout << c[i] << " ";
    }
  }
}
