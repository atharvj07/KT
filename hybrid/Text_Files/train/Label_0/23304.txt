#include <bits/stdc++.h>
using namespace std;
const int MAXN = int(2e5) + 10;
const int MOD = int(1e9) + 7;
const int oo = INT_MAX;
struct Query {
  int d, u, id;
};
int n, q;
int p[MAXN];
long long ans[MAXN][10];
vector<Query> open[MAXN], close[MAXN];
int bit[MAXN];
void update(int i) {
  for (i = MAXN - i; i < MAXN; i += i & -i) bit[i]++;
}
int query(int i) {
  int sum = 0;
  for (i = MAXN - i; i > 0; i -= i & -i) sum += bit[i];
  return sum;
}
long long gauss(long long x) {
  if (x == 0) return 0;
  return x * (x - 1) / 2LL;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  while (cin >> n >> q) {
    for (int i = 1; i <= n; ++i) {
      cin >> p[i];
      open[i].clear();
      close[i].clear();
    }
    for (int i = 0; i < q; ++i) {
      int l, d, r, u;
      cin >> l >> d >> r >> u;
      open[l].push_back({d, u, i});
      close[r].push_back({d, u, i});
    }
    memset(ans, 0, sizeof(ans));
    memset(bit, 0, sizeof(bit));
    for (int i = n; i > 0; --i) {
      for (auto& e : close[i]) {
        ans[e.id][3] = query(e.u + 1);
        ans[e.id][6] = query(e.d) - ans[e.id][3];
        ans[e.id][9] = query(1) - ans[e.id][6] - ans[e.id][3];
      }
      update(p[i]);
      for (auto& e : open[i]) {
        ans[e.id][2] = query(e.u + 1) - ans[e.id][3];
        ans[e.id][5] = query(e.d) - ans[e.id][2] - ans[e.id][3] - ans[e.id][6];
        ans[e.id][8] = query(1) - ans[e.id][5] - ans[e.id][6] - ans[e.id][2] -
                       ans[e.id][3] - ans[e.id][9];
      }
    }
    memset(bit, 0, sizeof(bit));
    for (int i = 1; i <= n; ++i) {
      for (auto& e : open[i]) {
        ans[e.id][1] = query(e.u + 1);
        ans[e.id][4] = query(e.d) - ans[e.id][1];
        ans[e.id][7] = query(1) - ans[e.id][4] - ans[e.id][1];
      }
      update(p[i]);
    }
    for (int i = 0; i < q; ++i) {
      long long r = 0;
      r += ans[i][1] * (ans[i][6] + ans[i][8] + ans[i][9]);
      r += ans[i][2] *
           (ans[i][4] + ans[i][6] + ans[i][7] + ans[i][8] + ans[i][9]);
      r += ans[i][3] * (ans[i][4] + ans[i][7] + ans[i][8]);
      r += ans[i][4] * (ans[i][6] + ans[i][8] + ans[i][9]);
      r += ans[i][6] * (ans[i][7] + ans[i][8]);
      r += ans[i][5] * (n - ans[i][5]);
      r += gauss(ans[i][5]);
      cout << r << '\n';
    }
  }
  return 0;
}
