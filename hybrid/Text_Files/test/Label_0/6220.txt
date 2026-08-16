#include <bits/stdc++.h>
using namespace std;
int n, ans = 1e9 + 5;
int main(void) {
  cin >> n;
  for (int i = 1; i * i <= n; i++) {
    int j = (n % i == 0 ? n / i : n / i + 1);
    ans = ((ans) < (i + j) ? (ans) : (i + j));
  }
  cout << ans << endl;
  return 0;
}
