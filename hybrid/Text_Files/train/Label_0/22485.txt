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
const double eps = 1e-14;
const int maxq = 100100;
const int maxabs = 1000000;
int qn;
long long m;
int n;
int a[maxq + 5], b[maxq + 5];
double rat[maxq + 5];
set<pair<int, int> > all;
int main() {
  scanf(
      "%d%"
      "ll"
      "d",
      &qn, &m);
  n = 0;
  int lst = 0;
  for (int i = (1), i_end_ = (qn + 1); i < i_end_; ++i) {
    int ty, first, second;
    scanf("%d%d%d", &ty, &first, &second);
    (first += lst) %= maxabs;
    (second += lst) %= maxabs;
    ++first, ++second;
    if (ty == 1) {
      a[n] = first, b[n] = second;
      rat[n] = (double)a[n] / b[n];
      auto to_add = make_pair(a[n], n);
      if (all.empty())
        all.insert(to_add);
      else {
        auto tmp = all.lower_bound(to_add);
        auto from = tmp, to = tmp;
        if (to == all.end() || rat[to->second] < rat[n]) {
          while (from != all.begin()) {
            --from;
            if (rat[from->second] > rat[n]) {
              ++from;
              break;
            }
          }
          all.erase(from, to);
          all.insert(to_add);
        }
      }
      ++n;
    } else {
      if (all.empty()) {
        puts("NO");
        continue;
      }
      int r = second / first;
      auto tmp = all.upper_bound(make_pair(r, oo));
      double ans = 0;
      if (tmp == all.begin()) {
        double t = min((double)first, (double)m / b[tmp->second]);
        ans = t * a[tmp->second];
      } else if (tmp == all.end()) {
        --tmp;
        double t = min((double)first, (double)m / b[tmp->second]);
        ans = t * a[tmp->second];
      } else {
        auto pre = tmp;
        --pre;
        int a0 = a[pre->second], a1 = a[tmp->second];
        int b0 = b[pre->second], b1 = b[tmp->second];
        double t0 = 0, t1 = 0;
        if ((long long)b0 * first > m)
          t0 = (double)m / b0, t1 = 0;
        else if ((long long)b1 * first <= m)
          t0 = 0, t1 = first;
        else {
          t0 = double(m - (long long)b1 * first) / (b0 - b1);
          t1 = first - t0;
        }
        ans = t0 * a0 + t1 * a1;
      }
      bool ret = (ans / second > (1 - eps));
      if (ret)
        puts("YES"), lst = i;
      else
        puts("NO");
    }
  }
  return 0;
}
