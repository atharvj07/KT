#include <bits/stdc++.h>
using namespace std;
int main() {
  vector<int> a(6);
  int sol = 1e9;
  for (int i = 0; i < 6; i++) {
    cin >> a[i];
  }
  int n;
  cin >> n;
  vector<pair<int, int>> c(6 * n);
  for (int i = 0; i < n; i++) {
    int b;
    cin >> b;
    for (int j = 0; j < 6; j++) c[6 * i + j] = {b - a[j], i};
  }
  vector<int> d(n, -1e9);
  multiset<int> ms;
  for (int i : d) ms.insert(i);
  sort(c.begin(), c.end());
  for (int i = 0; i < 6 * n; i++) {
    ms.erase(ms.find(d[c[i].second]));
    d[c[i].second] = c[i].first;
    ms.insert(c[i].first);
    sol = min(sol, c[i].first - (*ms.begin()));
  }
  cout << sol << endl;
  return 0;
}
