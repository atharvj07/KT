#include <bits/stdc++.h>
using namespace std;
class sqrt_decomp {
 private:
 public:
};
void A() {
  long long n, m;
  cin >> n >> m;
  long long len = n + m;
  vector<long long> a(len);
  for (int(i) = (0); (i) < (len); ++(i)) cin >> a[i];
  vector<long long> t(len);
  for (int(i) = (0); (i) < (len); ++(i)) cin >> t[i];
  vector<long long> ans(len, -1), dist(len, (long long)1e18);
  long long last = -1;
  for (int(i) = (0); (i) < ((int)(a).size()); ++(i)) {
    if (t[i] == 1) last = i;
    if (last > -1 && abs(a[i] - a[last]) < dist[i]) {
      dist[i] = abs(a[i] - a[last]);
      ans[i] = last;
    }
  }
  last = -1;
  for (int i = (int)(a).size() - 1; i >= 0; --i) {
    if (t[i] == 1) last = i;
    if (last > -1 && abs(a[i] - a[last]) < dist[i]) {
      dist[i] = abs(a[i] - a[last]);
      ans[i] = last;
    }
  }
  map<long long, long long> res;
  for (int(i) = (0); (i) < ((int)(a).size()); ++(i)) {
    if (t[i] == 0) {
      res[ans[i]]++;
    }
  }
  for (int(i) = (0); (i) < ((int)(a).size()); ++(i)) {
    if (t[i] == 1) {
      cout << res[i] << " ";
    }
  }
}
int main() {
  A();
  return 0;
}
