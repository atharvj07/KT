#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);
  long long int a[4];
  a[3] = 1000000000;
  cin >> a[0] >> a[1] >> a[2];
  sort(a, a + 3);
  if (a[0] == 1) {
    cout << "YES";
    return 0;
  }
  if (a[0] == 2 && a[1] == 2) {
    cout << "YES";
    return 0;
  }
  if (a[0] == 2 && a[1] == 4 && a[2] == 4) {
    cout << "YES";
    return 0;
  };
  if (a[0] == 3 && a[1] == 3 && a[2] == 3) {
    cout << "YES";
    return 0;
  };
  cout << "NO";
  return 0;
}
