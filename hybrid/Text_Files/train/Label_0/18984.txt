#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  string s;
  cin >> s;
  int n = s.length();
  vector<pair<char, int> > v;
  string w = "";
  for (int i = 0; i < n;) {
    int j = i;
    w += s[i];
    while (j < n && s[i] == s[j]) {
      j++;
    }
    v.push_back({s[i], j - i});
    i = j;
  }
  string t = w;
  reverse(t.begin(), t.end());
  if (t != w) {
    cout << 0;
    return 0;
  }
  for (int i = 0, j = v.size() - 1; i <= j; i++, j--) {
    if (i == j) {
      if (v[i].second == 1) {
        cout << 0;
        return 0;
      } else {
        cout << v[i].second + 1;
        return 0;
      }
    } else {
      if (v[i].second + v[j].second < 3) {
        cout << 0;
        return 0;
      }
    }
  }
}
