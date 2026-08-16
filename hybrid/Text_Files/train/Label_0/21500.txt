#include <bits/stdc++.h>
using namespace std;
int n;
int pie(int x, int y) {
  while (x != y) {
    if (x > y) {
      x = x - y;
    }
    if (x < y) {
      y = y - x;
    }
  }
  if (x == 1) {
    return 1;
  } else {
    return 0;
  }
}
int main() {
  cin >> n;
  for (int i = n / 2; i >= 1; --i) {
    if (pie(i, n - i) == 1) {
      cout << i << " " << n - i;
      return 0;
    }
  }
  return 0;
}
