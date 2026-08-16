#include <bits/stdc++.h>
using namespace std;
long long t;
int main() {
  cin >> t;
  while (t--) {
    long long n, g = 0, s = 0, b = 0, state = 0;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    if (n < 10) {
      cout << "0 0 0\n";
      continue;
    }
    long long pos;
    for (int i = 0; i < n / 2; i++) {
      if (state == 2) {
        pos = i;
        break;
      } else if (state == 0) {
        g++;
        if (a[i + 1] < a[i]) state++;
      } else {
        s++;
        if (a[i + 1] < a[i] && s > g) state++;
      }
    }
    if (state < 2) {
      cout << "0 0 0\n";
      continue;
    }
    b = (n / 2) - g - s;
    for (int i = n / 2 - 1; i >= pos; i--) {
      if (a[i + 1] != a[i]) break;
      b--;
    }
    if (g >= b || b <= 0) {
      cout << "0 0 0\n";
      continue;
    }
    cout << g << " " << s << " " << b << "\n";
  }
}
