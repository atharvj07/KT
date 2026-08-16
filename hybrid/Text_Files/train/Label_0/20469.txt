#include <bits/stdc++.h>
using namespace std;
void io() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
}
map<long long, long long> MP;
int main() {
  io();
  int n;
  cin >> n;
  vector<int> ans(n + 1, 1);
  for (int i = 2; i <= n; ++i) {
    for (int j = i + i; j <= n; j += i) {
      ans[j] = i;
    }
  }
  sort(ans.begin(), ans.end());
  for (int i = 2; i <= n; ++i) cout << ans[i] << ' ';
}
