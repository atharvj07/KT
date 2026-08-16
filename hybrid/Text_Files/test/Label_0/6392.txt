#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, counter = 0;
  cin >> n;
  int arr[n];
  for (int i = 0; i < n; i++) cin >> arr[i];
  sort(arr, arr + n);
  for (int i = 0, j = 0; i < n && j < n; j++) {
    if (arr[j] > arr[i]) i++, counter++;
  }
  cout << counter << endl;
}
