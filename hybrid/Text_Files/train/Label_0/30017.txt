#include <bits/stdc++.h>
using namespace std;
const int INF = (int)2e9;
const long long INFL = (long long)9e18;
const int MAXINT = ((~0) ^ (1 << 31));
const long long MAXLL = ((~0) ^ ((long long)1 << 63));
template <class T>
inline T pow2(T a) {
  return a * a;
}
template <class T>
inline bool mineq(T& a, T b) {
  return (a > b) ? (a = b, true) : false;
}
template <class T>
inline bool maxeq(T& a, T b) {
  return (a < b) ? (a = b, true) : false;
}
const int maxn = 2e5;
long long n, m, par[maxn], mark[maxn], d[maxn], ans[maxn], chk[maxn];
pair<long long, pair<long long, long long> > e[maxn], ed[maxn];
vector<pair<long long, long long> > g[maxn];
set<pair<long long, long long> > st, nn;
long long getpar(long long v) {
  if (par[v] == v) return v;
  par[v] = getpar(par[v]);
  return par[v];
}
void mrg(long long v, long long u) {
  v = getpar(v);
  u = getpar(u);
  par[v] = u;
}
long long dfs(long long w, long long l) {
  d[w] = l;
  mark[w] = 1;
  long long mn = l, s;
  vector<long long> de;
  for (int i = 0; i < g[w].size(); i++) {
    if (!mark[g[w][i].first]) {
      s = dfs(g[w][i].first, l + 1);
      if (s < mn) mn = s;
      if (s <= l) {
        chk[g[w][i].second] = 1;
      }
    } else if (d[g[w][i].first] < l - 1) {
      if (d[g[w][i].first] < mn) mn = d[g[w][i].first];
      chk[g[w][i].second] = 1;
    }
    if (d[g[w][i].first] == l - 1 && de.size() == 0) {
      de.push_back(g[w][i].second);
    } else if (de.size() == 1 && d[g[w][i].first] == l - 1) {
      chk[de[0]] = 1;
      chk[g[w][i].second] = 1;
    }
  }
  return mn;
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    cin >> e[i].second.first >> e[i].second.second >> e[i].first;
    ed[i] = e[i];
  }
  sort(e, e + m);
  for (int i = 1; i <= n; i++) par[i] = i;
  for (int i = 0; i < m;) {
    long long s = i;
    vector<long long> v;
    while (e[s].first == e[i].first) {
      if (getpar(e[s].second.first) != getpar(e[s].second.second)) {
        pair<long long, long long> v1, v2;
        v1.first = getpar(e[s].second.second);
        v1.second = s;
        v2.first = getpar(e[s].second.first);
        v2.second = s;
        g[getpar(e[s].second.first)].push_back(v1);
        g[getpar(e[s].second.second)].push_back(v2);
        v.push_back(getpar(e[s].second.first));
        v.push_back(getpar(e[s].second.second));
      } else {
        nn.insert({e[s].second.first, e[s].second.second});
        nn.insert({e[s].second.second, e[s].second.first});
      }
      s++;
    }
    for (int j = 0; j < v.size(); j++) {
      if (!mark[v[j]]) {
        dfs(v[j], 0);
      }
    }
    for (int j = 0; j < v.size(); j++) {
      mark[v[j]] = 0;
      g[v[j]].clear();
      d[v[j]] = 0;
    }
    while (e[i].first == e[s - 1].first) {
      if (chk[i]) {
        st.insert({e[i].second.first, e[i].second.second});
      }
      if (getpar(e[i].second.first) != getpar(e[i].second.second)) {
        mrg(e[i].second.first, e[i].second.second);
      }
      i++;
    }
    i = s;
  }
  for (int i = 0; i < m; i++) {
    if (st.find({ed[i].second.first, ed[i].second.second}) != st.end())
      cout << "at least one" << endl;
    else if (nn.find({ed[i].second.first, ed[i].second.second}) != nn.end())
      cout << "none" << endl;
    else
      cout << "any" << endl;
  }
}
