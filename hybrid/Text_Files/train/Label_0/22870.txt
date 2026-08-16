#include <bits/stdc++.h>
using namespace std;
const int N = 1e5;
vector<int> graph[N];
int a[N];
int s[N];
void DFS(int u, int p) {
  if (s[u] == -1) {
    int best = INT_MAX;
    for (int v : graph[u]) {
      if (v != p) {
        best = min(best, s[v]);
      }
    }
    if (best == INT_MAX) {
      best = s[p];
    }
    s[u] = best;
    if (s[u] < s[p]) {
      cout << -1;
      exit(0);
    }
    a[u] = s[u] - s[p];
  } else {
    if (p == -1) {
      a[u] = s[u];
    } else {
      a[u] = s[u] - s[p];
    }
  }
  for (int v : graph[u]) {
    if (v != p) {
      DFS(v, u);
    }
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  int n;
  cin >> n;
  for (int i = 1; i < n; i++) {
    int p;
    cin >> p;
    graph[i].push_back(p - 1);
    graph[p - 1].push_back(i);
  }
  for (int i = 0; i < n; i++) {
    cin >> s[i];
  }
  DFS(0, -1);
  cout << accumulate(a, a + n, 0LL);
  return 0;
}
