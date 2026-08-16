#include <bits/stdc++.h>
#pragma GCC optimize(2)
using namespace std;
void qread(int &x) {
  int neg = 1;
  x = 0;
  char c = getchar();
  while (c < '0' || c > '9') {
    if (c == '-') neg = -1;
    c = getchar();
  }
  while (c >= '0' && c <= '9') x = 10 * x + c - '0', c = getchar();
  x *= neg;
}
const int maxn = 200005;
const int maxm = 55;
int n, k;
double t[maxn], sum[maxn], isum[maxn];
double dp[maxm][maxn];
class Line {
 public:
  double k, b;
  Line(double _k = 0, double _b = 0) : k(_k), b(_b) {}
};
double inter(Line a, Line b) { return (b.b - a.b) / (a.k - b.k); }
namespace Convex {
int top;
Line st[maxn];
void init() { top = 0; }
void add(Line x) {
  while (top >= 2 && inter(st[top - 2], x) > inter(st[top - 1], x)) top--;
  st[top++] = x;
}
double qry(int &pos, double x) {
  if (!top) return -1e18;
  if (pos >= top) pos = top - 1;
  while (pos + 1 < top && x >= inter(st[pos + 1], st[pos])) pos++;
  return st[pos].k * x + st[pos].b;
}
}  // namespace Convex
int main() {
  scanf("%d%d", &n, &k);
  double ans = 0;
  for (int(i) = 1; (i) <= n; i++) {
    scanf("%lf", &t[i]);
    sum[i] = sum[i - 1] + t[i];
    isum[i] = isum[i - 1] + (1.0 / t[i]);
    ans += sum[i] / t[i];
  }
  for (int(i) = 0; (i) < k + 1; i++)
    for (int(j) = 0; (j) < n + 1; j++) dp[i][j] = -1e18;
  dp[0][0] = 0;
  for (int(i) = 1; (i) <= k; i++) {
    Convex::init();
    int pos = 0;
    for (int(j) = 1; (j) <= n; j++) {
      if (dp[i - 1][j - 1] != -1e18)
        Convex::add(
            Line(sum[j - 1], dp[i - 1][j - 1] - sum[j - 1] * isum[j - 1]));
      dp[i][j] = Convex::qry(pos, isum[j]);
    }
  }
  printf("%.10lf\n", ans - dp[k][n]);
  return 0;
}
