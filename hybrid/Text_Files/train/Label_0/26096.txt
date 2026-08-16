#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t = 1;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    int ans = 0;
    while (pow(2, ans + 1) - 1 < n) {
      ans++;
    }
    cout << ans << endl;
    int req = pow(2, ans + 1) - 1 - n;
    int arr[ans];
    for (int i = 0; i < ans; i++) {
      arr[i] = pow(2, i);
    }
    int upperrem = req / 3;
    int temp = upperrem;
    if (arr[ans - 2] >= upperrem) {
      arr[ans - 2] -= upperrem;
      upperrem = 0;
    } else {
      upperrem -= arr[ans - 2];
      temp = arr[ans - 2];
      arr[ans - 2] = 0;
    }
    arr[ans - 1] -= req % 3 + upperrem * 3 + temp;
    for (int i = 0; i < ans; i++) {
      cout << arr[i] << " ";
    }
    cout << endl;
  }
  return 0;
}
