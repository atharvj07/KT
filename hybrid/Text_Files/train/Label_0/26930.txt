#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;
int cf[N], t[N], ch[N], a[N], b[N];
vector<int> w[N];
signed main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    cin >> a[i] >> b[i];
    a[i]--;
    b[i]--;
  }
  mt19937 rnd(time(0));
  int ce = 0;
  while (ce < (m + 1) / 2) {
    for (int i = 0; i < n; i++) cf[i] = rnd() % 2;
    ce = 0;
    for (int i = 0; i < m; i++) {
      if (cf[a[i]] != cf[b[i]]) ce++;
    }
  }
  int mx = 0;
  for (int i = 0; i < n; i++) {
    int l;
    cin >> l;
    for (int j = 0; j < l; j++) {
      int x;
      cin >> x;
      mx = max(x, mx);
      w[i].push_back(x - 1);
    }
  }
  bool work = true;
  while (work) {
    work = false;
    for (int i = 0; i < mx; i++) t[i] = rnd() % 2;
    for (int i = 0; i < n; i++) {
      bool ok = false;
      for (int j : w[i]) {
        if (t[j] == cf[i]) {
          ch[i] = j;
          ok = true;
          break;
        }
      }
      if (!ok) {
        work = true;
        break;
      }
    }
  }
  for (int i = 0; i < n; i++) cout << ch[i] + 1 << " ";
  cout << "\n";
  for (int i = 0; i < mx; i++) cout << t[i] + 1 << " ";
  return 0;
}
