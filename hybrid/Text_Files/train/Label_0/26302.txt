#include <bits/stdc++.h>
using namespace std;
inline long long read() {
  long long x = 0, f = 1;
  char c = getchar();
  while (c < '0' || c > '9') {
    if (c == '-') f = 0;
    c = getchar();
  }
  while (c >= '0' && c <= '9')
    x = (x << 3) + (x << 1) + (c ^ 48), c = getchar();
  return f ? x : -x;
}
long long n, k, dp[2010][2010], maxn, vis[2010][2010], cnt, siz;
long long dx[] = {1, 0};
long long dy[] = {0, 1};
char ch[2010][2010], ans[5000], minc;
vector<pair<long long, long long> > vec;
queue<pair<long long, long long> > q;
signed main() {
  n = read(), k = read();
  for (long long i = 1; i <= n; i++) scanf("%s", ch[i] + 1);
  memset(dp, 0x3f, sizeof(dp));
  dp[1][1] = (ch[1][1] != 'a');
  for (long long i = 1; i <= n; i++)
    for (long long j = ((i == 1) ? 2 : 1); j <= n; j++)
      dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + (ch[i][j] != 'a');
  if (!k) {
    vec.push_back(make_pair(1, 1));
    vis[1][1] = 1;
    ans[++cnt] = ch[1][1];
    maxn = 2;
    goto ling;
  }
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j <= n; j++) {
      if (dp[i][j] <= k) {
        vis[i][j] = 1;
        if (i + j > maxn) {
          maxn = i + j;
          vec.clear();
          vec.push_back(make_pair(i, j));
        } else if (i + j == maxn)
          vec.push_back(make_pair(i, j));
      }
    }
  }
ling:;
  siz = vec.size();
  for (long long i = 0; i < siz; i++) q.push(vec[i]);
  vec.clear();
  for (long long i = maxn; i < (n << 1); i++) {
    minc = 'z';
    while (!q.empty()) {
      long long x = q.front().first, y = q.front().second;
      q.pop();
      for (long long dir = 0; dir < 2; dir++) {
        long long nx = x + dx[dir], ny = y + dy[dir];
        if (nx > n || ny > n || vis[nx][ny]) continue;
        if (ch[nx][ny] < minc) {
          minc = ch[nx][ny];
          vis[nx][ny] = 1;
          vec.clear();
          vec.push_back(make_pair(nx, ny));
        } else if (ch[nx][ny] == minc) {
          vis[nx][ny] = 1;
          vec.push_back(make_pair(nx, ny));
        }
      }
    }
    ans[++cnt] = minc;
    siz = vec.size();
    for (long long i = 0; i < siz; i++) q.push(vec[i]);
    vec.clear();
  }
  if (k)
    for (long long i = 1; i < maxn; i++) putchar('a');
  for (long long i = 1; i <= cnt; i++) putchar(ans[i]);
  return 0;
}
