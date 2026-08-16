#include <bits/stdc++.h>
using namespace std;
int main() {
  int t[5], i, j, b[101], sum = 0, temp, t1, t2, ans;
  for (i = 0; i < 101; i++) b[i] = 0;
  for (i = 0; i < 5; i++) {
    cin >> t[i];
    sum += t[i];
    b[t[i]]++;
  }
  ans = sum;
  for (i = 1; i < 101; i++) {
    if (b[i] >= 2) {
      if (b[i] == 2) {
        ans = min(ans, sum - i * 2);
      } else {
        ans = min(ans, sum - i * 3);
      }
    }
  }
  cout << ans << "\n";
  return 0;
}
