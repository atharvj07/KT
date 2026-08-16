#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  int arr[n];
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + n);
  int i = 0, ans = 0;
  while (m--) {
    ans += arr[i];
    i++;
  }
  cout << ans << endl;
  return 0;
}
