#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k, s = 0;
  cin >> n >> k;
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    s = s + y - x + 1;
  }
  if (s % k != 0)
    cout << k - s % k << endl;
  else
    cout << 0 << endl;
  return 0;
}
