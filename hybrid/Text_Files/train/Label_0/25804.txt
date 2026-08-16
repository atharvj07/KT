#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  vector<pair<int, int> > a(n);
  for (auto &[x, y] : a) {
    cin >> x >> y;
    x--;
    y--;
  }
  vector<int> ans(n + 5);
  ans[0] = 0;
  vector<bool> done(n);
  done[0] = true;
  for (int i = 0, ct = 0; ct < n; ct++) {
    int x = a[i].first, y = a[i].second;
    if (done[y]) {
      ans[ct + 1] = x;
      i = x;
    } else if (done[x]) {
      ans[ct + 1] = y;
      i = y;
    } else if (a[x].first == y or a[x].second == y) {
      ans[ct + 1] = x;
      done[x] = true;
      i = x;
    } else {
      ans[ct + 1] = y;
      done[y] = true;
      i = y;
    }
  }
  for (int i = 0; i < n; i++) cout << ans[i] + 1 << " ";
  cout << endl;
}
