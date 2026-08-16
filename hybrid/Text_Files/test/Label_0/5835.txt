#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n;
  cin >> n;
  if (n == 1 || n == 2) {
    cout << "-1";
    return 0;
  } else if (n % 2 == 1) {
    long long k = (n - 1) / 2;
    cout << 2 * k * k + 2 * k << " " << 2 * k * k + 2 * k + 1;
  } else {
    long long k = n / 2;
    cout << k * k - 1 << " " << k * k + 1;
  }
  return 0;
}
