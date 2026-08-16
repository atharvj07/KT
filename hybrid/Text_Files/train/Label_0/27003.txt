#include <bits/stdc++.h>
using namespace std;
const int maxn = 7007;
const int maxe = 200000;
struct node {
  int l, r, val;
};
vector<node> a[maxn];
int ll[maxe], rr[maxe];
set<int> mp;
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  ll[1] = 1, rr[1] = 2;
  int now = 1, cnt = 3;
  ll[1] = 1;
  rr[1] = 2;
  for (int i = 2; i < maxe; i++) {
    if ((1 << now) == i) {
      now++;
      ll[i] = cnt++;
    } else
      ll[i] = -1;
    rr[i] = cnt++;
  }
  for (int i = 1; i <= m; i++) {
    int op;
    scanf("%d", &op);
    if (op == 1) {
      int t;
      node as;
      scanf("%d%d%d%d", &t, &as.l, &as.r, &as.val);
      a[t].push_back(as);
    } else {
      int L, R;
      scanf("%d%d", &L, &R);
      mp.clear();
      int l = R, r = R;
      for (int j = L; j <= n; j++) {
        for (int k = 0; k < a[j].size(); k++) {
          if (a[j][k].l <= r && a[j][k].r >= l) mp.insert(a[j][k].val);
        }
        l = (ll[l] == -1 ? rr[l] : ll[l]);
        r = rr[r];
      }
      printf("%d\n", mp.size());
    }
  }
  return 0;
}
