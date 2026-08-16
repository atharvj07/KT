#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 10;
const long long INF = 5e18;
const long long LOG_INF = 60;
int p[MAXN];
long long a[MAXN], k[MAXN];
int n, qu[MAXN], deg[MAXN];
int my_log(long long x) {
  int ans = 0;
  while (x > 0) {
    x /= 2;
    ++ans;
  }
  return ans;
}
void solve() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    long long x;
    cin >> x;
    a[i] = x;
  }
  for (int i = 0; i < n; i++) {
    long long x;
    cin >> x;
    a[i] = x - a[i];
  }
  for (int v = 1; v < n; v++) {
    long long kk;
    cin >> p[v] >> kk;
    --p[v];
    ++deg[p[v]];
    k[v] = kk;
  }
  int h = 0, t = 0;
  for (int v = 0; v < n; v++) {
    if (deg[v] == 0) {
      qu[t++] = v;
    }
  }
  while (t - h) {
    int v = qu[h++];
    if (v == 0) {
      if (a[v] > 0) {
        cout << "NO\n";
        return;
      }
      break;
    }
    if (a[v] > 0) {
      if (my_log(a[v]) + my_log(k[v]) > LOG_INF) {
        cout << "NO\n";
        return;
      }
      if (my_log(a[p[v]]) > LOG_INF) {
        cout << "NO\n";
        return;
      }
      a[p[v]] += a[v] * k[v];
    } else {
      a[p[v]] += a[v];
    }
    if (--deg[p[v]] == 0) qu[t++] = p[v];
  }
  cout << "YES\n";
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int te = 1;
  for (int w = 1; w <= te; w++) {
    solve();
  }
  return 0;
}
