#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline bool chkmin(T &a, const T &b) {
  return a > b ? a = b, 1 : 0;
}
template <typename T>
inline bool chkmax(T &a, const T &b) {
  return a < b ? a = b, 1 : 0;
}
const int oo = 0x3f3f3f3f;
const int __buffsize = 100000;
char __buff[__buffsize];
char *__buffs, *__buffe;
template <typename T>
inline T &Read(T &first) {
  static char c;
  while (1) {
    c = (__buffs == __buffe ? fread(__buff, 1, __buffsize, stdin),
         __buffe = __buff + __buffsize, *((__buffs = __buff)++) : *(__buffs++));
    if (c == '-' || (c >= '0' && c <= '9')) break;
  }
  bool flag = c == '-';
  first = flag ? 0 : c - '0';
  while (1) {
    c = (__buffs == __buffe ? fread(__buff, 1, __buffsize, stdin),
         __buffe = __buff + __buffsize, *((__buffs = __buff)++) : *(__buffs++));
    if (c < '0' || c > '9') break;
    (first *= 10) += c - '0';
  }
  if (flag) first = -first;
  return first;
}
const int Mod = 1e9 + 7;
const int maxn = 100000, maxm = 100000;
int n, m;
long long a[maxn + 5];
long long b[maxm + 5];
inline long long calc(int first, int l, int r) {
  if (b[l] >= a[first]) return b[r] - a[first];
  if (b[r] <= a[first]) return a[first] - b[l];
  return min(((a[first] - b[l]) << 1) + (b[r] - a[first]),
             ((a[first] - b[l]) + ((b[r] - a[first]) << 1)));
}
inline bool work(long long first) {
  int j = 0;
  for (int i = (0), _end_ = (n); i < _end_; ++i) {
    int k = j;
    while (k < m && calc(i, j, k) <= first) ++k;
    j = k;
  }
  return j == m;
}
int main() {
  Read(n), Read(m);
  for (int i = (0), _end_ = (n); i < _end_; ++i) Read(a[i]);
  for (int i = (0), _end_ = (m); i < _end_; ++i) Read(b[i]);
  long long l = 0, r = 20000000000LL;
  while (l < r) {
    long long mid = (l + r) >> 1;
    if (!work(mid))
      l = mid + 1;
    else
      r = mid;
  }
  printf("%I64d\n", l);
  return 0;
}
