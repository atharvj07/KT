#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:512000000")
using namespace std;
template <class T>
inline T sqr(T x) {
  return x * x;
}
template <class T>
inline string tostr(const T& x) {
  stringstream ss;
  ss << x;
  return ss.str();
}
inline long long parse(const string& s) {
  stringstream ss(s);
  long long x;
  ss >> x;
  return x;
}
const double EPS = 1e-9;
const int INF = 1000 * 1000 * 1000;
const char CINF = 102;
const long long LINF = INF * 1ll * INF;
const double DINF = 1e200;
const double PI = 3.1415926535897932384626433832795l;
int gcd(int a, int b) { return a ? gcd(b % a, a) : b; }
long long gcd(long long a, long long b) { return a ? gcd(b % a, a) : b; }
long long powmod(long long a, long long p, long long m) {
  long long r = 1;
  while (p) {
    if (p & 1) r = r * a % m;
    p >>= 1;
    a = a * a % m;
  }
  return r;
}
double W, H;
vector<pair<double, double> > A;
double P[1100][1100];
double Q[1100][1100];
bool check(double R, int i0) {
  vector<pair<double, int> > evs;
  int D = 0;
  pair<double, double> v = A[i0];
  if (v.first < R) {
    double a = PI - acos(v.first / R);
    D += 2;
    evs.push_back(make_pair(-a, -2));
    evs.push_back(make_pair(+a, +2));
  }
  if (W - v.first < R) {
    double a = acos((W - v.first) / R);
    evs.push_back(make_pair(-a, +2));
    evs.push_back(make_pair(+a, -2));
  }
  if (v.second < R) {
    double a = acos(v.second / R);
    evs.push_back(make_pair(-PI / 2 - a, +2));
    evs.push_back(make_pair(-PI / 2 + a, -2));
  }
  if (H - v.second < R) {
    double a = acos((H - v.second) / R);
    evs.push_back(make_pair(PI / 2 - a, +2));
    evs.push_back(make_pair(PI / 2 + a, -2));
  }
  for (int i = 0; i < (((int)(A).size())); ++i) {
    if (i == i0 || A[i] == v) continue;
    double d = P[i0][i];
    if (d >= R * 2) continue;
    double a = acos(d / 2 / R);
    double x = Q[i0][i];
    if (x + a > PI) x -= 2 * PI;
    if (x - a < -PI) {
      ++D;
      evs.push_back(make_pair(x + a, -1));
      evs.push_back(make_pair(2 * PI + x - a, +1));
    } else {
      evs.push_back(make_pair(x - a, +1));
      evs.push_back(make_pair(x + a, -1));
    }
  }
  sort((evs).begin(), (evs).end());
  if (D <= 1) return true;
  for (int i = 0; i < (((int)(evs).size())); ++i) {
    D += evs[i].second;
    if (D <= 1) return true;
  }
  return false;
}
int main() {
  int n;
  cin >> W >> H >> n;
  A.resize(n);
  for (int i = 0; i < (n); ++i) {
    cin >> A[i].first >> A[i].second;
  }
  random_shuffle((A).begin(), (A).end());
  for (int i = 0; i < (n); ++i) {
    for (int j = 0; j < (n); ++j) {
      if (i <= j)
        P[i][j] = P[j][i] =
            sqrt(sqr(A[i].first - A[j].first) + sqr(A[i].second - A[j].second));
      if (A[i] != A[j])
        Q[i][j] = atan2(A[j].second - A[i].second, A[j].first - A[i].first);
    }
  }
  double ans = 0;
  for (int i0 = 0; i0 < (((int)(A).size())); ++i0) {
    double a = ans, b = sqrt(sqr(H) + sqr(W));
    if (!check(a + EPS, i0)) continue;
    for (int qqq = 0; qqq < (60); ++qqq) {
      double r = (a + b) / 2;
      if (check(r, i0))
        a = r;
      else
        b = r;
    }
    ans = a;
  }
  printf("%.15lf", (double)ans);
  return 0;
}
