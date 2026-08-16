#include <bits/stdc++.h>
using namespace std;
inline int gi() {
  char c = getchar();
  while (c < '0' || c > '9') c = getchar();
  int sum = 0;
  while ('0' <= c && c <= '9') sum = sum * 10 + c - 48, c = getchar();
  return sum;
}
const int maxn = 5005;
int T, n, m, s, n1, m1, n2, m2, len1, len2, len3, len4;
int sum[maxn * maxn];
int Calc(int x, int t) {
  for (int i = 1; i <= t; ++i) x /= 10;
  return x;
}
long long calc(int N, int M) {
  long long ans = 0;
  ans = (long long)N * Calc(m - 1, s - 1);
  ans += Calc(M, s - 1);
  ans += Calc(N, s - len1 - 1);
  return ans;
}
int main() {
  n = gi();
  m = gi();
  s = gi();
  int tmp;
  tmp = m;
  while (tmp) tmp /= 10, ++len2;
  tmp = m - 1;
  while (tmp) len1 += tmp % 10 != 0, tmp /= 10;
  tmp = n;
  while (tmp) tmp /= 10, ++len3;
  tmp = n - 1;
  while (tmp) len4 += tmp % 10 != 0, tmp /= 10;
  n1 = gi();
  m1 = gi();
  n2 = gi();
  m2 = gi();
  if (n2 > n1 || (n2 == n1 && m1 <= m2))
    printf("%lld\n", calc(n2, m2) - calc(n1, m1));
  else
    printf("%lld\n", calc(n2, m2) + (calc(n - 1, m - 1) - calc(n1, m1)) +
                         (len1 + len4 >= s));
  return 0;
}
