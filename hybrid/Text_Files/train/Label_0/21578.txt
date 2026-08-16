#include <bits/stdc++.h>
using namespace std;
const int MAX = 100000 + 5;
vector<int> adj[MAX];
vector<pair<int, int> > edges, nodes;
int n;
int lst = 0;
int solve(int cur, int par) {
  int lst = 0;
  for (int i = 0; i < adj[cur].size(); i++) {
    int t = adj[cur][i];
    if (t == par) continue;
    nodes.push_back(make_pair(cur, t));
    if (lst) edges.push_back(make_pair(lst, nodes.size()));
    lst = nodes.size();
    int child = solve(t, cur);
    if (child) edges.push_back(make_pair(child, lst));
  }
  return lst;
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i < n; i++) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  solve(1, 0);
  assert(nodes.size() + 1 == n);
  assert(edges.size() + 2 == n);
  cout << nodes.size() << "\n";
  for (int i = 0; i < nodes.size(); i++)
    cout << "2 " << nodes[i].first << " " << nodes[i].second << "\n";
  for (int i = 0; i < edges.size(); i++)
    cout << edges[i].first << " " << edges[i].second << "\n";
  return 0;
}
