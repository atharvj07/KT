#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  while (n--) {
    int x, y, k;
    int num1 = -1, num2 = -1, num;
    cin >> k >> x >> y;
    for (int i = 0; i < x; i++) {
      cin >> num;
      num1 = max(num1, num);
    }
    for (int i = 0; i < y; i++) {
      cin >> num;
      num2 = max(num2, num);
    }
    if (num1 > num2)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}
