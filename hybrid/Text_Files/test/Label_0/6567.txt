#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  n ^= 8;
  if (n / 8 == 1) n ^= 4;
  if (n / 4 == 3) n ^= 2;
  if (n / 2 == 7) n ^= 1;
  cout << n << endl;
  return 0;
}
