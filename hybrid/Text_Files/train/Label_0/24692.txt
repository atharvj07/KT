#include <bits/stdc++.h>
using namespace std;
int nxi() {
  int a;
  cin >> a;
  return a;
}
vector<long long> a;
void inc(int i, int v) {
  for (; i < a.size(); i |= i + 1) {
    a[i] += v;
  }
}
long long get(int r) {
  long long ans = 0;
  for (; r >= 0; r = (r & (r + 1)) - 1) {
    ans += a[r];
  }
  return ans;
}
long long get(int l, int r) { return get(r) - get(l - 1); }
int gcd(int a, int b) { return a == 0 ? b : gcd(b % a, a); }
long long phi(long long n) {
  long long result = n;
  for (long long i = 2; i * i <= n; ++i)
    if (n % i == 0) {
      while (n % i == 0) n /= i;
      result -= result / i;
    }
  if (n > 1) result -= result / n;
  return result;
}
int main() {
  long long n, k;
  cin >> n >> k;
  if (k % 2 == 0) --k;
  while (k > 1 && n > 1) {
    n = phi(n);
    k -= 2;
  }
  cout << (phi(n) % 1000000007);
  return 0;
}
