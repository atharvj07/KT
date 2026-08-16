#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int MAX = 2e5 + 7;
const int eps = -1e9;
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
long long lcm(long long a, long long b) { return a * b / gcd(a, b); }
bool isPrime(long long n) {
  if (n < 2) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  for (int i = 5; i * i <= n; i += 6)
    if (n % i == 0 || n % (i + 2) == 0) return false;
  return true;
}
long long powOfn(long long b, long long p) {
  if (p == 0) return 1;
  long long sq = powOfn(b, p / 2);
  sq *= sq;
  if (p & 1) sq *= b;
  return sq;
}
long long ncr(long long n, long long r) {
  if (n <= 0) return 0;
  long long ans = 1;
  if (n - r < r) r = n - r;
  for (long long i = 0; i < r; i++) {
    ans *= n - i;
    ans /= i + 1;
  }
  return ans;
}
int dx[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dy[] = {1, -1, 0, 0, 1, 1, -1, -1};
unsigned long long power(unsigned long long x, unsigned long long y,
                         unsigned long long m) {
  if (y == 0) return 1;
  unsigned long long p = power(x, y / 2, m) % m;
  p = (p * p) % m;
  return (y % 2 == 0) ? p : (x * p) % m;
}
int main() {
  ios_base::sync_with_stdio(NULL), cout.tie(NULL), cin.tie(NULL);
  long long n, k;
  cin >> n >> k;
  vector<bool> v(n + 1, 1);
  for (int i = 2; i * i <= n; i++) {
    if (v[i]) {
      for (int j = i * i; j <= n; j += i) v[j] = 0;
    }
  }
  long long ans = 0;
  vector<pair<int, int>> v2;
  for (int i = 2; i <= n; i++) {
    if (v[i]) {
      int j = i + 1;
      while (j < n && v[j] == 0) j++;
      if (v[j]) {
        if (v[i + j + 1] && i + j <= n) {
          ans++;
        }
      }
      i = j - 1;
    }
  }
  cout << (ans >= k ? "YES" : "NO") << endl;
  return 0;
}
