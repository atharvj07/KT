#include <bits/stdc++.h>
using namespace std;
long long n, x, ans;
map<int, int> a, b;
int main() {
  cin >> n;
  ans = 1;
  for (int i = 1; i <= n; i++) {
    cin >> x;
    a[x]++;
    b[a[x]]++;
    if (a[x] * b[a[x]] == i && i != n) {
      ans = i + 1;
    }
    if (a[x] * b[a[x]] == i - 1) {
      ans = i;
    }
  }
  cout << ans << endl;
  return 0;
}
