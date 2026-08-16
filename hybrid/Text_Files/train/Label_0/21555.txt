#include <bits/stdc++.h>
using namespace std;
int main() {
  string s;
  cin >> s;
  int n = s.size();
  vector<int> ab, ba;
  for (int i = 0; i < n - 1; ++i) {
    if (s[i] == 'A' && s[i + 1] == 'B') ab.push_back(i);
    if (s[i] == 'B' && s[i + 1] == 'A') ba.push_back(i);
  }
  if (ab.empty() || ba.empty())
    cout << "NO\n";
  else {
    if ((ba[(int)(ba.size()) - 1] - ab[0] > 1) ||
        (ab[(int)(ab.size()) - 1] - ba[0] > 1))
      cout << "YES\n";
    else
      cout << "NO\n";
  }
  return 0;
}
