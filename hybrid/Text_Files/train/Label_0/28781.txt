#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
int a[N];
vector<int> sum;
map<int, int> mp;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  sort(a, a + n, greater<int>());
  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      int x = a[i] + a[j];
      if (mp[x] == 0) {
        sum.push_back(x);
      }
      mp[x]++;
    }
  }
  int ans = 0;
  for (auto i : sum) {
    ans = max(ans, mp[i]);
  }
  cout << ans << '\n';
  return 0;
}
