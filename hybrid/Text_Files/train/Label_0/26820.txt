#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 100;
int arr[maxn];
multiset<int> s;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    s.insert(x);
  }
  int ans = 1;
  while (s.size() > 1) {
    auto it = s.begin();
    it++;
    if (*s.begin() != *it)
      ans++;
    else {
      int h = *it;
      h++;
      s.erase(it);
      s.insert(h);
    }
    s.erase(s.begin());
  }
  cout << ans << "\n";
}
