#include <bits/stdc++.h>
using namespace std;
template <class _Tp>
_Tp gcd(_Tp a, _Tp b) {
  return (b == 0) ? (a) : (gcd(b, a % b));
}
const int inf = 1000000000;
const long long Inf = 1000000000000000000ll;
const int N = 2050;
struct node {
  double l, r, y;
} seg[N];
int n;
vector<pair<double, int> > angs;
vector<double> res;
double calc(double k) {
  double mn = 1.0 * Inf, mx = -1.0 * Inf;
  for (int i = 1; i <= n; ++i) {
    double t = seg[i].y * k;
    mn = min(mn, seg[i].l + t);
    mx = max(mx, seg[i].r + t);
  }
  return mx - mn;
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i)
    scanf("%lf%lf%lf", &seg[i].l, &seg[i].r, &seg[i].y);
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= n; ++j) {
      if (seg[i].y > seg[j].y) {
        double delta = seg[i].y - seg[j].y;
        angs.push_back(pair<double, int>((seg[j].l - seg[i].r) / delta, 1));
        angs.push_back(pair<double, int>((seg[j].r - seg[i].l) / delta, -1));
      }
    }
  if (angs.empty()) {
    printf("%.10lf\n", calc(0));
    return 0;
  }
  sort(angs.begin(), angs.end());
  for (int i = 0, cnt = 0; i < angs.size(); ++i) {
    if (angs[i].second == 1 && cnt == 0) res.push_back(angs[i].first);
    if (angs[i].second == -1 && cnt == 1) res.push_back(angs[i].first);
    cnt += angs[i].second;
  }
  int l = 0, r = res.size() - 1;
  double ans = 1.0 * Inf;
  while (l <= r) {
    int l1 = (l + l + r) / 3, r1 = (l + r + r) / 3;
    double lans = calc(res[l1]), rans = calc(res[r1]);
    ans = min(ans, min(lans, rans));
    if (lans < rans)
      r = r1 - 1;
    else
      l = l1 + 1;
  }
  printf("%.10lf\n", ans);
  return 0;
}
