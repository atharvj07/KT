#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  string s, o = "";
  vector<int> v;
  cin >> s;
  for (int i = 0; i < ((int)s.size()); i++)
    if (s[i] != '+') v.push_back(s[i] - '0');
  sort(v.begin(), v.end());
  for (int i = 0; i < ((int)v.size()); i++) {
    o += v[i] + '0';
    o += '+';
  }
  o[((int)o.size()) - 1] = ' ';
  cout << o << "\n";
  return 0;
}
