#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10;
const int inf = 0x3f3f3f3f;
int a[N];
int n, k;
bool check1(int x) {
  long long sum = 0;
  for (int i = 1; i <= n; i++) {
    if (a[i] < x) sum += x - a[i];
  }
  return sum <= k;
}
bool check2(int x) {
  long long sum = 0;
  for (int i = 1; i <= n; i++) {
    if (a[i] > x) sum += a[i] - x;
  }
  return sum <= k;
}
int main() {
  long long sum = 0;
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; i++) {
    scanf("%lld", &a[i]);
    sum += a[i];
  }
  sort(a + 1, a + 1 + n);
  long long minn, maxn;
  if (sum % n == 0) {
    minn = sum / n;
    maxn = minn;
  } else {
    minn = sum / n;
    maxn = minn + 1;
  }
  long long l = 1, r = minn;
  long long ans1, ans2;
  while (l <= r) {
    int mid = l + r >> 1;
    if (check1(mid)) {
      l = mid + 1;
      ans1 = mid;
    } else
      r = mid - 1;
  }
  l = maxn, r = 1e9;
  while (l <= r) {
    int mid = l + r >> 1;
    if (check2(mid)) {
      r = mid - 1;
      ans2 = mid;
    } else
      l = mid + 1;
  }
  printf("%lld", ans2 - ans1);
  return 0;
}
