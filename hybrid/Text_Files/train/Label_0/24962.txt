#include <bits/stdc++.h>
long long mod = 1000000007;
using namespace std;
long long int fast_exp(long long int base, long long int ex) {
  long long int res = 1;
  while (ex > 0) {
    if (ex % 2 == 1) res = (res * base) % mod;
    base = (base * base) % mod;
    ex /= 2;
  }
  return res % mod;
}
long long int gcd(long long int a, long long int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  string s;
  cin >> s;
  long long n = s.length();
  vector<long long> v;
  long long cu = 0;
  for (int i = 0; i < n; i++) {
    if (s[i] == 'b') {
      if (cu != 0) v.push_back(cu);
      cu = 0;
      continue;
    }
    if (s[i] == 'a') cu++;
  }
  if (cu) v.push_back(cu);
  if (v.size() == 0) {
    cout << "0\n";
    return 0;
  }
  long long ans = 1;
  for (int i = 0; i < v.size(); i++) {
    long long h = v[i] + 1;
    ans *= h;
    ans %= mod;
  }
  ans--;
  if (ans < 0) ans += mod;
  ans %= mod;
  cout << ans << "\n";
  return 0;
}
