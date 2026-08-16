#include <bits/stdc++.h>
using namespace std;
long long k;
long long check(long long x, int tag) {
  long long res = 0;
  for (int i = 1; i <= x; i = i * 10) {
    if (tag)
      res += (x - i + 1) * (x - i + 2) / 2;
    else
      res += (x - i + 1);
  }
  return res;
}
long long bs(long long l, long long r, int tag) {
  while (l < r) {
    long long mid = (l + r + 1) >> 1;
    if (check(mid, tag) >= k)
      r = mid - 1;
    else
      l = mid;
  }
  return l;
}
int main() {
  int q;
  cin >> q;
  for (int i = 1; i <= q; i++) {
    cin >> k;
    long long x = bs(0, 2e9, 1);
    k -= check(x, 1);
    long long y = bs(0, x + 1, 0);
    k -= check(y, 0);
    cout << to_string(y + 1)[k - 1] << endl;
  }
}
