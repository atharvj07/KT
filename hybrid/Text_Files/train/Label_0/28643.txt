#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int q;
  cin >> q;
  while (q--) {
    long long int n, m, k, ans = 0;
    cin >> n >> m >> k;
    if (max(n, m) > k)
      cout << -1 << endl;
    else {
      ans += min(n, m);
      long long int dis = max(n, m) - min(n, m);
      long long int mov = k - min(n, m);
      if (dis & 1)
        ans += mov - 1;
      else if (mov % 2 == 0)
        ans += mov;
      else
        ans += mov - 2;
      cout << ans << endl;
    }
  }
}
