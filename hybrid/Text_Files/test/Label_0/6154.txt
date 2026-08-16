#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 10;
const int inf = 1 << 29;
int n, x;
int l[maxn], r[maxn];
bool canl[maxn], canr[maxn];
vector<int> pos[maxn];
int main() {
  scanf("%d%d", &n, &x);
  int tmp;
  for (int i = 1; i <= n; i++) {
    scanf("%d", &tmp);
    pos[tmp].push_back(i);
  }
  memset(canl, false, sizeof(canl));
  memset(canr, false, sizeof(canr));
  int p = -1;
  for (int i = 0; i <= x; i++) {
    if (pos[i].empty()) {
      canr[i + 1] = true;
      r[i + 1] = p;
      continue;
    }
    if (pos[i][0] > p) {
      canr[i + 1] = true;
      r[i + 1] = p = pos[i].back();
    } else
      break;
  }
  p = inf;
  for (int i = x + 1; i >= 1; i--) {
    if (pos[i].empty()) {
      canl[i - 1] = true;
      l[i - 1] = p;
      continue;
    }
    if (pos[i].back() <= p) {
      canl[i - 1] = true;
      l[i - 1] = p = pos[i][0];
    } else
      break;
  }
  long long ans = 0;
  int pp = 0;
  for (int i = 1; i <= x && canr[i]; i++) {
    while (pp < x && (pp < i || !canl[pp] || l[pp] < r[i])) pp++;
    ans += (x - pp + 1);
  }
  printf("%lld\n", ans);
  return 0;
}
