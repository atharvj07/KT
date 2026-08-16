#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, k, ans;
  cin >> n >> k;
  if (n % 2 == 0) {
    ans = n / 2;
  } else {
    ans = (n / 2) + 1;
  }
  if (k <= ans) {
    cout << (2 * k - 1) << endl;
  } else {
    cout << (k - ans) * 2;
  }
  return 0;
}
