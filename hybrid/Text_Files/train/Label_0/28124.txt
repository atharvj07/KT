#include <bits/stdc++.h>
using namespace std;
const int maxn = 200000 + 10;
int sun[maxn];
int main() {
  int n = 0, b = 0, a = 0;
  cin >> n >> b >> a;
  int bb = b, aa = a;
  for (int i = 0; i < n; i++) cin >> sun[i];
  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (sun[i]) {
      if (a == aa) {
        ans++;
        a--;
      } else if (b) {
        ans++;
        b--;
        a++;
      } else {
        if (a) {
          ans++;
          a--;
        } else {
          break;
        }
      }
    } else {
      if (a) {
        ans++;
        a--;
      } else {
        if (b) {
          ans++;
          b--;
        } else
          break;
      }
    }
  }
  cout << ans;
  getchar();
  getchar();
  return 0;
}
