#include <bits/stdc++.h>
using namespace std;
map<int, int> ma;
int main() {
  int t, n, k, i, j, l, r;
  cin >> n;
  set<int> s;
  for (int i = 1; i <= n; i++) {
    cin >> l >> r;
    ma[l]++;
    ma[r + 1]--;
    s.insert(l);
    s.insert(r + 1);
  }
  set<int>::iterator it = s.begin();
  bool ans = true;
  int val = 0;
  while (it != s.end()) {
    int x = *it;
    val += ma[x];
    if (val > 2) ans = false;
    it++;
  }
  if (ans == false)
    cout << "NO\n";
  else
    cout << "YES\n";
}
