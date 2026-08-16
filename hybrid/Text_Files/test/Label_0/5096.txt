#include <bits/stdc++.h>
using namespace std;
int main() {
  unsigned long long ans = 1e18, n, k;
  cin >> n >> k;
  vector<unsigned long long> v;
  for (unsigned long long i = 1; i <= n; i++)
    if (n % i == 0) v.push_back(i);
  for (unsigned long long x : v)
    if (x < k) ans = min(ans, (n / x) * k + x);
  cout << ans;
}
