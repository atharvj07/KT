#include <bits/stdc++.h>
using namespace std;
struct Point {
  int t, x, y, nom;
  Point(int t = 0, int x = 0, int y = 0, int nom = 0) {}
  const bool operator<(const Point& q) const { return t < q.t; }
  const bool operator>(const Point& q) const { return t > q.t; }
};
int n, m, sa[500500];
long long ans[500500];
set<long long> s;
vector<int> g[500500];
vector<pair<int, int> > g2[500500];
Point a[500500];
void add(int x, int val) {
  while (x <= 500500) {
    sa[x] += val;
    x = (x | (x - 1)) + 1;
  }
}
int fs(int x) {
  int res = 0;
  while (x) {
    res += sa[x];
    x &= (x - 1);
  };
  return res;
}
int findright(int x) {
  int l = x + 1, r = 500500 - 1, t = fs(x);
  while (l < r - 1)
    if (fs((l + r) / 2) == t)
      l = (l + r) / 2;
    else
      r = (l + r) / 2;
  if (fs(r) == t)
    return r;
  else
    return l;
}
int findleft(int x) {
  int l = 1, r = x - 1, t = fs(x);
  while (l < r - 1)
    if (fs((l + r) / 2) == t)
      r = (l + r) / 2;
    else
      l = (l + r) / 2;
  if (fs(l) == t)
    return l;
  else
    return r;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; i++) {
    Point o;
    scanf("%d%d%d", &o.t, &o.x, &o.y);
    o.nom = i;
    a[i] = o;
  }
  sort(a, a + n);
  s.clear();
  for (int i = 0; i < n; i++) s.insert(a[i].t);
  int tek = 1, way = 0, it = 0;
  long long ptime;
  while (!s.empty()) {
    long long time = *s.begin();
    s.erase(time);
    tek += way * (time - ptime);
    while ((it < n) && (a[it].t <= time)) {
      g2[a[it].x].push_back(make_pair(a[it].y, a[it].nom));
      add(a[it].x, +1);
      it++;
    }
    for (int i = 0; i < g[tek].size(); i++) ans[g[tek][i]] = time;
    add(tek, -g[tek].size());
    g[tek].clear();
    for (int i = 0; i < g2[tek].size(); i++) {
      g[g2[tek][i].first].push_back(g2[tek][i].second);
      add(g2[tek][i].first, +1);
    }
    add(tek, -g2[tek].size());
    g2[tek].clear();
    int up = fs(500500 - 1) - fs(tek), down = fs(tek - 1);
    if ((!up) && (!down))
      way = 0;
    else if (up >= down) {
      way = +1;
      s.insert(time + findright(tek) - tek);
    } else {
      way = -1;
      s.insert(time + tek - findleft(tek));
    }
    ptime = time;
  }
  for (int i = 0; i < n; i++) printf("%I64d\n", ans[i]);
}
