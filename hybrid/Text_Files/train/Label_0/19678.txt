#include <bits/stdc++.h>
const int MAXN = 1e5 + 5;
int a[MAXN], n;
std::vector<int> v[MAXN];
int q[MAXN], c[MAXN];
inline bool pd(int l, int r) {
  for (auto x : v[r])
    if (x == r - l + 1) return 1;
  return 0;
}
int main() {
  scanf("%d", &n);
  int now = 0;
  q[0] = 1;
  int xyx = 0;
  for (int ccc = 1; ccc <= n; ++ccc) {
    ++now;
    scanf("%d", a + now);
    v[now].clear();
    if (now != 1) {
      if (a[now] == a[now - 1]) v[now].push_back(2);
      for (auto x : v[now - 1])
        if (a[now - x - 1] == a[now]) v[now].push_back(x + 2);
    }
    if (!v[now].empty() &&
        pd(now - v[now][0] / 2 - v[now][0] + 1, now - v[now][0] / 2)) {
      now -= v[now][0];
      xyx += 2;
    } else {
      q[now] = q[now - 1];
      c[now] = c[now - 1];
      if (pd(q[now], now)) {
        q[now] += (now - q[now] + 1) / 2;
        c[now]++;
      }
    }
    int ans = xyx + c[now], p = now;
    while (!v[p].empty() && p - v[p][0] / 2 >= q[now]) {
      p -= v[p][0] / 2;
      ans++;
    }
    printf("%d ", ans);
  }
  puts("");
  return 0;
}
