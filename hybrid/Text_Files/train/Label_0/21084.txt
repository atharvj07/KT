#include <bits/stdc++.h>
using namespace std;
bool desc(long long i, long long j) { return i > j; }
long long d, x, y;
void gcd(long long A, long long B) {
  if (B == 0) {
    d = A;
    x = 1;
    y = 0;
  } else {
    gcd(B, A % B);
    long long temp = x;
    x = y;
    y = temp - (A / B) * y;
  }
}
long long power(long long x, long long n) {
  if (n == 0)
    return 1;
  else if (n % 2 == 0)
    return power((x * x) % 1000000007, n / 2);
  else
    return (x * power((x * x) % 1000000007, (n - 1) / 2)) % 1000000007;
}
long long ar[2009], not_prime[1100009], dp[2009], vis[2009];
void sieve() {
  not_prime[1] = 1;
  not_prime[0] = 1;
  for (long long p = 2; p * p <= 1100009; p++) {
    if (!not_prime[p]) {
      for (long long i = p * 2; i <= 1100009; i += p) not_prime[i] = 1;
    }
  }
}
long long modi(long long i) {
  gcd(i, 1000000007);
  return (x % 1000000007 + 1000000007) % 1000000007;
}
int main() {
  long long i, j, k, a, b, c, t, n, flag;
  string sk, s1, s2;
  char ch;
  cin >> s1 >> s2;
  map<char, char> mv;
  for (i = 0; i < s1.size(); i++) {
    mv[s1[i]] = s2[i];
    mv[char(s1[i] - 32)] = char(s2[i] - 32);
  }
  cin >> sk;
  for (i = 0; i < sk.size(); i++) {
    if ((sk[i] >= 65 && sk[i] <= 90) || (sk[i] >= 97 && sk[i] <= 122))
      cout << mv[sk[i]];
    else
      cout << sk[i];
  }
  return 0;
}
