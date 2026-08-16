#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC optimization("unroll-loops")
const int mod = 1000000007;
const int inf = 1000000009;
const long long INF = 1000000000000000009;
const long long big = 1000000000000000;
const long double eps = 0.000000000000000000001;
using namespace std;
struct triple {
  int a, b, c;
};
vector<triple> W;
bool O[100005], B[100005];
vector<int> P[100005];
int L[100005];
void dfs(int n, int p) {
  O[n] = 1;
  vector<int> A;
  for (auto v : P[n]) {
    if (!O[v]) {
      L[v] = L[n] + 1;
      dfs(v, n);
      if (!B[v]) A.push_back(v);
    } else if (v != p && L[v] > L[n])
      A.push_back(v);
  }
  int s = A.size();
  for (int i = 1; i < s; i += 2) W.push_back({A[i - 1], n, A[i]});
  if ((int)s % 2 == 1) {
    W.push_back({A[s - 1], n, p});
    B[n] = 1;
  }
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n, m;
  cin >> n >> m;
  for (int i = 1; i <= m; i++) {
    int a, b;
    cin >> a >> b;
    P[a].push_back(b);
    P[b].push_back(a);
  }
  if (m % 2 != 0) {
    cout << "No solution";
    return 0;
  }
  dfs(1, 0);
  for (auto v : W) cout << v.a << " " << v.b << " " << v.c << "\n";
  return 0;
}
