#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T bigmod(T p, T e, T M) {
  long long int ret = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1) ret = (ret * p) % M;
    p = (p * p) % M;
  }
  return (T)ret;
}
template <class T>
inline T gcd(T a, T b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
template <class T>
inline T modinverse(T a, T M) {
  return bigmod(a, M - 2, M);
}
template <class T>
inline T bpow(T p, T e) {
  long long int ret = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1) ret = (ret * p);
    p = (p * p);
  }
  return (T)ret;
}
int toInt(string s) {
  int sm;
  stringstream ss(s);
  ss >> sm;
  return sm;
}
int toLlint(string s) {
  long long int sm;
  stringstream ss(s);
  ss >> sm;
  return sm;
}
int cs, ln, q;
long long int p[2][2][1009][1009], p0[1009][1009];
bool bl0[1009][1009];
char bl[2][2][1009][1009];
char a[1009], b[1009];
long long int dppr(int i, int k) {
  if (i == -1) {
    if (k == 1005) return 1LL;
    return 0;
  }
  long long int &pr = p0[i][k];
  if (bl0[i][k] == 1) return pr;
  bl0[i][k] = 1;
  pr = 0ll;
  int qk;
  for (int j = 0; j <= 9; j++) {
    qk = k;
    if (k != 1005 && (j == 4 || j == 7)) {
      if (k == 1004)
        qk = i;
      else if (qk - i <= q)
        qk = 1005;
      else
        qk = i;
    }
    pr += dppr(i - 1, qk);
    if (pr >= 1000000007LL) pr -= 1000000007LL;
  }
  return pr;
}
long long int qry(bool bg, bool sm, int i, int k) {
  if (i == -1) {
    if (k == 1005) return 1LL;
    return 0;
  }
  long long int &pr = p[bg][sm][i][k];
  if (bl[bg][sm][i][k] == cs) return pr;
  bl[bg][sm][i][k] = cs;
  if (bg == 1 && sm == 1) {
    return pr = dppr(i, k);
  }
  pr = 0ll;
  bool qbg, qsm;
  int l, r, qk;
  l = (bg == 1) ? 0 : (a[i] - '0');
  r = (sm == 1) ? 9 : (b[i] - '0');
  for (int j = l; j <= r; j++) {
    qbg = (bg == 1) ? 1 : (j > l);
    qsm = (sm == 1) ? 1 : (j < r);
    qk = k;
    if (k != 1005 && (j == 4 || j == 7)) {
      if (k == 1004)
        qk = i;
      else if (qk - i <= q)
        qk = 1005;
      else
        qk = i;
    }
    pr += qry(qbg, qsm, i - 1, qk);
    if (pr >= 1000000007LL) pr -= 1000000007LL;
  }
  return pr;
}
int main() {
  cs = 1;
  int t, i, j, k;
  scanf("%d%d", &t, &q);
  while (t--) {
    scanf(" %s %s", a, b);
    j = strlen(a);
    ln = strlen(b);
    reverse(&a[0], &a[j]);
    reverse(&b[0], &b[ln]);
    for (i = j; i < 1003; i++) a[i] = '0';
    for (i = ln; i < 1003; i++) b[i] = '0';
    printf("%I64d\n", qry(0, 0, 1002, 1004));
    cs++;
  }
  return 0;
}
