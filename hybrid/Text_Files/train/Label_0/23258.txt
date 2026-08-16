#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const int maxn = 1000000;
long long b[maxn];
long long ans[maxn];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n / 2; i++) cin >> b[i];
  long long l, r;
  l = 0, r = b[0];
  ans[0] = l;
  ans[n - 1] = r;
  for (int i = 1; i < n / 2; i++) {
    if (b[i] >= r) {
      long long rk = r;
      long long lk = b[i] - r;
      if (lk >= l) {
        ans[i] = b[i] - rk;
        ans[n - i - 1] = rk;
        l = b[i] - rk;
        r = rk;
      } else if (lk < l) {
        ans[i] = l;
        ans[n - i - 1] = b[i] - l;
        l = l;
        r = b[i] - l;
      }
    } else {
      long long rk = b[i];
      long long lk = b[i] - r;
      if (lk >= l) {
        ans[i] = b[i] - rk;
        ans[n - i - 1] = rk;
        l = b[i] - rk;
        r = rk;
      } else if (lk < l) {
        ans[i] = l;
        ans[n - i - 1] = b[i] - l;
        l = l;
        r = b[i] - l;
      }
    }
  }
  for (int i = 0; i < n; i++) {
    cout << ans[i] << " ";
  }
  cout << endl;
  return 0;
}
