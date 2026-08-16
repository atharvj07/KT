#include <bits/stdc++.h>
#pragma GCC optimize(2)
#pragma GCC optimize("Ofast", "unroll-loops", "omit-frame-pointer", "inline")
using namespace std;
const long long INF = 1e18;
const int maxn = 1e6 + 6;
const int mod = 1e9 + 7;
const double eps = 1e-15;
inline bool read(long long &num) {
  char in;
  bool IsN = false;
  in = getchar();
  if (in == EOF) return false;
  while (in != '-' && (in < '0' || in > '9')) in = getchar();
  if (in == '-') {
    IsN = true;
    num = 0;
  } else
    num = in - '0';
  while (in = getchar(), in >= '0' && in <= '9') {
    num *= 10, num += in - '0';
  }
  if (IsN) num = -num;
  return true;
}
long long n, m;
int cnt[maxn];
int main() {
  read(n);
  long long max1 = 0, max2 = 0;
  for (int i = 1; i <= n; i++) {
    long long x;
    read(x);
    if (x > max1)
      cnt[x]--;
    else if (x > max2)
      cnt[max1]++;
    if (x > max1) {
      max2 = max1;
      max1 = x;
    } else if (x > max2)
      max2 = x;
  }
  long long maxl = cnt[1], pos = 1;
  for (int i = 2; i <= n; i++) {
    if (maxl < cnt[i]) {
      maxl = cnt[i];
      pos = i;
    }
  }
  printf("%d\n", pos);
  return 0;
}
