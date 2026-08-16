#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  int count = 0;
  map<string, string> mp;
  vector<vector<string>> v;
  for (int i = 0; i < (n + m); i++) {
    string str1, str2;
    vector<string> vin;
    cin >> str1;
    cin >> str2;
    if (i < n) mp[str2 + ';'] = str1;
    vin.push_back(str1);
    vin.push_back(str2);
    v.push_back(vin);
  }
  for (int i = n; i < (n + m); i++) {
    string ans = "";
    ans += v[i][0] + " " + v[i][1] + " " + '#' + mp[v[i][1]];
    cout << ans << endl;
  }
}
