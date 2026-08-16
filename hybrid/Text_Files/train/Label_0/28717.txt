#include <bits/stdc++.h>
using namespace std;
template <typename C>
auto test(C* x) -> decltype(cerr << *x, 0LL);
template <typename C>
char test(...);
template <typename C>
struct itr {
  C begin, end;
};
template <typename C>
itr<C> get_range(C b, C e) {
  return itr<C>{b, e};
};
struct debug {
  template <typename T>
  debug& operator<<(const T&) {
    return *this;
  }
};
string _ARR_(int* arr, int sz) {
  string ret = "{ " + to_string(arr[0]);
  for (int i = 1; i < sz; i++) ret += " , " + to_string(arr[i]);
  ret += " }";
  return ret;
}
const int INF = 1e9 + 7;
const int MxN = 1e5 + 100;
vector<int> adj[MxN];
int d[MxN];
int dmx, vmx;
void dfs(int u, int p) {
  if (p != u) d[u] = d[p] + 1;
  if (d[u] > dmx) {
    dmx = d[u];
    vmx = u;
  }
  for (int v : adj[u]) {
    if (v != p) {
      dfs(v, u);
    }
  }
  return;
}
int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int __TC__;
  cin >> __TC__;
  while (__TC__--) {
    int n, a, b, da, db;
    cin >> n >> a >> b >> da >> db;
    for (int i = 0; i <= n; i++) adj[i].clear();
    a--;
    b--;
    for (int i = 1; i < n; i++) {
      int u, v;
      cin >> u >> v;
      u--;
      v--;
      adj[u].push_back(v);
      adj[v].push_back(u);
    }
    dmx = 0;
    d[a] = 0;
    dfs(a, a);
    int dist = (d[b]);
    dmx = 0;
    d[vmx] = 0;
    dfs(vmx, vmx);
    bool ok = 1;
    if (dist <= da)
      ok = 0;
    else if (2 * da >= dmx)
      ok = 0;
    else if (db > 2 * da)
      ok = 1;
    else if (db <= 2 * da)
      ok = 0;
    cout << (ok ? "Bob\n" : "Alice\n");
  }
  return 0;
}
