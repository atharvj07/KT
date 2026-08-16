#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long int tt, i, j, k;
  cin >> tt;
  while (tt--) {
    int n;
    cin >> n;
    int a[n], b[n], flag = 0;
    for (i = 0; i < n; i++) cin >> a[i];
    for (i = 0; i < n; i++) cin >> b[i];
    map<pair<int, int>, int> m;
    for (i = 0; i < n / 2; i++) {
      m[{min(a[i], a[n - 1 - i]), max(a[i], a[n - 1 - i])}]++;
    }
    for (i = 0; i < n / 2; i++) {
      m[{min(b[i], b[n - 1 - i]), max(b[i], b[n - 1 - i])}]--;
    }
    for (auto x : m) {
      if (x.second != 0) flag = 1;
    }
    if (n % 2 && (a[(n - 1) / 2] != b[(n - 1) / 2])) flag = 1;
    if (flag)
      cout << "No\n";
    else
      cout << "Yes\n";
  }
  return 0;
}
