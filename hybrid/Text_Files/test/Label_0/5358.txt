#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3fffffff;
const int SINF = 0x7fffffff;
const long long LINF = 0x3fffffffffffffff;
const long long SLINF = 0x7fffffffffffffff;
long long n;
void init();
void input();
void work();
void divi(long long xl, long long xu, long long xr, long long yl, long long yu,
          long long yr, int d);
int query(long long x, long long y) {
  cout << x << " " << y << endl;
  int ret;
  cin >> ret;
  if (!ret) exit(0);
  return ret;
}
int main() {
  init();
  input();
  work();
}
void init() { ios::sync_with_stdio(false); }
void input() { cin >> n; }
void work() { divi(1, -1, n, 1, -1, n, 0); }
void divi(long long xl, long long xu, long long xr, long long yl, long long yu,
          long long yr, int d) {
  if (xu == -1 && yu == -1) {
    xu = (xl + xr) >> 1, yu = (yl + yr) >> 1;
    int ret = query(xu, yu);
    if (ret == 1)
      divi(xu + 1, -1, xr, yl, -1, yr, d ^ 1);
    else if (ret == 2)
      divi(xl, -1, xr, yu + 1, -1, yr, d ^ 1);
    else
      divi(xl, xu, xr, yl, yu, yr, d ^ 1);
  }
  if (xu <= xl) divi(xl, -1, xr, yl, -1, yu - 1, d);
  if (yu <= yl) divi(xl, -1, xu - 1, yl, -1, yr, d);
  long long xm = xu, ym = yu;
  if (!d)
    xm = (xl + xu - 1) >> 1;
  else
    ym = (yl + yu - 1) >> 1;
  int ret = query(xm, ym);
  if (ret == 1)
    divi(xm + 1, xu, xr, yl, yu, yr, d ^ 1);
  else if (ret == 2)
    divi(xl, xu, xr, ym + 1, yu, yr, d ^ 1);
  else
    divi(xl, xm, xr, yl, ym, yr, d ^ 1);
}
