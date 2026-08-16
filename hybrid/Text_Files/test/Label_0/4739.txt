#include <bits/stdc++.h>
using namespace std;
int X[200005], Y[200005], W[200005], S[200005], colormark[200005], mark[200005];
vector<int> V[200005];
vector<int> ans;
int main() {
  set<pair<int, int>> pq;
  int n, m;
  cin >> n >> m;
  for (int i = 1; i <= n; i++) cin >> W[i];
  for (int i = 0; i < m; i++) {
    cin >> X[i] >> Y[i];
    S[X[i]]++;
    S[Y[i]]++;
    V[X[i]].push_back(i);
    V[Y[i]].push_back(i);
  }
  for (long long int i = 1; i <= n; i++) {
    if (S[i]) pq.insert({S[i] - W[i], i});
  }
  while (pq.size()) {
    auto q = (*pq.begin());
    pq.erase(pq.begin());
    if (q.first > 0) {
      cout << "DEAD" << '\n';
      exit(0);
    }
    int id = q.second;
    vector<int> wt;
    for (auto j : V[id]) {
      if (mark[j]) continue;
      ans.push_back(j);
      if (X[j] == id) {
        swap(X[j], Y[j]);
      }
      wt.push_back(X[j]);
      mark[j] = 1;
    }
    for (auto j : wt) {
      pq.erase({S[j] - W[j], j});
      S[j]--;
      if (S[j] > 0) pq.insert({S[j] - W[j], j});
    }
  }
  reverse(ans.begin(), ans.end());
  cout << "ALIVE" << '\n';
  for (auto j : ans) {
    cout << j + 1 << " ";
  }
}
