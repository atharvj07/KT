#include <bits/stdc++.h>
using namespace std;
long long int gcd(long long int a, long long int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
long long int lcm(long long int a, long long int b) {
  return a * b / gcd(a, b);
}
long long int fexp(long long int a, long long int b) {
  long long int ans = 1;
  while (b) {
    if (b & 1) ans = ans * a % 1000000007;
    b /= 2;
    a = a * a % 1000000007;
  }
  return ans;
}
long long int inverse(long long int a, long long int p) {
  return fexp(a, p - 2);
}
void ingraph(vector<vector<long long int> >& graph, long long int m) {
  long long int x, y;
  for (long long int i = 0; i < m; i++) {
    cin >> x >> y;
    x--, y--;
    graph[x].push_back(y);
    graph[y].push_back(x);
  }
}
long long int modify(long long int n) {
  long long int res = n;
  res %= 1000000007;
  res += 1000000007;
  res %= 1000000007;
  return res;
}
vector<long long int> sum(1000001);
vector<long long int> dist(1000001);
long long int dp[1000001];
vector<long long int> vec(1000001);
bool visited[1000001] = {0};
void dfs(vector<vector<long long int> >& graph, long long int v,
         long long int p) {
  visited[v] = 1;
  if (v != 0)
    dist[v] = dist[p] + 1;
  else
    dist[v] = 0;
  dp[0] += dist[v] * vec[v];
  sum[v] += vec[v];
  for (long long int u : graph[v]) {
    if (!visited[u]) {
      dfs(graph, u, v);
      sum[v] += sum[u];
    }
  }
}
void det(vector<vector<long long int> >& graph, long long int v,
         long long int p) {
  visited[v] = 1;
  if (v != 0) {
    dp[v] = dp[p] + sum[0] - 2 * sum[v];
  }
  for (long long int u : graph[v]) {
    if (!visited[u]) {
      det(graph, u, v);
    }
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long int t;
  t = 1;
  while (t--) {
    long long int n;
    cin >> n;
    for (long long int i = 0; i < n; i++) cin >> vec[i];
    vector<vector<long long int> > graph(n);
    ingraph(graph, n - 1);
    dfs(graph, 0, -1);
    for (long long int i = 0; i < n; i++) visited[i] = 0;
    det(graph, 0, -1);
    long long int mx = 0;
    for (long long int i = 0; i < n; i++) mx = max(dp[i], mx);
    cout << mx;
  }
}
