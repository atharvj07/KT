#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, a[1000];
  vector<int> ot, b, c;
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> a[i];
  sort(a, a + n);
  for (int i = 0; i < n; ++i)
    if (a[i] < 0)
      b.push_back(a[i]);
    else if (a[i] > 0)
      c.push_back(a[i]);
  sort(b.begin(), b.end());
  sort(c.rbegin(), c.rend());
  int uk = 0;
  while (uk + 1 < b.size()) {
    ot.push_back(b[uk]);
    ot.push_back(b[uk + 1]);
    uk += 2;
  }
  uk = 0;
  while (uk + 1 < c.size()) {
    ot.push_back(c[uk]);
    ot.push_back(c[uk + 1]);
    uk += 2;
  }
  if (uk < c.size()) ot.push_back(c[uk]);
  if (ot.size() == 0) ot.push_back(a[n - 1]);
  for (int i = 0; i < ot.size(); ++i) cout << ot[i] << ' ';
  return 0;
}
