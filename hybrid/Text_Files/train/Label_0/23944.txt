#include <bits/stdc++.h>
using namespace std;
int main() {
  long long t, n;
  long long arr[1000000];
  cin >> t;
  for (int a = 1; a <= t; a++) {
    cin >> n;
    for (int i = 0; i < n; i++) {
      cin >> arr[i];
    }
    if (arr[0] + arr[1] <= arr[n - 1]) {
      cout << 1 << " " << 2 << " " << n << "\n";
    } else
      cout << -1 << "\n";
  }
}
