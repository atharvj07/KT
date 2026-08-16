#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e9 + 7;
const double eps = 1e-9;
const double PI = acos(-1);
const int maxn = 2e5 + 5;
int a[maxn];
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    int f = 1;
    for (int i = n, cur = 1; i >= 1;) {
      int j = a[i], l = i;
      for (; j >= cur; j--, l--) {
        if (l < 1 || a[l] != j) {
          f = 0;
          i = 0;
          break;
        }
      }
      cur = a[i] + 1;
      i = l;
    }
    if (f)
      cout << "Yes\n";
    else
      cout << "No\n";
  }
  return 0;
}
