#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization("unroll-loops")
long long int power(long long int x, long long int n) {
  long long int result = 1;
  while (n) {
    if (n % 2 == 1) result = result * x;
    n = n / 2;
    x = x * x;
  }
  return result;
}
long long int gcd(long long int a, long long int b) {
  if (!b) return a;
  return gcd(b, a % b);
}
long long int lcm(long long int a, long long int b) {
  return (a * b) / gcd(a, b);
}
long long int BS(long long int a[], long long int s, long long int n,
                 long long int val) {
  long long int mid, beg = s, end = n - 1;
  while (beg <= end) {
    mid = (beg + end) / 2;
    if (val == a[mid]) {
      break;
    } else if (val > a[mid]) {
      beg = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return mid;
}
inline long long int mul(long long int x, long long int y, long long int m) {
  long long int z = 1LL * x * y;
  if (z >= m) {
    z %= m;
  }
  return z;
}
long long int powmod(long long int x, long long int y, long long int m) {
  long long int r = 1;
  while (y) {
    if (y & 1) {
      r = mul(r, x, m);
    }
    y >>= 1;
    x = mul(x, x, m);
  }
  return r;
}
using namespace std;
void start() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ;
}
int main() {
  start();
  long long int t;
  cin >> (t);
  while (t--) {
    long long int n;
    cin >> n;
    string s;
    cin >> s;
    long long int c = 0;
    for (long long int i = 1; i < n; i++) {
      if (s[i] == s[i - 1]) c++;
    }
    cout << (c + 1) / 2 << "\n";
  }
  return 0;
}
