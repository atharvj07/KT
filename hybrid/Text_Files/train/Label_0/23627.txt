#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, b, c;
  int a;
  cin >> n >> a >> b >> c;
  int ans = 0;
  for (int i = 0; i <= b; i++) {
    for (int j = 0; j <= c; j++) {
      int p = n - (j * 2 + i);
      if (p >= 0 && p <= a / 2) ans++;
    }
  }
  cout << ans;
  return 0;
}
