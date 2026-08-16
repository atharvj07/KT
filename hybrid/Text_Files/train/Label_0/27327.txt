#include <bits/stdc++.h>
using namespace std;
int n;
string s;
int main() {
  ios::sync_with_stdio(0);
  cin >> n >> s;
  int ans = 0;
  int now = 0;
  map<char, int> mp;
  for (int i = 0; i < s.length(); i++) {
    if ('A' <= s[i] && s[i] <= 'Z') {
      mp.clear();
      now = 0;
    } else if (!mp.count(s[i])) {
      now++;
      mp[s[i]] = 1;
    }
    ans = max(ans, now);
  }
  cout << ans << endl;
  return 0;
}
