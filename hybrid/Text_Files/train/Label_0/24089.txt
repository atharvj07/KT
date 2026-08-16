#include <bits/stdc++.h>
using namespace std;
void printRes(int n, int d, int l) {
  if (d > 0) {
    for (int i = 1; i <= n / 2; i++) {
      if (d > l - 1) {
        cout << l << " 1 ";
        d -= l - 1;
      } else if (d == 0)
        cout << l << " " << l << " ";
      else {
        cout << l << " " << l - d << " ";
        d = 0;
      }
    }
  } else {
    for (int i = 1; i <= n / 2; i++) {
      if (d < 1 - l) {
        cout << "1 " << l << " ";
        d += l - 1;
      } else if (d == 0) {
        cout << l << " " << l << " ";
      } else {
        cout << "1 " << 1 - d << " ";
        d = 0;
      }
    }
  }
}
bool canBe(int n, int d, int l) {
  if ((d > (n / 2) * (l - 1)) || (d < (n / 2) * (1 - l)))
    return false;
  else
    return true;
}
int main() {
  int n, d, l;
  cin >> n >> d >> l;
  if (n % 2 == 0) {
    if (!canBe(n, d, l))
      cout << "-1" << endl;
    else {
      printRes(n, d, l);
    }
  } else {
    if ((d < (n / 2) * (1 - l) + 1) || (d > (n / 2) * (l - 1) + l))
      cout << "-1" << endl;
    else {
      if (canBe(n - 1, d - 1, l)) {
        printRes(n - 1, d - 1, l);
        cout << "1" << endl;
      } else {
        printRes(n - 1, d - l, l);
        cout << l << endl;
      }
    }
  }
}
