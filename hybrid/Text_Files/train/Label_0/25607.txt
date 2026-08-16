#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e5 + 9;
int a[MAX], n, ans;
vector<int> l;
int main() {
  cin >> n;
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n; i++) {
    while (l.size() && a[i] >= l.back()) l.pop_back();
    if (l.size()) ans = max(ans, l.back() ^ a[i]);
    l.push_back(a[i]);
  }
  for (int i = n - 1; i >= 0; i--) {
    while (l.size() && a[i] >= l.back()) l.pop_back();
    if (l.size()) ans = max(ans, l.back() ^ a[i]);
    l.push_back(a[i]);
  }
  cout << ans;
}
