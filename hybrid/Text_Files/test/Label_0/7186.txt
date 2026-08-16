#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <complex>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <queue>
#include <set>
#include <map>
#include <valarray>
#include <bitset>
#include <stack>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef long long ll;
typedef pair<int,int> pii;
const int INF = 1<<29;
const double PI = acos(-1);
const double EPS = 1e-8;

typedef complex<double> P;
struct C {
  P p; double r;
  C(const P &p, double r) : p(p), r(r) { }
  C() {}
};
bool p1(const C &a, const C &b) {
  return a.p.real() != b.p.real() ? a.p.real() < b.p.real() : a.p.imag() < b.p.imag();
}
bool p2(const C &a, const C &b) {
  return a.p.imag() != b.p.imag() ? a.p.imag() < b.p.imag() : a.p.real() < b.p.real();
}


C circle[100000];
double minR;

double solve(int s, int t) {
  if (s+1>=t) return INF;
  double m1 = solve(s, (s+t)/2);
  double m2 = solve((s+t)/2, t);
  double mid = (circle[(s+t)/2-1].p.real() + circle[(s+t)/2].p.real()) / 2;
  double d = min(m1, m2) + 2*minR + 1;
  int start = lower_bound(circle+s, circle+t, C(P(mid-d-1, -INF), 0), p1) - circle;
  int end = upper_bound(circle+s, circle+t, C(P(mid+d, INF), 0), p1) - circle;
  vector<C> v;
  //cout << s << " " <<t << endl;
  for (int i=start; i<end; ++i) {
    v.push_back(circle[i]);
    //cout << circle[i].p << endl;
  }
  sort(ALL(v), p2);
  double res = min(m1, m2);
  for (int i=0; i<v.size(); ++i) {
    for (int k=i+1; k<v.size() && (v[k].p.imag()-v[i].p.imag())<d; ++k) {
      res = min(res, abs(v[k].p-v[i].p)-v[k].r-v[i].r);
    }
  }
  //cout << res << endl;
  return res;
}

int main() {
  int n;
  while(cin>>n,n) {
    minR = INF;
    REP(i,n) {
      double x, y, r;
      cin >> r >> x >> y;
      circle[i] = C(P(x,y),r);
      minR = min(minR, r);
    }
    sort(circle, circle+n, p1);
    printf("%.10f\n", solve(0, n));
  }
}