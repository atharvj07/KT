#include <bits/stdc++.h>
using namespace std;
int n, s;
long long ans;
int main() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> s;
    ans += s * i;
  }
  cout << ans;
  return 0;
}
