#include <bits/stdc++.h>
using namespace std;
const int INFTY = 20000000;
const int MAX = 500100;
const int MOD = 10000000;
void coutTab(int* tab, int n) {
  for (int i = 0; i < n; i++) {
    cout << tab[i] << " ";
  }
  cout << "\n";
}
int findC(int a, int b, int c) {
  int i2 = 0, i5 = 0;
  int cb = b;
  while (b % 2 == 0) {
    i2++;
    b /= 2;
  }
  while (b % 5 == 0) {
    i5++;
    b /= 5;
  }
  b = cb;
  for (int i = 0; i < max(i2, i5); i++) {
    a *= 10;
    if (a / b == c) return i + 1;
    a = a % b;
  }
  a *= 10;
  int f = a / b;
  for (int i = 1; i < 10000; i++) {
    if (a / b == c) return max(i2, i5) + i;
    a = a % b;
    a *= 10;
  }
  return -1;
}
int main() {
  ios_base::sync_with_stdio(0);
  int a, b, c;
  cin >> a >> b >> c;
  cout << findC(a, b, c) << "\n";
}
