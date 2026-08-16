#include <bits/stdc++.h>
using namespace std;
long long n, k, p;
int a[3000];
int b[3000];
int ch(long long mid) {
  long long lastky = 0;
  for (int i = 0; i < n; i++) {
    int ok = 0;
    while (lastky < k) {
      long long minx = abs(a[i] - b[lastky]) + abs(b[lastky] - p);
      minx = abs(a[i] - b[lastky]) + abs(b[lastky] - p);
      lastky++;
      if (minx <= mid) {
        ok = 1;
        break;
      }
    }
    if (!ok) return 0;
  }
  return 1;
}
int main() {
  cin >> n >> k >> p;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (int i = 0; i < k; i++) {
    cin >> b[i];
  }
  b[k] = 1e10;
  sort(a, a + n);
  sort(b, b + k);
  long long st = 0, En = 1e10;
  long long ans = 1e10;
  while (st <= En) {
    long long mid = (st + En) / 2;
    if (ch(mid)) {
      En = mid - 1;
      ans = mid;
    } else {
      st = mid + 1;
    }
  }
  cout << ans;
}
