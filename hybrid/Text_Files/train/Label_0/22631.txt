#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  if (n < 20) {
    if (n == 2 || n == 3 || n == 4 || n == 5 || n == 6 || n == 8 || n == 12) {
      cout << "YES";
      return 0;
    }
    cout << "NO";
    return 0;
  }
  if (n / 10 == 2 || n / 10 == 7 || n / 10 == 9 || n % 10 == 1 || n % 10 == 7 ||
      n % 10 == 9) {
    cout << "NO";
    return 0;
  }
  cout << "YES";
  return 0;
}
