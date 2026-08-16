#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  char arr[305][305], letter1, letter2;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> arr[i][j];
    }
  }
  letter1 = arr[0][0];
  letter2 = arr[0][1];
  if (letter1 == letter2) {
    cout << "NO";
    return 0;
  }
  bool valid = true;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (i == j || i + j == n - 1) {
        if (arr[i][j] != letter1) {
          valid = false;
          break;
        }
      } else {
        if (arr[i][j] != letter2) {
          valid = false;
          break;
        }
      }
    }
  }
  if (valid)
    cout << "YES";
  else
    cout << "NO";
  return 0;
}
