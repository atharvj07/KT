#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int arr[n];
  for (int i = 0; i < n; i++) cin >> arr[i];
  int i = 0, j = 2, maxi = 1;
  int sum = arr[0] + arr[1];
  while (j < n) {
    if (sum == arr[j]) {
      maxi = max(maxi, j - i + 1);
      j++;
    } else {
      i = j - 1;
      j++;
    }
    sum = arr[j - 2] + arr[j - 1];
  }
  if (maxi >= 2)
    cout << maxi;
  else {
    if (arr[1] == arr[0])
      cout << "2";
    else if (n == 1)
      cout << "1";
    else if (n == 2)
      cout << "2";
  }
  return 0;
}
