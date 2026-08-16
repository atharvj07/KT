#include <bits/stdc++.h>
using namespace std;
string get_changed(const string& s1) {
  string s = s1;
  for (int j = 0; j < s.length(); ++j) {
    if (s[j] <= 'Z' && s[j] >= 'A') {
      s[j] += 32;
    }
    if (s[j] == '0') {
      s[j] = 'o';
    }
    if (s[j] == '1' || s[j] == 'i') {
      s[j] = 'l';
    }
  }
  return s;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  string s1;
  cin >> s1;
  int n;
  cin >> n;
  set<string> checker;
  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;
    s = get_changed(s);
    checker.insert(s);
  }
  s1 = get_changed(s1);
  if (checker.find(s1) != checker.end()) {
    cout << "No";
    return 0;
  }
  cout << "Yes";
}
