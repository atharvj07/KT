#include <bits/stdc++.h>
using namespace std;
struct Node {
  int n, t;
  Node(int _n, int _t) {
    t = _n;
    n = _t;
  }
  bool operator<(Node a) const {
    if (t < a.t) {
      return true;
    }
    if (t == a.t) {
      if (n > a.n) {
        return true;
      }
    }
    return false;
  }
};
vector<int> out;
vector<vector<int> > Edge;
set<Node> Q;
vector<int> ans;
signed main() {
  long long n, m;
  cin >> n >> m;
  Edge.resize(n + 1);
  ans.resize(n + 1);
  out.resize(n + 1, 0);
  for (int i = 1; i <= m; i++) {
    long long u, v;
    cin >> u >> v;
    Edge[v].push_back(u);
    out[u]++;
  }
  for (int i = 1; i <= n; i++) {
    Q.insert(Node(out[i], i));
  }
  long long p = n;
  for (int i = 1; i <= n; i++) {
    set<Node>::iterator q = Q.begin();
    int n = q->n;
    ans[n] = p;
    p--;
    Q.erase(*q);
    for (int j = 0; j < Edge[n].size(); j++) {
      int from = Edge[n][j];
      set<Node>::iterator y = Q.find(Node(out[from], from));
      Q.erase(*y);
      out[from]--;
      Q.insert(Node(out[from], from));
    }
  }
  for (int i = 1; i <= n; i++) {
    cout << ans[i] << ' ';
  }
  cout << '\n';
  return 0;
}
