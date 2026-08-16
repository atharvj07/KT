#include <bits/stdc++.h>
using namespace std;
int n, m;
char g[55][55];
vector<int> v[55];
int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      cin >> g[i][j];
      if (g[i][j] == '#') v[i].push_back(j);
    }
  }
  for (int i = 1; i <= n; i++) {
    int cnt = 0;
    for (int j = 1; j <= n; j++) {
      if (i == j) continue;
      cnt = 0;
      for (int x = 0; x < v[i].size(); x++) {
        ::vector<int>::iterator it;
        it = find(v[j].begin(), v[j].end(), v[i][x]);
        if (it != v[j].end()) cnt++;
      }
      if (cnt == 0) continue;
      if (cnt > 0 && v[j].size() != v[i].size()) {
        return cout << "No", 0;
      }
      if (v[j].size() == v[i].size()) {
        if (cnt != v[i].size()) {
          return cout << "No", 0;
        }
      }
    }
  }
  cout << "Yes";
  return 0;
}
