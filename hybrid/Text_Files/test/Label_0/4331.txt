#include <bits/stdc++.h>
using namespace std;
int main() {
  int X;
  cin >> X;
  if (X >= 5 && X % 5 == 0)
    cout << X / 5;
  else if (X < 5)
    cout << "1";
  else
    cout << 1 + (X / 5);
}
