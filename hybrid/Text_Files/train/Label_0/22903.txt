#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int T;
  cin >> T;
  while (T--) {
    queue<int> odd, even;
    string s;
    cin >> s;
    for (auto c : s) {
      int x = (int)(c - '0');
      if (x & 1)
        odd.push(x);
      else
        even.push(x);
    }
    while (!even.empty() || !odd.empty()) {
      if (!even.empty() && !odd.empty()) {
        if (even.front() > odd.front()) {
          cout << odd.front();
          odd.pop();
        } else {
          cout << even.front();
          even.pop();
        }
      } else if (!even.empty()) {
        cout << even.front();
        even.pop();
      } else {
        cout << odd.front();
        odd.pop();
      }
    }
    cout << '\n';
  }
  return 0;
}
