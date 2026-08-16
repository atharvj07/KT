#include <bits/stdc++.h>
using namespace std;
const long long maxL = 20;
long long mod = 1e9 + 7;
long long mod1 = 1e9 + 7;
long long inf = 1e12;
long long linf = 1e18;
const long long maxn = 1e5 + 100;
const long long maxk = 210;
const long long baze = 330;
vector<pair<long long, long long> > vc;
long long n, a[maxn], b[maxn], dp[maxn];
long long saghf(long long x, long long y) {
  if (y < 0) y = -y, x = -x;
  return (x + y - 1) / y;
}
long long when(long long i, long long j) {
  return saghf(dp[i] - dp[j], b[j] - b[i]);
}
void add(long long x) {
  while (((long long)((vc).size())) and
         when(vc.back().second, x) <= vc.back().first)
    vc.pop_back();
  if (((long long)((vc).size())))
    vc.push_back(pair<long long, long long>(when(vc.back().second, x), x));
  else
    vc.push_back(pair<long long, long long>(0, x));
}
long long get(long long x) {
  return (--lower_bound((vc).begin(), (vc).end(),
                        pair<long long, long long>(x + 1, 0)))
      ->second;
}
int32_t main() {
  cin >> n;
  for (long long i = 0; i < n; i++) cin >> a[i];
  for (long long i = 0; i < n; i++) cin >> b[i];
  add(0);
  for (long long i = 1; i < n; i++) {
    long long j = get(a[i]);
    dp[i] = dp[j] + a[i] * b[j];
    add(i);
  }
  cout << dp[n - 1] << endl;
}
