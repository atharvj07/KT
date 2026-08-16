#include <bits/stdc++.h>
using namespace std;
const long long inf = LLONG_MAX;
int n, q, sq, len, ord, ii, jj, val, mx, mn, mxpos, mnpos;
long long lazy[1000];
vector<pair<long long, long long> > S[1000];
inline int getseg(int pos) { return pos / sq + (pos % sq != 0); }
void prop(int as) {
  for (int i = 0; i < S[as].size(); i++) {
    S[as][i].first += lazy[as];
    if (S[as][i].second >= ii && S[as][i].second <= jj) S[as][i].first += val;
  }
  lazy[as] = 0;
  sort(S[as].begin(), S[as].end());
}
void update(int sts, int eds) {
  for (int i = sts; i <= eds; i++) lazy[i] += val;
}
int query() {
  long long FR = -inf, FL = inf;
  for (int i = 1; i <= len; i++) {
    int posL = 0, posR = 0;
    posL =
        lower_bound(S[i].begin(), S[i].end(), make_pair(val - lazy[i], -inf)) -
        S[i].begin();
    posR =
        upper_bound(S[i].begin(), S[i].end(), make_pair(val - lazy[i], inf)) -
        S[i].begin();
    if (S[i][posL].first == val - lazy[i]) FL = min(FL, S[i][posL].second);
    if (posR && S[i][posR - 1].first == val - lazy[i])
      FR = max(FR, S[i][posR - 1].second);
  }
  if (FL == inf || FR == -inf) return -1;
  return FR - FL;
}
int main() {
  scanf("%d %d", &n, &q);
  sq = sqrt(n);
  len = n / sq + (n % sq != 0);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &val);
    S[getseg(i)].push_back(make_pair(val, i));
  }
  for (int i = 1; i <= len; i++) sort(S[i].begin(), S[i].end());
  while (q--) {
    scanf("%d", &ord);
    if (ord == 1) {
      scanf("%d %d %d", &ii, &jj, &val);
      int second = getseg(ii);
      int es = getseg(jj);
      prop(second);
      if (second != es) prop(es);
      update(second + 1, es - 1);
    } else {
      scanf("%d", &val);
      printf("%d\n", query());
    }
  }
}
