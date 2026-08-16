#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n, k;
  cin >> n >> k;
  long long arr[n];
  long long mini = LONG_MAX;
  int flag = 0;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + n);
  long long ans = 0;
  for (int i = 1; i < n; i++) {
    long long val = arr[i] - arr[0];
    if (val % k != 0) {
      cout << -1;
      return 0;
    }
    ans += val / k;
  }
  cout << ans;
}
