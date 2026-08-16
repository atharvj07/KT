#include <bits/stdc++.h>
using namespace std;
long long n, k, ans = 0;
string s, t;
int main() {
  cin >> n >> k;
  cin >> s;
  cin >> t;
  long long range = 1, l = 0, r = 0;
  for (int i = 0; i < n; ++i) {
    l = (l << 1) + (s[i] - 'a');
    r = (r << 1) + (t[i] - 'a');
    if (range < k) {
      range = min(k, r - l + 1);
    }
    ans += range;
  }
  printf("%lld\n", ans);
}
