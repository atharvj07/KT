#include <bits/stdc++.h>
#pragma gcc optimize("ofast")
using namespace std;
long long modexp(long long a, long long b, long long m) {
  long long r = 1;
  a = a % m;
  while (b > 0) {
    if (b & 1) r = (r * a) % m;
    b = b / 2;
    a = (a * a) % m;
  }
  return r % m;
}
const int MAXN = 100002;
long long a[MAXN];
vector<long long> adj[100001];
long long res = 0;
map<long long, long long> m[MAXN];
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
void dfs(long long u, long long pa) {
  for (auto i : m[pa]) {
    long long tmpgcd = gcd(a[u], i.first);
    m[u][tmpgcd] += i.second;
    res =
        (res + ((tmpgcd % 1000000007) * (i.second % 1000000007)) % 1000000007) %
        1000000007;
  }
  m[u][a[u]]++;
  res = (res + a[u]) % 1000000007;
  for (auto i : adj[u]) {
    if (i != pa) dfs(i, u);
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  long long n;
  cin >> n;
  for (int i = 1; i < n + 1; i++) {
    cin >> a[i];
  }
  for (int i = 1; i < n; i++) {
    long long u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  dfs(1, 0);
  cout << res << '\n';
  return 0;
}
