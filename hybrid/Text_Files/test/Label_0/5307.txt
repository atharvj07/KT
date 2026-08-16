#include <bits/stdc++.h>
using namespace std;
long long a, b;
int main() {
  cin >> a >> b;
  if (a > b) swap(a, b);
  if (a == 2) {
    int t = 4 * ((b - 1) / 4);
    if (b % 4 == 1)
      t += 2;
    else
      t += 4;
    cout << t;
    return 0;
  }
  if (a == 1) {
    cout << b;
    return 0;
  }
  int t = a * b / 2;
  if (a % 2 != 0 && b % 2 != 0) t++;
  cout << t;
  return 0;
}
