#include <bits/stdc++.h>
using namespace std;
int k;
int mp[30];
string s;
int main() {
  cin >> k >> s;
  if (s.size() % k != 0) puts("-1"), exit(0);
  for (int i = 0; i < s.size(); i++) mp[s[i] - 'a']++;
  for (int i = 0; i < s.size(); i++) {
    if (mp[s[i] - 'a'] % k == 0) continue;
    puts("-1");
    exit(0);
  }
  string ans = "";
  for (int i = 0; i < 26; i++) {
    int n = mp[i] / k;
    for (int j = 0; j < n; j++) {
      ans += 'a' + i;
    }
  }
  for (int i = 0; i < k; i++) cout << ans;
  cout << endl;
}
