#include <bits/stdc++.h>
using namespace std;
int main() {
  int x;
  cin >> x;
  if (x % 2 == 0) {
    cout << -1 << endl;
    return 0;
  }
  for (int i = 0; i < x; i++) {
    cout << i << " ";
  }
  cout << "\n";
  for (int i = 0; i < x; i++) {
    cout << i << " ";
  }
  cout << "\n";
  for (int i = 0; i < x; i++) {
    cout << (i * 2) % x << " ";
  }
  cout << "\n";
}
