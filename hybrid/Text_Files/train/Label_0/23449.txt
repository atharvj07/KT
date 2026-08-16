#include <bits/stdc++.h>
using namespace std;
using LL = long long;
using vi = vector<int>;
using pii = pair<int, int>;
using vpii = vector<pair<int, int>>;
using vll = vector<LL>;
using LD = long double;
template <typename T>
void check(T& a, const T& b) {
  if (a >= b) {
    a %= b;
  }
}
template <typename T>
T gcd(T u, T v) {
  if (u == v) return u;
  if (u == 0) return v;
  if (v == 0) return u;
  if (~u & 1) {
    if (v & 1)
      return gcd(u >> 1, v);
    else
      return gcd(u >> 1, v >> 1) << 1;
  }
  if (~v & 1) return gcd(u, v >> 1);
  if (u > v) return gcd((u - v) >> 1, v);
  return gcd((v - u) >> 1, u);
}
LL mulmod(LL a, LL b, const LL& m) {
  LL q = (LL)(((LD)a * (LD)b) / (LD)m);
  LL r = a * b - q * m;
  if (r > m) r %= m;
  if (r < 0) r += m;
  return r;
}
template <typename T, typename S>
T expo(T e, S n) {
  T x = 1, p = e;
  while (n) {
    if (n & 1) x = x * p;
    p = p * p;
    n >>= 1;
  }
  return x;
}
template <typename T>
T powerL(T e, T n, const T& m) {
  T x = 1, p = e;
  while (n) {
    if (n & 1) x = mulmod(x, p, m);
    p = mulmod(p, p, m);
    n >>= 1;
  }
  return x;
}
const int N = (int)1e5 + 10;
vector<vi> g;
int c[N], cnt[N];
pair<bool, int> dp[N];
int fans;
map<int, int> m;
pair<bool, int> dfs(int u, int par) {
  bool ans = true;
  int b = -1;
  int here = true;
  for (int& i : g[u]) {
    if (i != par) {
      auto x = dfs(i, u);
      ans &= x.first;
      if (here) {
        here = false;
        b = x.second;
      } else {
        if (x.second != b) b = -1;
      }
    }
  }
  if (here) {
    return dp[u] = {true, c[u]};
  }
  if (c[u] != b) {
    b = -1;
  }
  if (u == 1) {
  }
  if (ans) {
    dp[u] = {ans, b};
  } else
    dp[u] = {false, -1};
  if (ans == false) b = -1;
  if (b == -1) ans = false;
  return {ans, b};
}
void DFS(int u, int p) {
  cnt[u] = 1;
  for (int& i : g[u]) {
    if (i != p) DFS(i, u), cnt[u] += cnt[i];
  }
}
void fdfs(int u, int par) {
  for (int& i : g[u]) {
    if (i != par) {
      if (dp[u].first) {
        m[dp[i].second] -= cnt[i];
        if (m[dp[i].second] == 0) m.erase(dp[i].second);
      }
    }
  }
  if (dp[u].first) {
    m[c[u]]--;
    if (m[c[u]] == 0) {
      m.erase(c[u]);
    }
  }
  if (fans == -1 && dp[u].first && m.size() <= 1) {
    fans = u + 1;
    return;
  } else if (dp[u].first) {
    m[c[u]]++;
    for (int& i : g[u]) {
      if (i != par) {
        if (dp[u].first) {
          m[dp[i].second] += cnt[i];
        }
      }
    }
  }
  for (int& i : g[u]) {
    if (i != par) fdfs(i, u);
  }
  return;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cerr.tie(NULL);
  ;
  int n;
  cin >> n;
  g.resize(n + 1);
  fans = -1;
  for (int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  for (int i = 0; i < n; i++) cin >> c[i], m[c[i]]++;
  auto ans = dfs(0, -1);
  DFS(0, -1);
  if (ans.first) {
    cout << "YES\n" << 1 << '\n';
    return 0;
  }
  fdfs(0, -1);
  if (fans == -1) {
    cout << "NO" << '\n';
    return 0;
  } else
    cout << "YES" << '\n' << fans << '\n';
  return 0;
}
