#include <bits/stdc++.h>
using namespace std;
int arr[100005];
int ans[100005];
int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> arr[i];
  }
  for (int i = 1; i <= n; ++i) {
    cin >> ans[arr[i]];
  }
  for (int i = 1; i <= n; ++i) cout << ans[i] << " ";
  return 0;
}
