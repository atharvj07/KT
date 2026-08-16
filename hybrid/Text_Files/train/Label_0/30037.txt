#include <bits/stdc++.h>
using namespace std;
long long int w, n, k, a[200001], t[200001], pr[200001];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> w >> k;
  for (long long int i = 1; i <= n; ++i) cin >> t[i], pr[i] = pr[i - 1] + t[i];
  for (long long int i = 1; i <= n; ++i) cin >> a[i];
  set<pair<long long int, long long int> > ms, ms2;
  long long int cur = 0, ps = 1;
  vector<pair<long long int, long long int> > ans;
  for (long long int i = 1; i <= n; ++i) {
    if (!ms.empty() && ms.find(make_pair(a[i - 1], i - 1)) != ms.end()) {
      if (ms.size() < w) {
        cur -= ((a[i - 1] + 1) / 2);
        ms.erase(make_pair(a[i - 1], i - 1));
      } else {
        cur -= ((a[i - 1] + 1) / 2);
        ms.erase(make_pair(a[i - 1], i - 1));
        if (!ms2.empty()) {
          auto it = ms2.end();
          it--;
          pair<long long int, long long int> pt = *it;
          cur += ((pt.first + 1) / 2);
          cur -= pt.first;
          ms.insert(pt);
          ms2.erase(it);
        }
      }
    } else {
      ms2.erase(make_pair(a[i - 1], i - 1));
      cur -= a[i - 1];
    }
    bool fl = 0;
    while (ps <= n) {
      if (ms.empty() || ms.size() < w) {
        if (cur + (a[ps] + 1) / 2 <= k) {
          cur += ((a[ps] + 1) / 2);
          ms.insert(make_pair(a[ps], ps));
          ps++;
        } else
          fl = 1;
      } else {
        auto it = ms.begin();
        if (a[ps] <= (*it).first) {
          if (cur + a[ps] <= k) {
            cur += a[ps];
            ms2.insert(make_pair(a[ps], ps));
            ps++;
          } else
            fl = 1;
        } else {
          pair<long long int, long long int> temp = (*it);
          long long int v = (*it).first;
          if (cur + (a[ps] + 1) / 2 + v - (v + 1) / 2 <= k) {
            cur = cur + (a[ps] + 1) / 2 + v - (v + 1) / 2;
            ms.insert(make_pair(a[ps], ps));
            ms.erase(ms.begin());
            ms2.insert(temp);
            ps++;
          } else
            fl = 1;
        }
      }
      if (fl) break;
    }
    ans.push_back(make_pair(i, ps - 1));
  }
  long long int fans = 0;
  for (pair<long long int, long long int> xp : ans)
    fans = max(fans, pr[xp.second] - pr[xp.first - 1]);
  cout << fans << endl;
}
