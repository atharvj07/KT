#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n, x, y;
  cin >> n >> x >> y;
  vector<int> v(n);
  for (int i = 0; i < n; i++) {
    cin >> v[i];
  }
  for (int i = 0; i < n; i++) {
    bool val = true;
    for (int j = max(0, i - x); j < i; j++) {
      if (v[i] > v[j]) {
        val = false;
        break;
      }
    }
    for (int j = i + 1; j < min(n, y + i + 1); j++) {
      if (v[i] > v[j]) {
        val = false;
        break;
      }
    }
    if (val) {
      cout << i + 1;
      return 0;
    }
  }
  return 0;
}
