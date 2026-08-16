#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  long long counter = 0;
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    if (y - x >= 2) counter++;
  }
  cout << counter;
  return 0;
}
