#include <bits/stdc++.h>
using namespace std;
struct pnt {
  int first, second, d, id;
  pnt(int first = 0, int second = 0, int d = 0, int id = 0)
      : first(first), second(second), d(d), id(id) {}
};
const int NN = 3030;
const double pi = acosl(-1.0);
int r[NN];
void solve(vector<pnt> &p) {
  int ma = 0, id = 0;
  for (int i = 0; i < p.size(); i++) {
    if (ma < p[i].d) ma = p[i].d, id = i;
  }
  if (ma == 1) {
    int u = -1;
    for (int i = 0; i < p.size(); i++)
      if (p[i].d == 0) u = i;
    for (int i = 0; i < p.size(); i++)
      if (p[i].d) {
        printf("%d %d\n", p[i].id, p[u].id);
      }
    return;
  }
  int n = p.size() - 1, all = 0;
  swap(p[id], p[n]);
  vector<pair<double, int>> q;
  for (int i = 0; i < n; i++) {
    all += p[i].d - 1;
    double first = atan2(p[i].second - p[n].second, p[i].first - p[n].first);
    q.emplace_back(first, i + 1);
    first += pi;
    if (first > pi) first -= pi * 2;
    q.emplace_back(first, -i - 1);
  }
  sort(q.begin(), q.end());
  int cur = 0;
  deque<int> DQ;
  for (auto a : q) {
    if (a.second > 0 && a.first > 1e-12) {
      cur += p[a.second - 1].d - 1;
      DQ.push_back(a.second - 1);
    }
  }
  for (auto a : q) {
    if (cur <= -1 && all - cur <= -1) break;
    if (a.second > 0) {
      cur += p[a.second - 1].d - 1;
      DQ.push_back(a.second - 1);
    } else {
      cur -= p[-a.second - 1].d - 1;
      DQ.pop_front();
    }
  }
  vector<int> fl(n, 0);
  for (auto a : DQ) fl[a] = 1;
  vector<pnt> P, Q;
  for (int i = 0; i < n; i++) {
    if (fl[i])
      P.emplace_back(p[i]);
    else
      Q.emplace_back(p[i]);
  }
  P.emplace_back(p[n].first, p[n].second, -cur, p[n].id);
  Q.emplace_back(p[n].first, p[n].second, cur - all, p[n].id);
  solve(P);
  solve(Q);
}
int main() {
  int T, a, b, first, second;
  for (cin >> T; T--;) {
    vector<pnt> p;
    scanf("%d%d", &a, &b);
    for (int i = 1; i <= b; i++) scanf("%d", r + i);
    for (int i = 1; i <= a; i++) {
      scanf("%d%d", &first, &second);
      p.emplace_back(first, second, 0, i);
    }
    for (int i = 1; i <= b; i++) {
      scanf("%d%d", &first, &second);
      p.emplace_back(first, second, r[i], i);
    }
    puts("YES");
    solve(p);
  }
  return 0;
}
