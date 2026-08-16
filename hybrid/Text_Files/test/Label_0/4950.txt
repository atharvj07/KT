#include <bits/stdc++.h>
using namespace std;
int a[8] = {0, 0, 1, 1, 1, -1, -1, -1};
int b[8] = {1, -1, 0, 1, -1, 0, 1, -1};
int main() {
  int n, x, y, ans = 0;
  char c[2];
  scanf("%s", &c);
  x = c[0] - '0' - '0';
  y = c[1] - '0';
  for (int i = 0; i < 8; i++) {
    if (x + a[i] <= 8 && x + a[i] > 0 && y + b[i] <= 8 && y + b[i] >= 1) ans++;
  }
  cout << ans << endl;
}
