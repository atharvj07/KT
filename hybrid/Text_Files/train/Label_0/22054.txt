#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    string ans[4];
    if ((a + b) % 2) {
      ans[3] = "Tidak";
      ans[2] = "Tidak";
      if (a > 0 || d > 0)
        ans[0] = "Ya";
      else
        ans[0] = "Tidak";
      if (b > 0 || c > 0)
        ans[1] = "Ya";
      else
        ans[1] = "Tidak";
    } else {
      ans[0] = "Tidak";
      ans[1] = "Tidak";
      if (c > 0 || b > 0)
        ans[2] = "Ya";
      else
        ans[2] = "Tidak";
      if (d > 0 || a > 0)
        ans[3] = "Ya";
      else
        ans[3] = "Tidak";
    }
    for (int i = 0; i < 4; i++) cout << ans[i] << " ";
    cout << endl;
  }
}
