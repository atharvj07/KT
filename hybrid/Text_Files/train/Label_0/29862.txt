#include <bits/stdc++.h>
using namespace std;
int main() {
  int a[5];
  for (int i = 0; i < 4; i++) {
    cin >> a[i];
  }
  sort(a, a + 4);
  ((a[0] + a[3] == a[1] + a[2]) || (a[0] + a[1] == a[2] + a[3]) ||
   (a[0] + a[2] == a[1] + a[3]) || (a[0] + a[1] + a[2] == a[3]))
      ? cout << "YES\n"
      : cout << "NO\n";
  return 0;
}
