#include <bits/stdc++.h>
using namespace std;
long long ans[1000000];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  long long n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    ans[i] = 1;
  }
  for (int i = 2; i <= n; i++) {
    for (int j = 2 * i; j <= n; j = j + i) {
      ans[j] = i;
    }
  }
  sort(ans + 1, ans + 1 + n);
  for (int i = 2; i <= n; i++) {
    cout << ans[i] << " ";
  }
  return 0;
}
