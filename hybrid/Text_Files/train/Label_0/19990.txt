#include <bits/stdc++.h>
using namespace std;
int n, m, i, x, y, w, ans;
map<int, int> nod[100005];
int query(int w, map<int, int> &m) {
  auto it = m.lower_bound(w);
  if (it == m.begin()) return 0;
  it = prev(it);
  return it->second;
}
void upd(int val, int w, map<int, int> &m) {
  auto it = m.upper_bound(w);
  if (it != m.begin()) {
    it = prev(it);
    if (val <= it->second) return;
  }
  while (true) {
    auto it = m.upper_bound(w);
    if (it == m.end()) break;
    if (it->second > val) break;
    m.erase(it);
  }
  m[w] = val;
}
int main() {
  cin >> n >> m;
  for (i = 1; i <= m; i++) {
    cin >> x >> y >> w;
    int len = query(w, nod[x]);
    upd(len + 1, w, nod[y]);
    ans = max(ans, len + 1);
  }
  cout << ans;
  return 0;
}
