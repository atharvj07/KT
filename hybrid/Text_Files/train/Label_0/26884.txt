#include <bits/stdc++.h>
using namespace std;
const int mod = 1000;
const int maxn = 120;
template <class T>
inline bool scan_d(T &ret) {
  char c;
  int sgn;
  if (c = getchar(), c == EOF) return 0;
  while (c != '-' && (c < '0' || c > '9')) c = getchar();
  sgn = (c == '-') ? -1 : 1;
  ret = (c == '-') ? 0 : (c - '0');
  while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c - '0');
  ret *= sgn;
  return 1;
}
inline void out(long long x) {
  if (x > 9) out(x / 10);
  putchar(x % 10 + '0');
}
char s[10000];
int main() {
  int n, m;
  int t = 0;
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; ++i) putchar('1');
  puts("");
  for (int i = 0; i < n - 1; ++i) putchar('8');
  putchar('9');
  return 0;
}
