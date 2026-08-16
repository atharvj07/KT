#include <bits/stdc++.h>
using namespace std;
vector<long long> pa, pb;
vector<long long> njp;
int main() {
  long long x, y, l, r;
  cin >> x >> y >> l >> r;
  pa.push_back(1);
  for (long long p = 1; p <= r / x; p *= x) {
    pa.push_back(p * x);
  }
  pb.push_back(1);
  for (long long p = 1; p <= r / y; p *= y) {
    pb.push_back(p * y);
  }
  for (auto i : pa) {
    for (auto j : pb) {
      if (l <= i + j && i + j <= r) {
        njp.push_back(i + j);
      }
    }
  }
  njp.push_back(r + 1);
  sort(njp.begin(), njp.end());
  long long ans = 0, last = l - 1;
  for (auto i : njp) {
    ans = max(ans, i - last - 1);
    last = i;
  }
  cout << ans << "\n";
  return 0;
}
