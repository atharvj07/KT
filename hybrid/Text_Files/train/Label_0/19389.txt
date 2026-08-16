#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline void maximize(T &a, T b) {
  if (b > a) a = b;
}
template <typename T>
inline void minimize(T &a, T b) {
  if (b < a) a = b;
}
template <typename T>
inline void xReplace(T v, T &mx, T &sx) {
  if (v > mx)
    sx = mx, mx = v;
  else if (v > sx)
    sx = v;
}
template <typename T>
inline void nReplace(T v, T &mn, T &sn) {
  if (v < mn)
    sn = mn, mn = v;
  else if (v < sn)
    sn = v;
}
inline long long fr() {
  long long ret = 0, sym = 1;
  int c = 0;
  while (!isdigit(c)) sym = c == '-' ? -1 : 1, c = getchar();
  while (isdigit(c)) ret = ret * 10 + c - '0', c = getchar();
  return ret * sym;
}
const int maxn = 5e3 + 5;
const int maxq = 1e5 + 5;
int n, Q, irc[114514];
int dt_d[maxq] = {}, dt_a[maxq] = {};
int dt_x[maxq], dt_y[maxq], dt_l[maxq];
int C[maxn * 2][maxn] = {};
inline void add(int x, int y, int v) {
  for (int i = x; i < maxn * 2; i += ((i) & (-(i)))) {
    for (int j = y; j < maxn; j += ((j) & (-(j)))) {
      C[i][j] += v;
    }
  }
}
inline int getsum(int x, int y) {
  int ret = 0;
  for (int i = x; i; i -= ((i) & (-(i)))) {
    for (int j = y; j; j -= ((j) & (-(j)))) {
      ret += C[i][j];
    }
  }
  return ret;
}
inline void rectadd(int x1, int Y1, int x2, int y2, int v) {
  if (!x2 || !y2) return;
  ++x2, ++y2;
  add(x2, y2, v);
  add(x1, y2, -v);
  add(x2, Y1, -v);
  add(x1, Y1, v);
}
int main() {
  n = fr(), Q = fr();
  for (int i = 1; i <= (Q); ++i) {
    irc[0] = fr();
    if (irc[0] == 1) {
      dt_d[i] = fr(), dt_x[i] = fr(), dt_y[i] = fr(), dt_l[i] = fr();
      if (dt_d[i] == 1)
        rectadd(dt_x[i] + dt_y[i], 1, dt_x[i] + dt_y[i] + dt_l[i], dt_x[i] - 1,
                -1);
      if (dt_d[i] == 4)
        rectadd(dt_x[i] + dt_y[i] - dt_l[i], dt_x[i] + 1, dt_x[i] + dt_y[i], n,
                -1);
    } else {
      dt_x[i] = fr(), dt_y[i] = fr();
      dt_a[i] += getsum(dt_x[i] + dt_y[i], dt_x[i]);
    }
  }
  memset(C, 0, sizeof(C));
  for (int i = 1; i <= (Q); ++i) {
    if (dt_d[i] == 1)
      rectadd(dt_x[i] + dt_y[i], 1, dt_x[i] + dt_y[i] + dt_l[i], dt_y[i] - 1,
              -1);
    if (dt_d[i] == 4)
      rectadd(dt_x[i] + dt_y[i] - dt_l[i], dt_y[i] + 1, dt_x[i] + dt_y[i], n,
              -1);
    if (dt_d[i] == 0) dt_a[i] += getsum(dt_x[i] + dt_y[i], dt_y[i]);
  }
  memset(C, 0, sizeof(C));
  for (int i = 1; i <= (Q); ++i) {
    if (dt_d[i] == 2)
      rectadd(dt_y[i] - dt_x[i] - dt_l[i] + maxn, 1, dt_y[i] - dt_x[i] + maxn,
              dt_x[i] - 1, -1);
    if (dt_d[i] == 3)
      rectadd(dt_y[i] - dt_x[i] + maxn, dt_x[i] + 1,
              dt_y[i] - dt_x[i] + dt_l[i] + maxn, n, -1);
    if (dt_d[i] == 0) dt_a[i] += getsum(dt_y[i] - dt_x[i] + maxn, dt_x[i]);
  }
  memset(C, 0, sizeof(C));
  for (int i = 1; i <= (Q); ++i) {
    if (dt_d[i] == 2)
      rectadd(dt_y[i] - dt_x[i] - dt_l[i] + maxn, dt_y[i] + 1,
              dt_y[i] - dt_x[i] + maxn, n, -1);
    if (dt_d[i] == 3)
      rectadd(dt_y[i] - dt_x[i] + maxn, 1, dt_y[i] - dt_x[i] + dt_l[i] + maxn,
              dt_y[i] - 1, -1);
    if (dt_d[i] == 0) dt_a[i] += getsum(dt_y[i] - dt_x[i] + maxn, dt_y[i]);
  }
  memset(C, 0, sizeof(C));
  for (int i = 1; i <= (Q); ++i) {
    if (dt_d[i] == 1)
      rectadd(dt_x[i] + dt_y[i], 1, dt_x[i] + dt_y[i] + dt_l[i], 1, 1);
    if (dt_d[i] == 2)
      rectadd(dt_y[i] - dt_x[i] - dt_l[i] + maxn, 2, dt_y[i] - dt_x[i] + maxn,
              2, 1);
    if (dt_d[i] == 3)
      rectadd(dt_y[i] - dt_x[i] + maxn, 2, dt_y[i] - dt_x[i] + dt_l[i] + maxn,
              2, 1);
    if (dt_d[i] == 4)
      rectadd(dt_x[i] + dt_y[i] - dt_l[i], 1, dt_x[i] + dt_y[i], 1, 1);
    if (dt_d[i] == 0)
      dt_a[i] +=
          getsum(dt_x[i] + dt_y[i], 1) + getsum(dt_y[i] - dt_x[i] + maxn, 2),
          printf("%d\n", dt_a[i]);
  }
  return 0;
}
