#include <bits/stdc++.h>
using namespace std;
inline void read(int &x) {
  int v = 0, f = 1;
  char c = getchar();
  while (!isdigit(c) && c != '-') c = getchar();
  if (c == '-')
    f = -1;
  else
    v = (c & 15);
  while (isdigit(c = getchar())) v = (v << 1) + (v << 3) + (c & 15);
  x = v * f;
}
inline void read(long long &x) {
  long long v = 0ll, f = 1ll;
  char c = getchar();
  while (!isdigit(c) && c != '-') c = getchar();
  if (c == '-')
    f = -1;
  else
    v = (c & 15);
  while (isdigit(c = getchar())) v = (v << 1) + (v << 3) + (c & 15);
  x = v * f;
}
inline void readc(char &x) {
  char c;
  while (((c = getchar()) == ' ') || c == '\n')
    ;
  x = c;
}
const int mod = 998244353;
int n, m, i, j, x, y, dp[300005][3], f[3];
vector<int> e[300005];
void dfs(int x, int p) {
  dp[x][1] = dp[x][2] = 1;
  for (__typeof((e[x]).begin()) it = (e[x]).begin(); it != (e[x]).end(); it++) {
    if (*it == p) continue;
    dfs(*it, x);
    f[2] = 1ll * dp[x][2] * (dp[*it][0] + dp[*it][2]) % mod;
    f[1] = 1ll * dp[x][1] * (dp[*it][0] + dp[*it][2]) % mod;
    f[0] = 1ll * dp[x][0] * (dp[*it][0] + dp[*it][2]) % mod;
    f[1] = (f[1] + 1ll * dp[x][1] * dp[*it][0]) % mod;
    f[0] = (f[0] + 1ll * dp[x][1] * dp[*it][1]) % mod;
    f[0] = (f[0] + 1ll * dp[x][0] * dp[*it][0]) % mod;
    memcpy(dp[x], f, sizeof(f));
  }
}
int main() {
  read(n);
  for (((i)) = (1); ((i)) <= ((n - 1)); ((i))++) {
    int x, y;
    read(x);
    read(y);
    e[x].push_back(y);
    e[y].push_back(x);
  }
  dfs(1, 0);
  cout << (dp[1][0] + dp[1][2]) % mod;
  return 0;
}
