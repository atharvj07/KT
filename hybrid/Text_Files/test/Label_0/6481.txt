#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 10;
int str[maxn];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> str[i];
  long long ans = 0;
  for (int i = 0; i < n; i++) {
    if (i == 0) {
      ans += 1ll * str[i] * (n - str[i] + 1);
    } else {
      if (str[i] > str[i - 1])
        ans += 1ll * (str[i] - str[i - 1]) * (n - str[i] + 1);
      else
        ans += 1ll * (str[i - 1] - str[i]) * str[i];
    }
  }
  cout << ans << endl;
  return 0;
}
