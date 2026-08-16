#include <bits/stdc++.h>
using namespace std;
int main() {
  int q;
  cin >> q;
  while (q--) {
    long long int a, b, c;
    cin >> a >> b >> c;
    long long int ans = INT_MAX;
    for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        for (int k = -1; k <= 1; k++) {
          long long int pa = a + i, pb = b + j, pc = c + k;
          ans = min(ans, abs(pa - pb) + abs(pa - pc) + abs(pb - pc));
        }
      }
    }
    cout << ans << "\n";
  }
  return 0;
}
