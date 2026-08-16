#include <bits/stdc++.h>
using namespace std;
int n, x, mx = 0, mp[200010];
int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    scanf("%d", &x);
    mp[x] = i + 1;
  }
  for (int i = 0; i < n; i++) {
    scanf("%d", &x);
    cout << max(0, mp[x] - mx) << ' ';
    mx = max(mx, mp[x]);
  }
  return 0;
}
