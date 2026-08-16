#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ;
  int n;
  cin >> n;
  vector<int> arr(n);
  int oddcnt = 0, evencnt = 0;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    if (a % 2)
      oddcnt++;
    else
      evencnt++;
  }
  if (oddcnt == 0)
    cout << 0 << "\n";
  else {
    if (oddcnt <= evencnt) {
      cout << oddcnt << "\n";
    } else {
      int ans = evencnt;
      oddcnt -= evencnt;
      ans += (oddcnt / 3);
      cout << ans << "\n";
    }
  }
  return 0;
}
