#include <bits/stdc++.h>
using namespace std;
long long n, m;
struct data {
  long long l;
  long long r;
  friend bool operator<(const data &a, const data &b) { return a.l < b.l; }
} qwq[200010];
long long num[200010];
long long now[200010];
long long minn;
long long ans;
int main() {
  scanf("%lld%lld", &n, &m);
  for (int i = 1; i <= n; i++) {
    scanf("%lld%lld", &qwq[i].l, &qwq[i].r);
    num[i] = qwq[i].l - qwq[i - 1].r;
    now[i] = now[i - 1] + num[i];
  }
  sort(qwq + 1, qwq + n + 1);
  if (m == 0) {
    puts("0");
    return 0;
  }
  for (int i = 1; i <= n; i++) {
    while (now[i] - now[minn] >= m) minn++;
    ans = max(ans, qwq[i].r - qwq[minn].l + (m - now[i] + now[minn]));
  }
  printf("%lld", ans);
  return 0;
}
