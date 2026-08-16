#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n, x;
  cin >> n;
  long long k1, k2;
  vector<long long> v1, v2, v3, v4;
  cin >> k1;
  for (int i = 0; i < k1; i++) {
    cin >> x;
    v1.push_back(x);
    v3.push_back(x);
  }
  cin >> k2;
  for (int i = 0; i < k2; i++) {
    cin >> x;
    v2.push_back(x);
    v4.push_back(x);
  }
  long long ans = 0, f = -1;
  while (1) {
    if (v1.size() == 0) {
      f = 2;
      break;
    } else if (v2.size() == 0) {
      f = 1;
      break;
    } else {
      bool mf = 1, mf1 = 1;
      for (int i = 0; i < v1.size(); i++) {
        if (v1[i] != v3[i]) {
          mf = 0;
          break;
        }
      }
      for (int i = 0; i < v2.size(); i++) {
        if (v2[i] != v4[i]) {
          mf1 = 0;
          break;
        }
      }
      if (ans > 1 && mf == 1 && mf1 == 1 && (v1.size() == v3.size()) &&
          (v2.size() == v4.size())) {
        f = -1;
        break;
      } else if (ans > 10000000)
        break;
      if (v1[0] > v2[0]) {
        v1.push_back(v2[0]);
        v1.push_back(v1[0]);
        v1.erase(v1.begin());
        v2.erase(v2.begin());
        ans++;
      } else {
        v2.push_back(v1[0]);
        v2.push_back(v2[0]);
        v1.erase(v1.begin());
        v2.erase(v2.begin());
        ans++;
      }
    }
  }
  if (f == -1)
    cout << -1 << endl;
  else
    cout << ans << " " << f << endl;
}
