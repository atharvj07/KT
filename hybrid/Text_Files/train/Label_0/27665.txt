#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
int main() {
  long long n, k, cnt = 0, a, g;
  cin >> n >> k;
  g = k;
  for (long long i = 0; i < n; ++i) cin >> a, g = gcd(a, g);
  vector<long long> r;
  for (long long i = 0; i < k; i += g) r.push_back(i);
  cout << r.size() << '\n';
  for (long long i : r) cout << i << ' ';
}
