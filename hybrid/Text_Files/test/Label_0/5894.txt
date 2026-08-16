#include <bits/stdc++.h>
using namespace std;
int n, m, r, v;
const int N = 200000;
int ai[N], bi[N], gc[N], pc[N], pd[N];
int ls[N], id[N], pr[N], va[N], wa[N];
int flag[N];
int main() {
  ios::sync_with_stdio(0);
  cin >> n;
  for (int i = 1; i <= n; ++i) cin >> ai[i];
  n++;
  ai[n] = 1e9 + 5;
  cin >> m;
  for (int i = 1; i <= m; ++i) cin >> bi[i];
  sort(bi + 1, bi + m + 1);
  r = unique(bi + 1, bi + m + 1) - bi - 1;
  for (int i = 1; i <= n; ++i) gc[i] = gc[i - 1] + (ai[i] == -1);
  for (int i = 1; i <= n; ++i)
    pc[i] = lower_bound(bi + 1, bi + r + 1, ai[i]) - bi;
  for (int i = 1; i <= n; ++i)
    pd[i] = upper_bound(bi + 1, bi + r + 1, ai[i]) - bi;
  pd[0] = 1;
  for (int i = 1; i <= n; ++i)
    if (ai[i] != -1) {
      int p = lower_bound(ls, ls + v + 1, ai[i]) - ls;
      if (p > v) v++;
      ls[p] = ai[i];
      id[p] = i;
      pr[i] = id[p - 1];
      va[i] = p;
    } else {
      for (int q = r, p = v + 1; q >= 1; --q) {
        while (ls[p - 1] >= bi[q]) p--;
        if (p > v) v++;
        ls[p] = bi[q];
        id[p] = -1;
      }
    }
  for (int i = n; i >= 1;) {
    flag[i] = 1;
    if (pr[i] != -1) {
      i = pr[i];
    } else {
      for (int j = i - 1; ~j; --j)
        if (ai[j] != -1 && va[j] < va[i] && ai[j] < ai[i] &&
                min(gc[i] - gc[j], pc[i] - pd[j]) == va[i] - va[j] - 1 ||
            j == 0) {
          for (int p = j + 1, q = pd[j], c = 1; c <= va[i] - va[j] - 1; ++p)
            if (ai[p] == -1) {
              flag[p] = 1;
              ai[p] = bi[q];
              bi[q] = -1;
              q++;
              c++;
            }
          i = j;
          break;
        }
    }
  }
  int w = 0;
  for (int i = 1; i <= n; ++i) {
    int p = lower_bound(ls, ls + w + 1, ai[i]) - ls;
    if (p > w) w++;
    ls[p] = ai[i];
    wa[i] = p;
  }
  n--;
  for (int i = 1, j = 1; i <= n; ++i)
    if (ai[i] == -1) {
      while (bi[j] == -1) j++;
      ai[i] = bi[j++];
    }
  for (int i = 1; i <= n; ++i) cout << ai[i] << " ";
}
