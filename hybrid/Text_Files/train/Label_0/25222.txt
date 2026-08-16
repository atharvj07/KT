#include <bits/stdc++.h>
using namespace std;
bool comp(pair<int, int> p1, pair<int, int> p2) { return p1.first < p2.first; }
int main(int argc, char **argv) {
  int n, ret, a, b;
  vector<pair<int, int> > vp;
  scanf("%d%d", &n, &ret);
  for (int k = (0); k < (int)(n); k++) {
    scanf("%d%d", &a, &b);
    vp.push_back(make_pair(a, b));
  }
  sort(vp.begin(), vp.end());
  int sz = vp.size();
  int cnt = 0;
  int q[3005];
  int diff;
  fill(q, q + 3005, ret);
  for (int k = (0); k < (int)(sz); k++) {
    diff = q[vp[k].first] - vp[k].second;
    if (diff >= 0) {
      q[vp[k].first] -= vp[k].second;
    } else {
      q[vp[k].first] = 0;
      q[vp[k].first + 1] = max(0, q[vp[k].first + 1] + diff);
    }
  }
  for (int k = (1); k < (int)(3002); k++) {
    cnt += (ret - q[k]);
  }
  printf("%d", cnt);
  vp.clear();
  return 0;
}
