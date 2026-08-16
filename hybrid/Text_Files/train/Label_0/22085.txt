#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100000;
const int MOD = 1000 * 1000 * 1000 + 7;
void solve();
int main() {
  auto start = clock();
  cout.sync_with_stdio(0);
  cin.tie(0);
  cout.precision(10);
  cout << fixed;
  int t = 1;
  while (t--) {
    solve();
  }
  cerr << "\nTime: " << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n";
  return 0;
}
int n, q;
vector<long long> t;
vector<int> parent;
vector<int> deg;
vector<long long> aggr;
vector<multiset<long long>> children;
multiset<long long> treeSet;
const long long INF = 1000ll * 1000 * 1000 * 1000 * 1000 * 1000;
void pushToParent(int v, int p, int sign) {
  long long val = t[v] / (deg[v] + 1);
  aggr[p] += val * sign;
}
long long getValWO(int v) {
  long long val = t[v] - deg[v] * (t[v] / (deg[v] + 1));
  val += aggr[v];
  return val;
}
long long getVal(int v) {
  int p = parent[v];
  assert(p != -1);
  return getValWO(v) + t[p] / (deg[p] + 1);
}
void mutateTreeSet(int v, bool add) {
  if (!children[v].empty()) {
    long long Min = *children[v].begin();
    long long Max = *children[v].rbegin();
    Min += t[v] / (deg[v] + 1);
    Max += t[v] / (deg[v] + 1);
    if (add) {
      treeSet.insert(Min);
      treeSet.insert(Max);
    } else {
      treeSet.erase(treeSet.find(Min));
      treeSet.erase(treeSet.find(Max));
    }
  }
}
void removeFromTreeSet(int v) { mutateTreeSet(v, false); }
void addToTreeSet(int v) { mutateTreeSet(v, true); }
void removeFromParent(int v) {
  int p = parent[v];
  assert(p != -1);
  long long val = getValWO(v);
  children[p].erase(children[p].find(val));
}
void addToParent(int v) {
  int p = parent[v];
  assert(p != -1);
  long long val = getValWO(v);
  children[p].insert(val);
}
void cut(int v) {
  int p = parent[v];
  assert(p != -1);
  int pp = parent[p];
  assert(pp != -1);
  int ppp = parent[pp];
  assert(ppp != -1);
  removeFromTreeSet(p);
  removeFromTreeSet(pp);
  removeFromTreeSet(ppp);
  removeFromParent(pp);
  removeFromParent(p);
  removeFromParent(v);
  pushToParent(v, p, -1);
  pushToParent(p, pp, -1);
  parent[v] = -1;
  --deg[p];
  pushToParent(p, pp, +1);
  addToParent(p);
  addToParent(pp);
  addToTreeSet(p);
  addToTreeSet(pp);
  addToTreeSet(ppp);
}
void link(int v, int p) {
  assert(parent[v] == -1);
  int pp = parent[p];
  assert(pp != -1);
  int ppp = parent[pp];
  assert(ppp != -1);
  removeFromTreeSet(p);
  removeFromTreeSet(pp);
  removeFromTreeSet(ppp);
  removeFromParent(pp);
  removeFromParent(p);
  pushToParent(v, p, +1);
  pushToParent(p, pp, -1);
  parent[v] = p;
  ++deg[p];
  pushToParent(p, pp, +1);
  addToParent(v);
  addToParent(p);
  addToParent(pp);
  addToTreeSet(p);
  addToTreeSet(pp);
  addToTreeSet(ppp);
}
void gen() {
  freopen("biginput.txt", "w", stdout);
  int n = 100;
  int q = 100;
  cout << n << " " << q << endl;
  for (int i = 0; i < n; ++i) {
    cout << rand() % 100 << " ";
  }
  cout << endl;
  vector<int> p(n);
  for (int i = 0; i < n; ++i) {
    p[i] = (i + 1) % n;
    cout << p[i] + 1 << " ";
  }
  cout << endl;
  for (int i = 0; i < q; ++i) {
    int u;
    int v;
    do {
      u = rand() % n;
      v = rand() % n;
    } while (u == v || p[v] == u || p[u] == v);
    cout << 1 << " " << u + 1 << " " << v + 1 << endl;
    p[u] = v;
  }
}
void solve() {
  scanf("%d%d", &n, &q);
  t.resize(n);
  parent.resize(n);
  aggr.assign(n, 0);
  deg.assign(n, 0);
  children.resize(n);
  for (int i = 0; i < n; ++i) {
    scanf("%lld", &t[i]);
  }
  for (int i = 0; i < n; ++i) {
    scanf("%d", &parent[i]);
    --parent[i];
    ++deg[i];
    ++deg[parent[i]];
  }
  for (int i = 0; i < n; ++i) {
    pushToParent(i, parent[i], +1);
  }
  for (int i = 0; i < n; ++i) {
    children[parent[i]].insert(getValWO(i));
  }
  for (int i = 0; i < n; ++i) {
    addToTreeSet(i);
  }
  for (int i = 0; i < q; ++i) {
    int type;
    scanf("%d", &type);
    if (type == 1) {
      int a, b;
      scanf("%d%d", &a, &b);
      --a;
      --b;
      cut(a);
      link(a, b);
    } else if (type == 2) {
      int a;
      scanf("%d", &a);
      --a;
      printf("%lld\n", getVal(a));
    } else if (type == 3) {
      printf("%lld %lld\n", *treeSet.begin(), *treeSet.rbegin());
    }
  }
}
