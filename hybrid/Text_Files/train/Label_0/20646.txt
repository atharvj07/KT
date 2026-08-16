#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n, i, x;
  long long sum;
  cin >> n;
  sum = -n * (n - 1) / 2;
  for (i = 1; i <= n; i++) {
    cin >> x;
    sum += 1LL * x * i;
  }
  cout << sum;
  return 0;
}
