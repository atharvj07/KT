#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000000007;
const long long inf = 1e9 + 21;
long long powmod(long long a, long long b) {
  long long res = 1;
  a %= mod;
  assert(b >= 0);
  for (; b; b >>= 1) {
    if (b & 1) res = res * a % mod;
    a = a * a % mod;
  }
  return res;
}
template <typename N>
N gcd(N a, N b) {
  return b ? gcd(b, a % b) : a;
}
void precision(long long pr) {
  cout.precision(pr);
  cout << fixed;
}
const int N = 1e6 + 21;
long long a[N];
vector<long long> v[N], v2;
long long f(long long x) {
  long long l = 0, r = ((int)((v2).size())) - 1;
  while (l < r) {
    long long mid = (l + r) / 2;
    if (v2[mid] < x)
      r = mid;
    else
      l = mid + 1;
    if (r < 0) return 0;
    if (l > ((int)((v2).size())) - 1) return ((int)((v2).size())) - 1;
  }
  return l;
}
int main() {
  long long i, j, k, n, x;
  cin >> n;
  for ((i) = (int)(0); (i) <= (int)(n - 1); (i)++) cin >> a[i];
  for ((i) = (int)(0); (i) <= (int)(n - 1); (i)++) {
    if (((int)((v2).size()))) {
      if (v2[((int)((v2).size())) - 1] >= a[i]) {
        v2.push_back(a[i]);
        v[((int)((v2).size())) - 1].push_back(a[i]);
      } else {
        x = f(a[i]);
        v[x].push_back(a[i]);
        v2[x] = a[i];
      }
    } else {
      v2.push_back(a[i]);
      v[0].push_back(a[i]);
    }
  }
  for ((i) = (int)(0); (i) <= (int)(((int)((v2).size()))); (i)++) {
    for ((j) = (int)(0); (j) <= (int)(((int)((v[i]).size())) - 1); (j)++)
      cout << v[i][j] << " ";
    cout << '\n';
  }
  return 0;
}
