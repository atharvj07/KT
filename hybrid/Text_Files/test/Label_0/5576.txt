#include <bits/stdc++.h>
using namespace std;
long long prime[200001];
vector<long long> v[200001];
long long p(long long a, long long b) {
  long long res = 1;
  while (b) {
    if (b % 2) res *= a;
    a *= a;
    b /= 2;
  }
  return res;
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  long long n;
  cin >> n;
  for (long long i = 0; i <= 200000; i++) prime[i] = 1;
  for (long long i = 2; i <= 200000; i++) {
    if (prime[i]) {
      for (long long j = 2 * i; j <= 200000; j += i) prime[j] = 0;
    }
  }
  vector<long long> a(n + 1);
  for (long long i = 1; i <= n; i++) cin >> a[i];
  for (long long i = 1; i <= n; i++) {
    for (long long j = 2; j * j <= a[i]; j++) {
      long long count = 0;
      while (a[i] % j == 0) {
        count++;
        a[i] /= j;
      }
      if (count != 0) v[j].push_back(count);
    }
    if (a[i] > 1) v[a[i]].push_back(1);
  }
  long long ans = 1;
  for (long long i = 2; i <= 200000; i++) {
    if (prime[i]) {
      sort(v[i].begin(), v[i].end());
      long long x = v[i].size();
      long long zero = n - x;
      if (zero >= 2) continue;
      if (x == 1 || zero > 0) {
        ans *= p(i, v[i][0]);
        continue;
      }
      ans *= p(i, v[i][1]);
      continue;
    }
  }
  cout << ans;
}
