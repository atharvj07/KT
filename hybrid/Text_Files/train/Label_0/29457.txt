#include <bits/stdc++.h>
using namespace std;
struct order {
  int l, r;
} r[500005];
bool cmp(order a, order b) { return a.r < b.r; }
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%d%d", &r[i].l, &r[i].r);
  sort(r, r + n, cmp);
  int e = r[0].r, ans = 1;
  for (int i = 1; i < n; i++)
    if (e < r[i].l) {
      ans++;
      e = r[i].r;
    }
  printf("%d\n", ans);
  return 0;
}
