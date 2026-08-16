#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  ;
  long long int t, i;
  cin >> t;
  int m, n, p, j, e;
  for (i = 0; i < t; i++) {
    cin >> m;
    int arr[m];
    for (j = 0; j < m; j++) cin >> arr[j];
    sort(arr, arr + n);
    int flag = 0;
    for (j = 0; j < m - 1; j++) {
      if (abs(arr[j] - arr[j + 1]) % 2 != 0) {
        flag = 1;
        break;
      }
    }
    if (flag == 1)
      cout << "NO\n";
    else
      cout << "YES\n";
  }
  return 0;
}
