#include <bits/stdc++.h>
using namespace std;
const int mod = 1000000007;
long long qpow(long long n, long long k) {
  long long ans = 1;
  assert(k >= 0);
  n %= mod;
  while (k > 0) {
    if (k & 1) ans = (ans * n) % mod;
    n = (n * n) % mod;
    k >>= 1;
  }
  return ans % mod;
}
long long n, b;
vector<pair<long long, long long> > di;
int main() {
  cin >> n >> b;
  long long rem = b;
  for (long long i = 2; i * i <= b; i++) {
    long long x = i;
    int cnt = 0;
    while (rem % x == 0) {
      rem /= x;
      cnt++;
    }
    if (cnt) di.push_back({i, cnt});
  }
  if (rem > 1) di.push_back({rem, 1});
  long long ret = -1;
  for (int i = 0; i < di.size(); i++) {
    long long curr = 0;
    long long tmp = n / di[i].first;
    while (tmp) {
      curr += tmp;
      tmp /= di[i].first;
    }
    curr /= di[i].second;
    if (ret == -1 or curr < ret) ret = curr;
  }
  cout << ret << endl;
  return 0;
}
