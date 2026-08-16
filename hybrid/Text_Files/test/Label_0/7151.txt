#include <bits/stdc++.h>
using namespace std;
int s[105];
int main() {
  int n, x;
  while (cin >> n >> x) {
    for (int i = 0; i < n; i++) {
      cin >> s[i];
    }
    sort(s, s + n);
    int index = lower_bound(s, s + n, x) - s;
    if (s[index] == x) {
      cout << 1 + x - index << endl;
    } else {
      cout << x - index << endl;
    }
  }
  return 0;
}
