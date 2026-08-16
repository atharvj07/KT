#include <bits/stdc++.h>
using namespace std;
int main() {
  string s;
  cin >> s;
  vector<int> a, b;
  int i = 0, j = s.size() - 1;
  while (i < j) {
    while (i < s.size() && s[i] == ')') i++;
    while (j >= 0 && s[j] == '(') j--;
    if (i < s.size() && j >= 0 && i < j) {
      a.push_back(i + 1);
      b.push_back(j + 1);
      i++;
      j--;
    }
  }
  if (a.empty()) {
    cout << 0 << "\n";
    return 0;
  }
  cout << 1 << "\n";
  cout << 2 * a.size() << "\n";
  for (auto i : a) cout << i << " ";
  reverse(b.begin(), b.end());
  for (auto i : b) cout << i << " ";
  cout << "\n";
  return 0;
}
