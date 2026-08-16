#include <bits/stdc++.h>
using namespace std;
unsigned long long mod = 1e9 + 7;
unsigned long long ncr(long long int n, long long int k) {
  unsigned long long res = 1;
  if (k > n - k) k = n - k;
  for (int i = 0; i < k; ++i) {
    res *= (n - i);
    res /= (i + 1);
    res = res % mod;
  }
  return res % mod;
}
bool prime(unsigned long long num) {
  bool flag = true;
  for (unsigned long long i = 2; i * i <= num; i++) {
    if (num % i == 0) {
      flag = false;
      break;
    }
  }
  return flag;
}
long long ipow(long long base, long long exp) {
  long long result = 1;
  for (;;) {
    if (exp & 1) {
      result *= base;
      result = result % mod;
    }
    exp >>= 1;
    if (!exp) break;
    base *= base;
    base = base % mod;
  }
  return result % mod;
}
long long abs(long long a, long long b) {
  if ((a - b) > 0)
    return (a - b);
  else
    return (b - a);
}
int main() {
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  int n, k;
  cin >> n >> k;
  int mx[n + 1], mn[n + 1];
  memset(mn, -1, sizeof mn);
  memset(mx, -1, sizeof mx);
  for (int i = 0; i < k; i++) {
    int k;
    cin >> k;
    if (mn[k] == -1) mn[k] = i;
    mx[k] = i;
  }
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    if (mn[i] == -1 && i != 1 && i != n)
      ans += 3;
    else if (mn[i] == -1 && (i == 1 || i == n))
      ans += 2;
    else {
      if (i != 1) {
        if (mn[i - 1] == -1)
          ans++;
        else {
          if (mx[i - 1] < mn[i]) ans++;
        }
      }
      if (i != n) {
        if (mn[i + 1] == -1)
          ans++;
        else {
          if (mx[i + 1] < mn[i]) {
            ans++;
          }
        }
      }
    }
  }
  cout << ans;
}
