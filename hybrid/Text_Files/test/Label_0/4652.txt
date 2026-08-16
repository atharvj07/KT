#include <bits/stdc++.h>
using namespace std;
set<int> ms;
set<pair<int, int>> aRes;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int n, k;
  cin >> n >> k;
  int ans = 4 + 3 * (n - 2);
  for (int i = 0; i < k; i++) {
    int item;
    cin >> item;
    int k0 = item - 1;
    int k1 = item + 1;
    aRes.insert({item, item});
    if (ms.find(k0) != ms.end()) aRes.insert({k0, item});
    if (ms.find(k1) != ms.end()) aRes.insert({k1, item});
    ms.insert(item);
  }
  ans -= aRes.size();
  cout << ans << "\n";
  return 0;
}
