#include <bits/stdc++.h>
using namespace ::std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    string a, b;
    vector<int> ans;
    cin >> a >> b;
    for (int i = n - 1; i > 0; i--)
      if (a[i] != b[i]) {
        if (a[i] != a[0]) ans.push_back(1), a[0] = !(a[0] - '0') + '0';
        ans.push_back(i + 1);
        for (int j = 0; j <= i; j++) a[j] = !(a[j] - '0') + '0';
        string tmp = a.substr(0, i + 1);
        reverse(tmp.begin(), tmp.end());
        a = tmp + (i != n - 1 ? a.substr(i + 1) : "");
      }
    if (a[0] != b[0]) ans.push_back(1);
    cout << ans.size() << ' ';
    for (auto c : ans) cout << c << ' ';
    cout << '\n';
  }
}
