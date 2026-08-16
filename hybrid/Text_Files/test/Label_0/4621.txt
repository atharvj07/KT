#include <bits/stdc++.h>
using namespace std;
struct edge {
  int a, b, w;
};
vector<vector<edge> > es;
long long dfs(int u, int p) {
  long long ret = 0;
  for (int v = 0; v < es[u].size(); v++) {
    edge e = es[u][v];
    if (e.b == p) {
      ret = max(0LL, ret);
    } else {
      ret = max(ret, dfs(e.b, u) + (long long)e.w);
    }
  }
  return ret;
}
int main() {
  int n;
  long long sum;
  cin >> n;
  es.clear();
  es.resize(n + 1);
  sum = 0;
  for (int i = 0; i < n - 1; i++) {
    int x, y, w;
    cin >> x >> y >> w;
    x;
    y;
    es[x].push_back((edge){x, y, w});
    es[y].push_back((edge){y, x, w});
    sum += w;
  }
  cout << (sum * 2 - dfs(1, -1)) << endl;
}
