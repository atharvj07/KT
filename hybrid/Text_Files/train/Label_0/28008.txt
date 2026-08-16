#include <bits/stdc++.h>
using namespace std;
double PI = acos(-1);
double EPS = 1e-7;
int INF = 1000000000;
int MOD = 1000000007;
int MAXINT = 2147483647;
long long INFLL = 1000000000000000000LL;
long long MAXLL = 9223372036854775807LL;
int mx[8] = {-1, 1, 0, 0, -1, -1, 1, 1};
int my[8] = {0, 0, -1, 1, -1, 1, -1, 1};
long long bit[200005];
long long bit2[200005];
long long val[200005];
int h[200005];
void update2(int x, int v) {
  x++;
  for (int i = x; i <= 200000; i += (i & -i)) {
    bit2[i] += v;
  }
}
long long que2(int x) {
  x++;
  long long res = 0;
  for (int i = x; i >= 1; i -= (i & -i)) {
    res += bit2[i];
  }
  return res;
}
void update(int x, int v) {
  x++;
  for (int i = x; i <= 200000; i += (i & -i)) {
    bit[i] += v;
  }
}
long long que(int x) {
  x++;
  long long res = 0;
  for (int i = x; i >= 1; i -= (i & -i)) {
    res += bit[i];
  }
  return res;
}
vector<long long> num;
vector<pair<int, pair<long long, int> > > query;
int pos(long long z) {
  return lower_bound(num.begin(), num.end(), z) - num.begin();
}
int main() {
  int n, q;
  scanf("%d%d", &n, &q);
  for (int(a) = (1); (a) <= (n); (a)++) {
    scanf("%d", &h[a]);
    num.push_back(h[a]);
  }
  for (int(a) = (1); (a) <= (q); (a)++) {
    int t;
    scanf("%d", &t);
    if (t == 1) {
      int p, x;
      scanf("%d%d", &p, &x);
      num.push_back(x);
      query.push_back(make_pair(t, make_pair(p, x)));
    } else {
      long long v;
      scanf("%I64d", &v);
      query.push_back(make_pair(t, make_pair(v, 0)));
    }
  }
  num.push_back(0);
  sort(num.begin(), num.end());
  num.erase(unique(num.begin(), num.end()), num.end());
  for (int(a) = (1); (a) <= (n); (a)++) {
    update(pos(h[a]), h[a]);
    update2(pos(h[a]), 1);
  }
  for (int(a) = (0); (a) <= (q - 1); (a)++) {
    int t = query[a].first;
    if (t == 1) {
      int p = query[a].second.first, x = query[a].second.second;
      update(pos(h[p]), -h[p]);
      update2(pos(h[p]), -1);
      h[p] = x;
      update(pos(h[p]), h[p]);
      update2(pos(h[p]), 1);
    } else {
      long long v = query[a].second.first;
      double l = 0.0;
      double r = INFLL;
      for (int(it) = (1); (it) <= (100); (it)++) {
        double mid = (l + r) / 2.0;
        long long nearest = (long long)mid;
        long long lol = pos(nearest);
        if (lol == (int)num.size() || num[lol] != nearest) lol--;
        double tot = mid * que2(lol) - que(lol);
        if (tot > v || fabs(tot - v) < EPS) {
          r = mid;
        } else
          l = mid;
      }
      printf("%.5lf\n", l);
    }
  }
}
