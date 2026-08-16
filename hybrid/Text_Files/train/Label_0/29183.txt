#include <bits/stdc++.h>
using namespace std;
const int maxN = 5 * 10000 + 10, mod = (int)1e9 + 7;
int n;
long double k = 0, s = 0, lll, pp;
int p[maxN], l[maxN];
pair<int, int> c[maxN];
bool cmp(pair<int, int> x, pair<int, int> y) {
  double xxx, yyy;
  if (x.second != 100)
    xxx = (double)(x.first * x.second) / (100 - x.second);
  else
    return 1;
  if (y.second != 100)
    yyy = (double)(y.first * y.second) / (100 - y.second);
  else
    return 0;
  return xxx > yyy;
}
int main(void) {
  ios_base::sync_with_stdio(0);
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> c[i].first >> c[i].second;
  sort(c, c + n, cmp);
  for (int i = 0; i < n; ++i) {
    lll = (double)c[i].first;
    pp = (double)c[i].second;
    s += lll;
    s += (k * (100 - pp)) / 100;
    k += (lll * pp) / 100;
  }
  printf("%.9lf", s);
  return 0;
}
