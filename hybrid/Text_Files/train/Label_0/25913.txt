#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<int> > parents(n);
  int deg[n];
  fill(deg, deg + n, 0);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    parents[b - 1].push_back(a - 1);
    deg[a - 1]++;
  }
  priority_queue<int> q;
  for (int i = 0; i < n; i++) {
    if (deg[i] == 0) q.push(i);
  }
  int rank[n];
  for (int i = n; i >= 1; i--) {
    int x = q.top();
    q.pop();
    for (int j = 0; j < parents[x].size(); j++) {
      deg[parents[x][j]]--;
      if (deg[parents[x][j]] == 0) q.push(parents[x][j]);
    }
    rank[x] = i;
  }
  for (int i = 0; i < n; i++) {
    cout << rank[i] << " ";
  }
  cout << endl;
}
