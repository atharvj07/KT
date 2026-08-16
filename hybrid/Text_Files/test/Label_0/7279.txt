#include <bits/stdc++.h>
using namespace std;
int n, m, x, y, z, taka;
int ara[30000];
vector<int> cut;
int main() {
  cin >> n >> taka;
  int odd = 0, even = 0;
  for (int i = 1; i <= n; i++) cin >> ara[i];
  for (int i = 1; i <= n; i++) {
    x = ara[i];
    if (x % 2)
      odd++;
    else
      even++;
    if (odd == even && i != n) {
      cut.push_back(abs(ara[i] - ara[i + 1]));
    }
  }
  sort(cut.begin(), cut.end());
  int ans = 0;
  for (int i = 0; i < cut.size(); i++) {
    if (taka - cut[i] < 0) break;
    ans++;
    taka = taka - cut[i];
  }
  cout << ans << endl;
  return 0;
}
