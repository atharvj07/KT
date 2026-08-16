#include <bits/stdc++.h>
using namespace std;
string s, s1;
int main() {
  int n, c = -1, k;
  cin >> n >> s;
  for (int i = 0; i < n; i++) {
    if (s[i] == tolower(s[i])) {
      s1.push_back(s[i]);
    }
    if (s[i] == toupper(s[i])) {
      sort(s1.begin(), s1.end());
      s1.erase(unique(s1.begin(), s1.end()), s1.end());
      k = s1.size();
      c = max(c, k);
      s1 = "";
    }
  }
  sort(s1.begin(), s1.end());
  s1.erase(unique(s1.begin(), s1.end()), s1.end());
  k = s1.size();
  c = max(c, k);
  cout << c;
  return 0;
}
