#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int t, n, i, j, p = 0, x = 0, y = 0, x1 = 0, y1 = 0, k = 0, a = 0,
                            b = 0, sum = 0, q = 0, r = 0, s = 0, l = 0, c = 0,
                            odd = 0, even = 0;
  long long int array[5];
  for (i = 0; i < 4; i++) {
    cin >> array[i];
  }
  sort(array, array + 4);
  a = array[0] + array[1] + array[2];
  b = array[3];
  x = array[0] + array[1];
  y = array[2] + array[3];
  x1 = array[0] + array[2];
  y1 = array[1] + array[3];
  odd = array[0] + array[3];
  even = array[1] + array[2];
  if (a == b) {
    cout << "YES" << endl;
  } else if (x == y) {
    cout << "YES" << endl;
  } else if (x1 == y1) {
    cout << "YES" << endl;
  } else if (odd == even) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  p = 0, x = 0, y = 0, a = 0, k = 0, l = 0, s = 0, b = 0, c = 0, sum = 0, r = 0,
  q = 0, odd = 0, even = 0;
}
