#include <bits/stdc++.h>
using namespace std;
const uint64_t seed =
    std::chrono::system_clock::now().time_since_epoch().count();
mt19937_64 rnd(seed);
const int MOD = 998244353;
const char NL = '\n';
using LL = long long;
void solve(int caseNum) {
  int n;
  cin >> n;
  vector<pair<int, int>> pp;
  for (int i = 0; i <= n; i++) {
    int x, y;
    cin >> x >> y;
    pp.push_back({x, y});
  }
  int TT = 32;
  vector<double> sum(n + 1, 0);
  auto getDis = [](double x1, double y1, double x2, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
  };
  for (int i = 1; i <= n; i++) {
    sum[i] = sum[i - 1] + getDis(pp[i].first, pp[i].second, pp[i - 1].first,
                                 pp[i - 1].second);
  }
  auto getV = [&](double x1, double y1, double x2, double y2, double c1,
                  double c2, double tb, double tb2, double v, bool f) {
    double s = 0.0, e = 1.0;
    double d[4];
    for (int j = 0; j < 4; j++) {
      double t = (s * (3 - j) + e * j) / 3;
      double dd = getDis(c1, c2, x1 * (1 - t) + x2 * t, y1 * (1 - t) + y2 * t);
      double d2 = (tb + tb2 * t) / v;
      d[j] = dd - d2;
    }
    for (int i = 0; i < TT; i++) {
      if (e - s < 5e-7) break;
      double m1 = (s * 2 + e) / 3;
      double m2 = (s + e * 2) / 3;
      for (int j = 1; j < 3; j++) {
        double t = (s * (3 - j) + e * j) / 3;
        double dd =
            getDis(c1, c2, x1 * (1 - t) + x2 * t, y1 * (1 - t) + y2 * t);
        double d2 = (tb + tb2 * t) / v;
        d[j] = dd - d2;
        if (d[j] < 0 && f) return d[j];
      }
      if (d[0] > d[1] && d[1] > d[2]) {
        s = m1;
        d[0] = d[1];
      } else {
        e = m2;
        d[3] = d[2];
      }
    }
    double m = (s + e) / 2;
    double dd = getDis(c1, c2, x1 * (1 - m) + x2 * m, y1 * (1 - m) + y2 * m);
    double d2 = (tb + tb2 * m) / v;
    return dd - d2;
  };
  auto getRange = [&](double x1, double y1, double x2, double y2, double xx1,
                      double xx2, double yy1, double yy2, double tb, double tb1,
                      double tb2, double sv) {
    double s = 0.0, e = 1.0;
    double b1 = 1, b2 = 0;
    for (int i = 0; i < TT; i++) {
      if (e - s < 5e-7) break;
      double d[4];
      for (int j = 0; j < 4; j++) {
        double m1 = (s * (3 - j) + e * j) / 3;
        d[j] = getV(xx1, xx2, yy1, yy2, x1 * (1 - m1) + x2 * m1,
                    y1 * (1 - m1) + y2 * m1, tb + tb1 * m1, tb2, sv, false);
        if (d[j] < 0) {
          b1 = min(b1, m1);
          b2 = max(b2, m1);
        }
      }
      if (d[0] > d[1] && d[1] > d[2])
        s = (s * 2 + e) / 3;
      else
        e = (s + e * 2) / 3;
    }
    double m = (s + e) / 2;
    double vv = getV(xx1, xx2, yy1, yy2, x1 * (1 - m) + x2 * m,
                     y1 * (1 - m) + y2 * m, tb + tb1 * m, tb2, sv, false);
    if (vv > 0)
      return make_pair(1.0, 0.0);
    else {
      s = 0, e = b1;
      for (int i = 0; i < TT; i++) {
        if (e - s < 5e-7) break;
        double mid = (s + e) / 2;
        double v =
            getV(xx1, xx2, yy1, yy2, x1 * (1 - mid) + x2 * mid,
                 y1 * (1 - mid) + y2 * mid, tb + tb1 * mid, tb2, sv, true);
        if (v <= 0)
          e = mid;
        else
          s = mid;
      }
      double left = (s + e) / 2;
      s = b2, e = 1;
      for (int i = 0; i < TT; i++) {
        if (e - s < 5e-7) break;
        double mid = (s + e) / 2;
        double v =
            getV(xx1, xx2, yy1, yy2, x1 * (1 - mid) + x2 * mid,
                 y1 * (1 - mid) + y2 * mid, tb + tb1 * mid, tb2, sv, true);
        if (v <= 0)
          s = mid;
        else
          e = mid;
      }
      double right = (s + e) / 2;
      return make_pair(left, right);
    }
  };
  auto check = [&](double m) {
    vector<pair<double, double>> r1, r2;
    for (int i = 1; i < n; i++) {
      vector<pair<double, double>> r1, r2;
      for (int j = 0; j < i; j++) {
        auto r = getRange(pp[i].first, pp[i].second, pp[i + 1].first,
                          pp[i + 1].second, pp[j + 1].first, pp[j + 1].second,
                          pp[j].first, pp[j].second, sum[i] - sum[j + 1],
                          sum[i + 1] - sum[i], sum[j + 1] - sum[j], m);
        if (r.first <= r.second) {
          r1.push_back(r);
        }
      }
      for (int j = i + 1; j < n; j++) {
        auto r = getRange(
            pp[i + 1].first, pp[i + 1].second, pp[i].first, pp[i].second,
            pp[j].first, pp[j].second, pp[j + 1].first, pp[j + 1].second,
            sum[j] - sum[i + 1], sum[i + 1] - sum[i], sum[j + 1] - sum[j], m);
        if (r.first <= r.second) {
          r2.push_back({1 - r.second, 1 - r.first});
        }
      }
      sort(r1.begin(), r1.end());
      sort(r2.begin(), r2.end());
      int p1 = 0, p2 = 0;
      while (p1 < r1.size() && p2 < r2.size()) {
        if (max(r1[p1].first, r2[p2].first) <=
            min(r1[p1].second, r2[p2].second))
          return true;
        if (r1[p1] < r2[p2])
          p1++;
        else
          p2++;
      }
    }
    return false;
  };
  double ss = 1, ee = 1010;
  for (int i = 0; i < 40; i++) {
    if (ee - ss < 1e-7) break;
    double m = (ss + ee) / 2;
    if (check(m))
      ss = m;
    else
      ee = m;
  }
  cout << (ss + ee) / 2 << endl;
}
int main() {
  clock_t beg = clock();
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.precision(10);
  int T = 1;
  for (int i = 1; i <= T; i++) {
    solve(i);
  }
  cout.flush();
  ;
  return 0;
}
