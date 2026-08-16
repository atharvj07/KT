#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  for (int j = 1; j <= t; j++) {
    int n;
    cin >> n;
    long long int arr[n], s = 0, x;
    for (int i = 0; i < n; i++) {
      cin >> arr[i];
      if (arr[i] <= 2048) {
        s = s + arr[i];
      }
    }
    if (s >= 2048)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}
