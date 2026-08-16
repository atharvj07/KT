#include <bits/stdc++.h>
using namespace std;
void preprocess(void) { return; }
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.precision(20);
  preprocess();
  int n;
  cin >> n;
  long long k;
  cin >> k;
  vector<int> a(n);
  for (auto i = (0); i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  int cnt = 0;
  ;
  for (auto i = (0); i < n; i++) {
    ;
    if (k * 2 >= a[i]) {
      k = max(k, (long long)a[i]);
    } else {
      ;
      for (auto j = (1); j < 34; j++) {
        if (k * 2 < a[i]) {
          k = k * 2;
          cnt++;
        } else {
          break;
        }
      }
      k = max(k, (long long)a[i]);
    }
  }
  cout << cnt << endl;
}
