#include <bits/stdc++.h>
using namespace std;
int n;
long long k;
vector<int> a;
int mysqrt(long long n) {
  long long l = -1;
  long long r = 2 * sqrt(n);
  while (r - l > 1) {
    long long mid = (r + l) >> 1;
    if (mid * mid <= n)
      l = mid;
    else
      r = mid;
  }
  return l;
}
bool check(long long d) {
  if (d <= 0) return false;
  long long to_remove = 0;
  for (int i = 0; i < n; ++i) {
    to_remove += (a[i] + d - 1) / d * d - a[i];
  }
  return to_remove <= k;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> k;
  a.resize(n);
  long long C = k;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    C += a[i];
  }
  int sqrtc = mysqrt(C);
  long long d = 1;
  for (int i = 1; i <= sqrtc + 1000; ++i) {
    if (check(i)) d = i;
  }
  for (int i = 1; i <= sqrtc + 1000; ++i) {
    long long x = C / i;
    if (check(x)) d = max(d, x);
  }
  cout << d << endl;
  return 0;
}
