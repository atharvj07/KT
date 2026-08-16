#include <bits/stdc++.h>
using namespace std;
int n, first, a[1111];
int b[1111], ub = -1, pos;
vector<int> c[1111];
vector<int> d;
int can[1111];
void go(int p, int v) {
  if (v == -1) return;
  if (v == first) ub = p;
  c[p].push_back(v);
  go(p, a[v]);
}
int main() {
  scanf("%d%d", &n, &first);
  --first;
  for (int i = 0; i < n; ++i) b[i] = -1;
  for (int i = 0; i < n; ++i) {
    scanf("%d", a + i);
    a[i]--;
    b[a[i]] = i;
  }
  for (int i = 0; i < n; ++i) {
    c[i].clear();
    if (b[i] == -1) {
      go(i, i);
    }
  }
  assert(ub >= 0);
  d.clear();
  for (int i = 0; i < c[ub].size(); ++i) {
    if (c[ub][i] == first) pos = c[ub].size() - i;
  }
  for (int i = 0; i < n; ++i) {
    if (i == ub) continue;
    if (c[i].size() != 0) d.push_back(c[i].size());
  }
  sort(d.begin(), d.end());
  for (int i = 0; i < n; ++i) can[i] = 0;
  can[0] = 1;
  for (int i = 0; i < d.size(); ++i) {
    for (int j = n - 1; j >= 0; --j) {
      if ((j + d[i] < n) && (can[j] == 1)) can[j + d[i]] = 1;
    }
  }
  for (int i = 0; i < n; ++i) {
    if (can[i]) cout << i + pos << endl;
  }
  return 0;
}
