#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int x = 0, f = 1, c = getchar();
  while (c < 48) c == '-' && (f = -1), c = getchar();
  while (c > 47) x = x * 10 + c - '0', c = getchar();
  return x * f;
}
const int MAXN = 100005;
std::vector<int> adj[MAXN];
int s[MAXN], c[MAXN], q[MAXN];
int n, cnt;
inline bool check(int l, int r) {
  for (int x : adj[r])
    if (x == r - l + 1) return 1;
  return 0;
}
int main(int argc, char const *argv[]) {
  n = read();
  for (int i = q[0] = 1, x = 1; i <= n; ++x, ++i) {
    s[x] = read();
    adj[x].clear();
    if (x != 1) {
      if (s[x] == s[x - 1]) adj[x].push_back(2);
      for (int y : adj[x - 1])
        if (s[x - y - 1] == s[x]) adj[x].push_back(y + 2);
    }
    function<bool(void)> fes = [x]() {
      return check(x - adj[x][0] / 2 - adj[x][0] + 1, x - adj[x][0] / 2);
    };
    if (!adj[x].empty() && fes())
      x -= adj[x][0], cnt += 2;
    else {
      q[x] = q[x - 1];
      c[x] = c[x - 1];
      if (check(q[x], x)) q[x] += (x - q[x] + 1) / 2, c[x]++;
    }
    int ans = cnt + c[x], p = x;
    while (!adj[p].empty() && p - adj[p][0] / 2 >= q[x])
      p -= adj[p][0] / 2, ans++;
    printf("%d%c", ans, " \n"[i == n]);
  }
  return 0;
}
