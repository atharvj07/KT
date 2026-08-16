#include <bits/stdc++.h>
using namespace std;
int main() {
  int a, b, c, i, f = 1, g = 1;
  cin >> a;
  int arr[a];
  cin >> arr[0];
  for (i = 1; i < a; i++) {
    cin >> arr[i];
    if (arr[i] > arr[i - 1]) {
      f++;
      if (f > g) {
        g = f;
      }
    } else
      f = 1;
  }
  cout << g << endl;
  return 0;
}
