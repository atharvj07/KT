#include <bits/stdc++.h>
using namespace std;
const int INF = 100000000;
struct put {
  int a, b;
  bool radi;
};
vector<vector<struct put>> graf;
int main() {
  int n, m;
  scanf("%d", &n);
  scanf("%d", &m);
  int a, b, c;
  set<pair<int, int>> sispr;
  set<pair<int, int>> spokv;
  struct put sp;
  int pokv = 0;
  vector<struct put> bzvz;
  graf.assign(n, bzvz);
  for (int i = 0; i < m; i++) {
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    a--;
    b--;
    sp.a = a;
    sp.b = b;
    sp.radi = ((c == 1) ? true : false);
    graf[a].push_back(sp);
    sp.a = b;
    sp.b = a;
    graf[b].push_back(sp);
    if (c == 0) {
      pokv++;
    } else {
      if (a < b) {
        sispr.insert(make_pair(a, b));
      } else {
        sispr.insert(make_pair(b, a));
      }
    }
  }
  int s = 0;
  vector<int> d(n, INF), p(n), d2(n, INF), pokvarenih(n, 0), ispravnih(n, 0);
  vector<bool> p2(n, false);
  d[s] = 0;
  d2[s] = 0;
  set<pair<int, int>> q;
  q.insert(make_pair(d[s], s));
  while (!q.empty()) {
    int v = q.begin()->second;
    int vv = q.begin()->first;
    q.erase(make_pair(vv, v));
    for (int j = 0; j < graf[v].size(); ++j) {
      int to = graf[v][j].b, len = 1, pokvaren = (graf[v][j].radi + 1) % 2;
      if (d[v] + len == d[to]) {
        if (pokvaren) {
          if (d2[v] + 1 < d2[to]) {
            d2[to] = d2[v] + 1;
            ispravnih[to] = ispravnih[v];
            pokvarenih[to] = pokvarenih[v] + 1;
            p[to] = v;
            p2[to] = false;
          }
        } else {
          if (d2[v] - 1 < d2[to]) {
            d2[to] = d2[v] - 1;
            ispravnih[to] = ispravnih[v] + 1;
            pokvarenih[to] = pokvarenih[v];
            p[to] = v;
            p2[to] = true;
          }
        }
      }
      if (d[v] + len < d[to]) {
        q.erase(make_pair(d[to], to));
        d[to] = d[v] + len;
        p[to] = v;
        if (pokvaren) {
          d2[to] = d2[v] + 1;
          ispravnih[to] = ispravnih[v];
          pokvarenih[to] = pokvarenih[v] + 1;
          p2[to] = false;
        } else {
          d2[to] = d2[v] - 1;
          ispravnih[to] = ispravnih[v] + 1;
          pokvarenih[to] = pokvarenih[v];
          p2[to] = true;
        }
        q.insert(make_pair(d[to], to));
      }
    }
  }
  int otac = 0, sin = n - 1;
  while (sin != otac) {
    a = sin;
    b = p[sin];
    bool r = p2[sin];
    if (r) {
      if (a < b) {
        sispr.erase(make_pair(a, b));
      } else {
        sispr.erase(make_pair(b, a));
      }
    } else {
      if (a < b) {
        spokv.insert(make_pair(a, b));
      } else {
        spokv.insert(make_pair(b, a));
      }
    }
    sin = p[sin];
  }
  int k = spokv.size() + sispr.size();
  printf("%d\n", k);
  while (spokv.size() != 0) {
    a = spokv.begin()->first;
    b = spokv.begin()->second;
    spokv.erase(make_pair(a, b));
    printf("%d %d 1\n", (a + 1), (b + 1));
  }
  while (sispr.size() != 0) {
    a = sispr.begin()->first;
    b = sispr.begin()->second;
    sispr.erase(make_pair(a, b));
    printf("%d %d 0\n", (a + 1), (b + 1));
  }
  return 0;
}
