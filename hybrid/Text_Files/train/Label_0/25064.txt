#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    int p[n];
    for (int i = 0; i < n; ++i) {
      cin >> p[i];
    }
    int l = n / 2 - 1;
    while (p[l] == p[l + 1] && l >= 0) --l;
    if (l < 4) {
      printf("0 0 0\n");
      continue;
    }
    int g = 1, s = 0, b, i;
    for (i = 1; p[i] == p[i - 1]; ++i) {
      ++g;
    }
    while (s <= g && i <= l) {
      ++s;
      for (++i; p[i] == p[i - 1]; ++i) {
        ++s;
      }
    }
    b = l + 1 - g - s;
    if (g >= s || g >= b || g == 0 || s == 0 || b == 0 || (g + s + b) > n / 2) {
      printf("0 0 0\n");
    } else {
      printf("%d %d %d\n", g, s, b);
    }
  }
  return 0;
}
