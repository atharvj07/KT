#include <bits/stdc++.h>
using namespace std;
int he[200010], ver[2 * 200010], nxt[2 * 200010], tot, in[200010];
void add(int x, int y) {
  ver[++tot] = y;
  nxt[tot] = he[x];
  he[x] = tot;
}
int que[200010], cnt;
long long w[200010];
vector<int> v[200010];
long long ans[200010];
int s[200010];
bool vis[200010];
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) {
    scanf("%lld", &w[i]);
  }
  for (int i = 1; i <= m; i++) {
    int x, y;
    scanf("%d%d", &x, &y);
    add(y, x);
    in[x]++;
  }
  queue<int> q;
  for (int i = 1; i <= n; i++) {
    if (in[i] == 0) q.push(i);
  }
  while (!q.empty()) {
    int x = q.front();
    q.pop();
    que[++cnt] = x;
    for (int i = he[x]; i; i = nxt[i]) {
      in[ver[i]]--;
      if (!in[ver[i]]) q.push(ver[i]);
    }
  }
  int maxx = 0;
  for (int i = 1; i <= cnt; i++) {
    int x = que[i];
    int stp = 0;
    if (!v[x].size())
      ans[0] ^= w[x];
    else {
      sort(v[x].begin(), v[x].end());
      s[x] = 0;
      for (int j = 0; j < v[x].size(); j++) {
        if (v[x][j] == s[x]) s[x]++;
      }
      stp = s[x];
      ans[stp] ^= w[x];
      maxx = max(maxx, stp);
    }
    s[x] = stp;
    for (int j = he[x]; j; j = nxt[j]) v[ver[j]].push_back(stp);
  }
  bool xx = false;
  for (int i = 0; i <= maxx; i++) {
    if (ans[i] != 0) {
      xx = true;
      break;
    }
  }
  if (xx) {
    puts("WIN");
    for (int i = maxx; i >= 0; i--) {
      if (ans[i]) {
        maxx = i;
        break;
      }
    }
    int tmp = 0;
    for (int i = 1; i <= n; i++) {
      if (s[i] == maxx && ((w[i] ^ ans[s[i]]) < w[i])) {
        tmp = i;
        break;
      }
    }
    w[tmp] = ans[maxx] ^ w[tmp];
    for (int i = 1; i <= n; i++) {
      if (i == tmp || s[i] >= s[tmp]) continue;
      for (int j = he[i]; j; j = nxt[j]) {
        if (ver[j] == tmp && vis[s[i]] == 0) {
          w[i] = ans[s[i]] ^ w[i];
          vis[s[i]] = 1;
          break;
        }
      }
    }
    for (int i = 1; i <= n; i++) printf("%lld ", w[i]);
  } else
    puts("LOSE");
}
