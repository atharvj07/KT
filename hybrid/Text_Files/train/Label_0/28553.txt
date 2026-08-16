#include <bits/stdc++.h>
const long long limit = 1e15 + 5;
using namespace std;
long long a[755], b[755], n, test;
void Nhap() {
  cin >> n >> test;
  for (long long i = 1; i <= n; i++) cin >> a[i];
}
bool check(long long start, long long x) {
  long long d = 0;
  long long s = start, val;
  priority_queue<long long> q;
  for (long long i = 1; i <= n; i++) {
    s += a[i];
    if (a[i] < 0) q.push(abs(a[i]));
    if (s < 0) {
      val = q.top();
      s += val;
      q.pop();
      ++d;
    }
    if (d > x) return (false);
  }
  return (true);
}
long long bs1(long long x) {
  long long l = 0, r = limit, mid, res = 0;
  while (l <= r) {
    mid = (l + r) / 2;
    if (check(mid, x)) {
      res = mid;
      r = mid - 1;
    } else
      l = mid + 1;
  }
  return (res);
}
void pre() {
  long long x;
  for (long long i = 0; i <= n; i++) {
    x = bs1(i);
    b[i] = x;
  }
}
long long bs2(long long x) {
  long long l = 0, r = n, mid, res = 0;
  while (l <= r) {
    mid = (l + r) / 2;
    if (b[mid] <= x) {
      res = mid;
      r = mid - 1;
    } else
      l = mid + 1;
  }
  return (res);
}
void process() {
  long long t, x;
  while (test--) {
    cin >> t;
    x = bs2(t);
    cout << x << "\n";
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  Nhap();
  pre();
  process();
  return 0;
}
