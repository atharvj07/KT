#include <bits/stdc++.h>
using namespace std;
const int N = 75005;
const double eps = 0.5;
bool zero(double x) { return x > -eps && x < eps; }
struct P {
  double x, y;
  P operator+(const P &a) const { return (P){x + a.x, y + a.y}; }
  P operator-(const P &a) const { return (P){x - a.x, y - a.y}; }
  P operator*(const P &a) const {
    return (P){x * a.x - y * a.y, x * a.y + y * a.x};
  }
  P operator/(const double &a) const { return (P){x / a, y / a}; }
  double sqrlen() const { return x * x + y * y; }
  double len() const { return sqrt(x * x + y * y); }
  P operator/(const P &a) const {
    return (P){x * a.x + y * a.y, -x * a.y + y * a.x} / a.len() / a.len();
  }
  bool operator<(const P &a) const {
    if (zero(x - a.x)) {
      if (zero(y - a.y)) return 0;
      return y < a.y;
    }
    return x < a.x;
  }
  bool operator==(const P &a) const { return zero(x - a.x) && zero(y - a.y); }
} a[N], b[N];
pair<double, int> A[N], B[N];
vector<pair<int, int> > v;
map<P, int> mp;
int n, n1, n2;
int fa[N], fb[N];
void check(int xa, int xb, int ya, int yb) {
  P r = (a[xb] - a[xa]) / (b[yb] - b[ya]);
  P c = a[xa] - b[ya] * r;
  int cnt1 = 0, cnt0 = 0;
  for (int i = 1; i <= n2; i++) {
    P p = r * b[i] + c;
    if (mp.find(p) != mp.end())
      cnt1++;
    else
      cnt0++;
    if (cnt0 + 0.85 * n > n2) break;
    if (1.0 * cnt1 / (cnt0 + cnt1) < 0.1 && cnt0 + cnt1 > 25) break;
  }
  if (cnt1 < 0.9 * n) return;
  for (int j = 1; j <= n2; j++) {
    P cur = b[j] * r + c;
    if (mp.find(cur) != mp.end()) {
      int nxt = mp[cur];
      if (v.size() < n && !fa[nxt] && !fb[j]) {
        v.push_back(pair<int, int>(nxt, j));
        fa[nxt] = 1;
        fb[j] = 1;
      }
    }
  }
  int ii = 1, jj = 1;
  for (; v.size() < n;) {
    for (; fa[ii]; ii++)
      ;
    for (; fb[jj]; jj++)
      ;
    v.push_back(pair<int, int>(ii, jj));
    ii++;
    jj++;
  }
  for (int i = 0; i < n; i++) printf("%d %d\n", v[i].first, v[i].second);
  exit(0);
}
void solve(int x, int y) {
  for (int i = 1; i <= n1; i++)
    A[i] = pair<double, int>((a[x] - a[i]).sqrlen(), i);
  for (int i = 1; i <= n2; i++)
    B[i] = pair<double, int>((b[i] - b[y]).sqrlen(), i);
  sort(A + 1, A + n1 + 1);
  sort(B + 1, B + n2 + 1);
  int j = 2;
  for (int i = 2; i < n1; i++) {
    for (; j < n2 && B[j].first + 1 < A[i].first; j++)
      ;
    for (int t = j; B[t].first < A[i].first + 5 && t < n2; t++) {
      check(x, A[i].second, y, B[t].second);
      check(x, A[i].second, B[t].second, y);
    }
  }
}
int rnd() {
  int x = 0;
  for (int i = 1; i <= 9; i++) x = x * 10 + rand() % 10;
  return x;
}
int main() {
  srand(time(NULL));
  scanf("%d", &n);
  scanf("%d", &n1);
  for (int i = 1; i <= n1; i++) {
    double x, y;
    scanf("%lf%lf", &x, &y);
    a[i] = (P){x, y};
    mp[a[i]] = i;
  }
  scanf("%d", &n2);
  for (int i = 1; i <= n2; i++) {
    double x, y;
    scanf("%lf%lf", &x, &y);
    b[i] = (P){x, y};
  }
  for (;;) {
    int x = rnd() % n1 + 1;
    int y = rnd() % n2 + 1;
    solve(x, y);
  }
}
