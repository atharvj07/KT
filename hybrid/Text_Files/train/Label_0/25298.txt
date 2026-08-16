#include <bits/stdc++.h>
using namespace std;
int inf = 1000000005;
long long int llinf = 2000000000000000005LL;
long long int mod = 1000000007;
long long int mod9 = 1000000009;
double pi = 3.1415926535897;
double eps = 1e-15;
int dx[] = {1, -1, 0, 0, 1, -1, 1, -1}, dy[] = {0, 0, 1, -1, 1, 1, -1, -1};
vector<bool> isprime;
vector<int> primes;
void seive(int n, bool wantlist = true) {
  isprime.resize(n + 1, true);
  isprime[0] = isprime[1] = false;
  int sq = sqrt(n + 1);
  for (int i = 2; i < sq + 1; i++) {
    if (isprime[i]) {
      for (int j = i * i; j <= n; j += i) isprime[j] = false;
    }
  }
  for (int i = 2; wantlist && i <= n; i++) {
    if (isprime[i]) primes.push_back(i);
  }
}
template <class T>
inline T gcd(T a, T b) {
  while (b > 0) {
    a %= b;
    swap(a, b);
  }
  return a;
}
template <class T>
inline T lcm(T a, T b) {
  return a * b / gcd(a, b);
}
template <class T>
inline vector<T> operator+(vector<T>& a, vector<T>& b) {
  assert(a.size() == b.size());
  int n = a.size();
  vector<T> c(n);
  for (int i = 0; i < n; i++) c[i] = a[i] + b[i];
  return c;
}
int fastMax(int x, int y) { return (((y - x) >> (32 - 1)) & (x ^ y)) ^ y; }
inline long long int bexp(long long int x, long long int n,
                          long long int m = mod) {
  long long int res = 1;
  x %= m;
  while (n) {
    if (n & 1) res = res * x % m;
    x = x * x % m;
    n >>= 1;
  }
  return res;
}
inline bool ispalin(string& str) {
  int n = str.length();
  for (int i = 0; i < n / 2; i++)
    if (str[i] != str[n - i - 1]) return false;
  return true;
}
int main() {
  int a, b, x1, y1, x2, y2;
  int x, y;
  cin >> a >> b >> x1 >> y1 >> x2 >> y2;
  x = x1;
  y = y1;
  x1 = x + y;
  y1 = y - x;
  x = x2;
  y = y2;
  x2 = x + y;
  y2 = y - x;
  a *= 2;
  b *= 2;
  x1 = x1 / a + (x1 > 0);
  x2 = x2 / a + (x2 > 0);
  y1 = y1 / b + (y1 > 0);
  y2 = y2 / b + (y2 > 0);
  cout << max(abs(y2 - y1), abs(x2 - x1)) << endl;
}
