#include <bits/stdc++.h>
using namespace std;
const int N = 100003;
int rd() {
  int ch = getchar(), x = 0;
  for (; ch < '0' || ch > '9'; ch = getchar())
    ;
  for (; ch >= '0' && ch <= '9'; ch = getchar()) x = x * 10 + ch - '0';
  return x;
}
template <typename T>
bool chmax(T &a, const T &b) {
  if (a < b) return a = b, 1;
  return 0;
}
int n;
vector<pair<int, int> > G[N], V[N];
struct DS {
  map<int, int> ps, ng;
  int tag;
  priority_queue<pair<int, int>, vector<pair<int, int> >,
                 greater<pair<int, int> > >
      pq;
  void reb(int x, bool op) {
    if (op) {
      auto it = ng.upper_bound(x - (tag << 1));
      if (it == ng.begin()) return;
      --it;
      pq.emplace(x - it->first, x);
    } else {
      auto it = ps.lower_bound(x + (tag << 1));
      if (it == ps.end()) return;
      pq.emplace(it->first - x, it->first);
    }
  }
  void ins(int x, int val) {
    if (val > 0) {
      ps[x + tag] += val;
      reb(x + tag, true);
    } else {
      ng[x - tag] += val;
      reb(x - tag, false);
    }
  }
  int get() const {
    int res = 0, now = 0;
    auto i = ps.begin(), j = ng.begin();
    while (i != ps.end() && j != ng.end()) {
      if (i->first - j->first >= (tag << 1)) {
        now += j->second;
        ++j;
      } else {
        now += i->second;
        ++i;
      }
      chmax(res, now);
    }
    return res;
  }
  void work(int l) {
    while (!pq.empty()) {
      pair<int, int> _ = pq.top();
      if (_.first > (tag + l << 1)) break;
      pq.pop();
      int x = _.second, y = x - _.first;
      auto i = ps.find(x), j = ng.find(y);
      if (i == ps.end() || j == ng.end()) continue;
      if (i->second + j->second < 0) {
        j->second += i->second;
        ps.erase(i);
        reb(j->first, false);
      } else {
        i->second += j->second;
        ng.erase(j);
        reb(i->first, true);
      }
    }
    tag += l;
  }
  size_t size() const { return ps.size() + ng.size(); }
  int qry(int p) const {
    auto i = ps.find(p + tag), j = ng.find(p - tag);
    return (i == ps.end() ? 0 : i->second) + (j == ng.end() ? 0 : j->second);
  }
  void operator+=(const DS &o) {
    for (pair<int, int> i : o.ps) ins(i.first - o.tag, i.second);
    for (pair<int, int> i : o.ng) ins(i.first + o.tag, i.second);
  }
} S[N];
void dfs(int x, int fa) {
  for (pair<int, int> _ : G[x])
    if (_.first != fa) {
      int v = _.first, len = _.second;
      dfs(v, x);
      for (pair<int, int> &i : V[v])
        i.second -= max(0, max(-S[v].qry(i.first), S[v].qry(i.first + 1)));
      S[v].work(1);
      for (pair<int, int> i : V[v])
        if (i.second > 0) {
          S[v].ins(i.first, i.second);
          S[v].ins(i.first + 1, -i.second);
        }
      S[v].work(len - 1);
      if (S[x].size() < S[v].size()) swap(S[x], S[v]);
      S[x] += S[v];
    }
}
int main() {
  n = rd();
  for (int i = 1; i < n; ++i) {
    int u = rd(), v = rd(), l = rd() << 1;
    G[u].emplace_back(v, l);
    G[v].emplace_back(u, l);
  }
  int m = rd();
  G[0].emplace_back(1, 2);
  while (m--) {
    int d = rd() << 1, f = rd(), p = rd();
    V[p].emplace_back(d, f);
  }
  dfs(0, 0);
  printf("%d\n", S[0].get());
}
