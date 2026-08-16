#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
const long long INF = 1e9 + 19;
int n, qq;
long long t[N];
long long res[N];
int p[N];
int cntCh[N];
set<pair<long long, int> > ch[N];
set<pair<long long, int> > q;
void read() {
  scanf("%d%d", &n, &qq);
  for (int i = 0; i < n; i++) scanf("%lld", &t[i]);
  for (int i = 0; i < n; i++) {
    scanf("%d", &p[i]);
    p[i]--;
    cntCh[p[i]]++;
  }
}
long long getCost(int v) { return t[v] / (cntCh[v] + 2); }
long long getCostMe(int v) { return t[v] - getCost(v) * (cntCh[v] + 1); }
void remMain(int i) {
  if (ch[i].empty()) return;
  q.erase(make_pair(ch[i].begin()->first + getCost(i), ch[i].begin()->second));
  q.erase(
      make_pair(ch[i].rbegin()->first + getCost(i), ch[i].rbegin()->second));
}
void addMain(int i) {
  if (ch[i].empty()) return;
  q.insert(make_pair(ch[i].begin()->first + getCost(i), ch[i].begin()->second));
  q.insert(
      make_pair(ch[i].rbegin()->first + getCost(i), ch[i].rbegin()->second));
}
void solve() {
  for (int i = 0; i < n; i++) {
    res[p[i]] += getCost(i);
    res[i] += getCostMe(i);
  }
  for (int i = 0; i < n; i++) {
    ch[p[i]].insert(make_pair(res[i], i));
  }
  for (int i = 0; i < n; i++) {
    if (!ch[i].empty()) {
      addMain(i);
    }
  }
  for (int i = 0; i < qq; i++) {
    int type;
    scanf("%d", &type);
    if (type == 1) {
      int v, u;
      scanf("%d%d", &v, &u);
      v--;
      u--;
      remMain(p[v]);
      remMain(p[p[v]]);
      remMain(p[p[p[v]]]);
      ch[p[v]].erase(make_pair(res[v], v));
      ch[p[p[v]]].erase(make_pair(res[p[v]], p[v]));
      ch[p[p[p[v]]]].erase(make_pair(res[p[p[v]]], p[p[v]]));
      res[p[v]] -= getCost(v);
      res[p[v]] -= getCostMe(p[v]);
      res[p[p[v]]] -= getCost(p[v]);
      cntCh[p[v]]--;
      res[p[p[v]]] += getCost(p[v]);
      res[p[v]] += getCostMe(p[v]);
      ch[p[p[p[v]]]].insert(make_pair(res[p[p[v]]], p[p[v]]));
      ch[p[p[v]]].insert(make_pair(res[p[v]], p[v]));
      addMain(p[p[p[v]]]);
      addMain(p[p[v]]);
      addMain(p[v]);
      remMain(u);
      remMain(p[u]);
      remMain(p[p[u]]);
      ch[p[u]].erase(make_pair(res[u], u));
      ch[p[p[u]]].erase(make_pair(res[p[u]], p[u]));
      res[u] -= getCostMe(u);
      res[p[u]] -= getCost(u);
      cntCh[u]++;
      res[u] += getCostMe(u);
      res[p[u]] += getCost(u);
      res[u] += getCost(v);
      ch[p[p[u]]].insert(make_pair(res[p[u]], p[u]));
      ch[p[u]].insert(make_pair(res[u], u));
      ch[u].insert(make_pair(res[v], v));
      addMain(p[p[u]]);
      addMain(p[u]);
      addMain(u);
      p[v] = u;
    } else if (type == 2) {
      int v;
      scanf("%d", &v);
      v--;
      printf("%lld\n", res[v] + getCost(p[v]));
    } else if (type == 3) {
      printf("%lld %lld\n", q.begin()->first, q.rbegin()->first);
    } else
      assert(false);
  }
}
void stress() {}
int main() {
  if (1) {
    int k = 1;
    for (int tt = 0; tt < k; tt++) {
      read();
      solve();
    }
  } else {
    stress();
  }
  return 0;
}
