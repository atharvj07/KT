#include <bits/stdc++.h>
using namespace std;
int n;
struct node {
  long long int l, p;
} a[50005];
bool cmp(node x, node y) {
  return (x.l * x.p * (100 - y.p) < y.l * y.p * (100 - x.p));
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d%d", &a[i].l, &a[i].p);
  sort(a + 1, a + n + 1, cmp);
  double ans = 0, sum = 0;
  for (int i = 1; i <= n; i++) {
    ans += sum * a[i].l * a[i].p / 100.0;
    ans += a[i].l;
    sum += (100 - a[i].p) / 100.0;
  }
  printf("%.12f\n", ans);
  return 0;
}
