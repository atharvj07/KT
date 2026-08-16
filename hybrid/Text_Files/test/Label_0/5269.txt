#include <bits/stdc++.h>
using namespace std;
template <class T>
inline void sc(T &x) {
  register int c = getchar();
  x = 0;
  int neg = 0;
  for (; ((c<48 | c> 57) && c != '-'); c = getchar())
    ;
  if (c == '-') {
    neg = 1;
    c = getchar();
  }
  for (; c > 47 && c < 58; c = getchar()) {
    x = (x << 1) + (x << 3) + c - 48;
  }
  if (neg) x = -x;
}
template <class T>
inline T bigmod(T p, T e, T M) {
  long long ret = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1) ret = (ret * p) % M;
    p = (p * p) % M;
  }
  return (T)ret;
}
template <class T>
inline T gcd(T a, T b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
template <class T>
inline T modinverse(T a, T M) {
  return bigmod(a, M - 2, M);
}
const int N = 1e5 + 55;
vector<int> L;
map<int, int> qq;
int dp[N];
vector<pair<int, int> > coin;
bool vis[N];
vector<int> G[N];
int us[N];
void dfs(int u) {
  if (u > N) return;
  if (u > 0) L.push_back((u));
  dfs(10 * u + 4);
  dfs(10 * u + 7);
}
int dfs(int u, int p) {
  vis[u] = 1;
  int ret = 0;
  for (auto a : G[u])
    if (a != p && vis[a] == 0) {
      ret += dfs(a, u);
    }
  return 1 + ret;
}
int main() {
  dfs(0);
  int n, m;
  sc(n);
  sc(m);
  for (int i = 0; i < m; i++) {
    int a, b;
    sc(a);
    sc(b);
    G[a].push_back((b));
    G[b].push_back((a));
  }
  for (int i = 1; i <= n; i++) {
    if (vis[i] == 0) {
      int t = dfs(i, -1);
      qq[t]++;
    }
  }
  for (auto a : qq) {
    int x = a.first;
    int y = a.second;
    for (int i = 1; i <= y; y -= i, i *= 2) {
      coin.push_back((make_pair(x * i, i)));
    }
    if (y > 0) coin.push_back((make_pair(x * y, y)));
  }
  for (int i = 0; i < N; i++) dp[i] = 1 << 30;
  dp[0] = 0;
  int tot = 0;
  for (auto a : coin) {
    tot += a.first;
    for (int j = tot; j >= a.first; j--) {
      dp[j] =
          ((dp[j]) > (dp[j - a.first] + a.second) ? (dp[j - a.first] + a.second)
                                                  : (dp[j]));
    }
  }
  int iM = 1 << 30;
  for (auto a : L) iM = ((iM) > (dp[a]) ? (dp[a]) : (iM));
  printf("%d\n", iM == 1 << 30 ? -1 : iM - 1);
}
