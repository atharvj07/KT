#include <bits/stdc++.h>
using namespace std;
long long const M = 1e6 + 10, M2 = 1e3 + 10, mod = 1e9 + 7, inf = 1e18 + 10;
long long a[M], suf[M], pre[M], n, t = 0;
pair<pair<long double, long long>, pair<long long, long long> > ans =
    make_pair(make_pair((long double)-inf, -inf), make_pair(-inf, -inf));
long double check(long long x, long long ind) {
  long long len = n - x + 1;
  long double tmp = ((long double)pre[ind] - (long double)pre[ind - len - 1]);
  tmp += (long double)suf[x];
  tmp /= (len * 2 + 1);
  tmp -= ((long double)a[ind]);
  return tmp;
}
long double check2(long long x, long long ind) {
  long long len = n - x + 1;
  long double tmp =
      ((long double)pre[ind] - (long double)pre[max(ind - len - 2, t)]);
  tmp += (long double)suf[x];
  tmp /= (long double)(len * 2 + 2);
  tmp -= ((((long double)a[ind] + (long double)a[ind - 1]) / (long double)2));
  return tmp;
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  for (long long i = 1; i <= n; i++) cin >> a[i], a[i] *= 2;
  sort(a + 1, a + n + 1);
  for (long long i = 1; i <= n; i++) {
    pre[i] = pre[i - 1] + a[i];
  }
  for (long long i = n; i >= 1; i--) suf[i] = suf[i + 1] + a[i];
  for (long long i = 1; i <= n; i++) {
    long long lo = i + 1;
    long long hi = n + 1;
    lo = max(lo, n - i + 2);
    while (hi > lo + 2) {
      long long m1 = (lo + 2 * hi) / 3;
      long long m2 = (2 * lo + hi) / 3;
      if (check(m1, i) > check(m2, i)) {
        lo = m2 + 1;
      } else
        hi = m1 - 1;
    }
    long long good = 0;
    long double all = (long double)-inf;
    for (long long j = lo; j <= hi; j++) {
      if (check(j, i) > all) all = check(j, i), good = j;
    }
    if (all > ans.first.first)
      ans.first.first = all, ans.first.second = i, ans.second.first = 0,
      ans.second.second = good;
    if (i == 1) continue;
    lo = i + 1;
    hi = n + 1;
    lo = max(lo, n - i + 3);
    while (hi > lo + 2) {
      long long m1 = (lo + 2 * hi) / 3;
      long long m2 = (2 * lo + hi) / 3;
      if (check2(m1, i) > check2(m2, i)) {
        lo = m2 + 1;
      } else
        hi = m1 - 1;
    }
    good = 0;
    all = (long double)-inf;
    for (long long j = lo; j <= hi; j++) {
      if (check2(j, i) >= all) all = check2(j, i), good = j;
    }
    if (all >= ans.first.first)
      ans.first.first = all, ans.first.second = i, ans.second.first = i - 1,
      ans.second.second = good;
  }
  long long len = n - ans.second.second + 1;
  if (ans.second.first)
    cout << len * 2 + 2 << endl;
  else
    cout << len * 2 + 1 << endl;
  if (!ans.second.first) ans.second.first = ans.first.second;
  for (long long i = ans.second.first - len; i <= ans.second.first; i++)
    cout << a[i] / 2 << " ";
  if (ans.second.first != ans.first.second)
    cout << a[ans.first.second] / 2 << " ";
  for (long long i = n - len + 1; i <= n; i++) cout << a[i] / 2 << " ";
}
