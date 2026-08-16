#include <bits/stdc++.h>
using namespace std;
int main() {
  set<int> done;
  vector<pair<int, int> > grads1, grads2;
  vector<long long> sols;
  int n, q;
  scanf("%d%d", &n, &q);
  vector<int> vals;
  vals.resize(n);
  for (int c = 0; c < n; c++) scanf("%d", &vals[c]);
  for (int c = 0; c < n - 1; c++)
    grads1.push_back(pair<int, int>(abs(vals[c + 1] - vals[c]), c));
  grads2 = grads1;
  sort(grads2.begin(), grads2.end());
  sols.resize(n - 1);
  vector<int> left(n - 1), right(n - 1);
  for (int c = n - 2; c >= 0; c--) {
    auto l = done.upper_bound(grads2[c].second);
    auto u = done.lower_bound(grads2[c].second + 1);
    if (l == done.begin())
      left[grads2[c].second] = 0;
    else
      left[grads2[c].second] = *(--l);
    if (u == done.end())
      right[grads2[c].second] = n - 1;
    else
      right[grads2[c].second] = *u;
    done.insert(grads2[c].second);
    done.insert(grads2[c].second + 1);
  }
  int i, j;
  while (q--) {
    scanf("%d%d", &i, &j);
    long long r = 0;
    i--;
    j--;
    for (int c = i; c < j; c++) {
      r += (long long)grads1[c].first * (min(right[c], j) - c) *
           (c + 1 - max(left[c], i));
    }
    cout << r << endl;
  }
  return 0;
}
