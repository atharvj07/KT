#include <bits/stdc++.h>
using namespace std;
int main() {
  int a, b, c, d, e, f, n, arr1[1000], arr[1000];
  cin >> n;
  for (int i = 0; i < n; i++) cin >> arr1[i];
  for (int j = 0; j < n; j++) {
    int sum = 0;
    for (int i = 0; i < arr1[j]; i++) {
      cin >> b;
      sum = sum + (5 * b);
    }
    sum += 15 * arr1[j];
    arr[j] = sum;
  }
  cout << *min_element(arr, arr + n) << endl;
  return 0;
}
