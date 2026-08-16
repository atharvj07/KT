#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2 * (2e5 + 5);
const int MOD = 998244353;
int n, m;
int sumK = 0;
int k[MAXN];
vector<pair<int, int> > oriSp;
bool canFin(const int day) {
  vector<int> ks(k, k + MAXN);
  vector<int> sp(MAXN, 0);
  for (int i = 0; i < m; ++i) {
    const int d = oriSp[i].first;
    const int t = oriSp[i].second;
    if (d <= day) {
      sp[t] = max(d, sp[t]);
    }
  }
  vector<vector<int> > spe(MAXN, vector<int>());
  for (int type = 1; type <= n; ++type) {
    if (sp[type] != 0) {
      spe[sp[type]].push_back(type);
    }
  }
  int burle = 0;
  int restK = sumK;
  for (int i = 1; i <= day; ++i) {
    ++burle;
    for (int type : spe[i]) {
      int sub = min(ks[type], burle);
      burle -= sub;
      ks[type] -= sub;
      restK -= sub;
      if (restK <= 0) {
        return true;
      }
    }
  }
  bool suc;
  if (restK * 2 <= burle) {
    suc = true;
  } else {
    suc = false;
  }
  return suc;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &k[i]);
    sumK += k[i];
  }
  for (int i = 1; i <= m; ++i) {
    int d, t;
    scanf("%d%d", &d, &t);
    oriSp.push_back({d, t});
  }
  int low = sumK;
  int high = sumK * 2;
  while (low < high) {
    int mid = (low + high) / 2;
    if (canFin(mid)) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }
  int ans = low;
  printf("%d\n", ans);
}
