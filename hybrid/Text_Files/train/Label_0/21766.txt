#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  vector<int> arr(2 * n - 1);
  for (int i = 0; i < 2 * n - 1; ++i) cin >> arr[i];
  if (n % 2 == 1) {
    int sum = 0;
    for (int i = 0; i < 2 * n - 1; ++i) sum += abs(arr[i]);
    cout << sum << endl;
  } else {
    int min = 1001;
    int idx = -1;
    int count = 0;
    for (int i = 0; i < 2 * n - 1; ++i) {
      if (arr[i] < 0) ++count;
      if (abs(arr[i]) < min) {
        min = abs(arr[i]);
        idx = i;
      }
    }
    int sum = 0;
    for (int i = 0; i < 2 * n - 1; ++i) sum += abs(arr[i]);
    if (count == 0 || (count % 2 == 0 && count != 0))
      cout << sum;
    else
      cout << sum - 2 * abs(arr[idx]);
  }
  return 0;
}
