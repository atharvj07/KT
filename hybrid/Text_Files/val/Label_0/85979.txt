#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
map<int, int> m;
int a[N];
int main() {
  int n, ans = 0x3f3f3f3f, num = 0x3f3f3f3f;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    num = min(a[i], num);
  }
  for (int i = 1; i <= n; i++) {
    if (m[a[i]] != 0 && a[i] == num) ans = min(ans, i - m[a[i]]);
    m[a[i]] = i;
  }
  cout << ans << endl;
  return 0;
}
