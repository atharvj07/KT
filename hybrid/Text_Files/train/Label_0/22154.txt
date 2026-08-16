#include <bits/stdc++.h>
using namespace std;
bool sorty(const pair<string, long long int> &a,
           const pair<string, long long int> &b) {
  return a.second > b.second;
}
void initialize(bool flag[], long long int x) {
  for (long long int i = 0; i < x; i++) flag[i] = false;
}
long long int t, n, m;
long long int x, y;
long long int i, k;
string s1;
int main() {
  cin >> n >> m;
  set<long long int> s, ans;
  for (long long int i = 0; i < n; i++) {
    cin >> x, s.insert(x);
  }
  for (long long int j = 1; j <= m; j++) {
    if (!s.count(j)) {
      m -= j;
      ans.insert(j);
    }
  }
  cout << ans.size() << endl;
  for (auto p : ans) cout << p << " ";
  cout << endl;
  return 0;
}
