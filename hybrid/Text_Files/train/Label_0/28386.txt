#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  string s[n + 10000];
  vector<int> v;
  for (int i = 0; i < n; ++i) cin >> s[i];
  for (int i = 0; i < s[0].size(); ++i) {
    int j = 0;
    int ans = 1;
    while (j <= n - 1) {
      if (s[j][i] == s[j + 1][i]) ++ans;
      ++j;
    }
    if (ans == n) v.push_back(i);
  }
  int c = 0;
  int mx = -1;
  if (v.size()) ++c;
  for (int i = 1; i < v.size(); ++i) {
    if (v[i] - v[i - 1] == 1)
      ++c;
    else {
      mx = max(mx, c);
      c = 1;
    }
  }
  if (mx == 1) mx = 0;
  if (mx == -1) mx = v.size();
  cout << mx;
}
