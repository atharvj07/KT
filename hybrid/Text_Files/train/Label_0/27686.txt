#include <bits/stdc++.h>
using namespace std;
vector<vector<long long int> > G;
vector<int> V;
vector<long long int> S;
int A[100001];
int B[100001];
int dfs(long long int x, long long int d) {
  V[x] = 1;
  for (unsigned long long int j = 0; j < G[x].size(); j++) {
    if (d % 2) {
      if (A[G[x][j]])
        return 1;
      else
        B[G[x][j]] = 1;
    } else {
      if (B[G[x][j]])
        return 1;
      else
        A[G[x][j]] = 1;
    }
    if (V[G[x][j]] == 0) {
      if (dfs(G[x][j], d + 1)) {
        return 1;
      }
    }
  }
  return 0;
}
int main() {
  long long int m, n, u, v, a;
  int f = 0;
  cin >> n >> m;
  G.clear();
  V.clear();
  for (long long int i = 0; i <= n; i++) {
    A[i] = B[i] = 0;
    V.push_back(0);
    G.push_back(vector<long long int>(0));
  }
  for (long long int i = 0; i < m; i++) {
    cin >> u >> v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  for (long long int i = 1; i <= n; i++) {
    if (!V[i]) {
      if (G[i].size() > 0) {
        A[i] = 1;
        if (dfs(i, 1)) {
          f = 1;
          break;
        }
      }
    }
  }
  if (f)
    cout << "-1" << endl;
  else {
    S.clear();
    a = 0;
    for (long long int i = 0; i <= n; i++) {
      if (A[i]) {
        S.push_back(i);
        a++;
      }
    }
    cout << a << endl;
    for (unsigned long long int i = 0; i < S.size(); i++) {
      cout << S[i] << " ";
    }
    cout << endl;
    S.clear();
    a = 0;
    for (long long int i = 0; i <= n; i++) {
      if (B[i]) {
        S.push_back(i);
        a++;
      }
    }
    cout << a << endl;
    for (unsigned long long int i = 0; i < S.size(); i++) {
      cout << S[i] << " ";
    }
    cout << endl;
  }
  return 0;
}
