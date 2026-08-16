#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int arr[105];
    int lock[105];
    int unlocked[105];
    int n, m = 0;
    cin >> n;
    for (int j = 0; j < n; j++) cin >> arr[j];
    for (int j = 0; j < n; j++) cin >> lock[j];
    for (int j = 0; j < n; j++) {
      if (!lock[j]) {
        unlocked[m] = arr[j];
        m++;
      }
    }
    sort(unlocked, unlocked + m);
    for (int j = 0; j < n; j++) {
      if (!lock[j]) {
        m--;
        cout << unlocked[m] << " ";
      } else
        cout << arr[j] << " ";
    }
    cout << "\n";
  }
  return 0;
}
