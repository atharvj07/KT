#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  if (n % 2 == 0) {
    cout << "NO" << endl;
  } else {
    cout << "YES" << endl;
    int move = 0;
    int tempans = 1;
    for (int i = 0; i < n; i++) {
      cout << tempans << " ";
      if (move % 2 == 0)
        tempans += 3;
      else
        tempans++;
      move++;
    }
    move = 1;
    tempans = 2;
    for (int i = 0; i < n; i++) {
      cout << tempans << " ";
      if (move % 2 == 0)
        tempans += 3;
      else
        tempans++;
      move++;
    }
  }
  return 0;
}
