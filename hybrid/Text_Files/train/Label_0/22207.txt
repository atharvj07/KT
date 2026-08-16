#include <bits/stdc++.h>
using namespace std;
const int MAX = 100005;
const int INF = 1 << 28;
const double EPS = 1e-7;
int N;
int v[MAX];
bool mark[MAX];
vector<int> G[MAX];
map<int, set<int> > M;
bool fill(int a, int b, int c) {
  v[0] = a;
  v[1] = 1;
  v[2] = b;
  v[3] = c;
  for (int i = 1; i <= (N); ++i) mark[i] = false;
  mark[1] = true;
  mark[a] = true;
  mark[b] = true;
  mark[c] = true;
  for (int i = 4; i < N; ++i) {
    bool flag = false;
    for (typeof(G[v[i - 2]].begin()) k = G[v[i - 2]].begin();
         k != G[v[i - 2]].end(); ++k)
      if (!mark[*k]) {
        flag = true;
        v[i] = *k;
        mark[*k] = true;
        break;
      }
    if (!flag) {
      return false;
    }
  }
  for (int i = 0; i < (N); ++i)
    if (M[v[i]].find(v[(i + 1) % N]) == M[v[i]].end() ||
        M[v[i]].find(v[(i + 2) % N]) == M[v[i]].end()) {
      return false;
    }
  return true;
}
int main() {
  ios::sync_with_stdio(false);
  cin >> N;
  for (int i = 0; i < (2 * N); ++i) {
    int a, b;
    cin >> a >> b;
    G[a].push_back(b);
    G[b].push_back(a);
    M[a].insert(b);
    M[b].insert(a);
  }
  for (int i = 1; i <= (N); ++i)
    if (M[i].size() != 4) {
      cout << -1 << endl;
      return 0;
    }
  for (typeof(G[1].begin()) i = G[1].begin(); i != G[1].end(); ++i)
    for (typeof(G[1].begin()) j = G[1].begin(); j != G[1].end(); ++j)
      for (typeof(G[1].begin()) k = G[1].begin(); k != G[1].end(); ++k)
        if (*i != *j && *j != *k && *i != *k)
          if (fill(*i, *j, *k)) {
            for (int a = 0; a < (N); ++a) cout << v[a] << ' ';
            return 0;
          }
  cout << -1 << endl;
  return 0;
}
