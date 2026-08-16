#include <bits/stdc++.h>
using namespace std;
int main() {
  int br, tac = 0;
  cin >> br;
  for (int i = 0; i < br; i++) {
    int p, v, t;
    cin >> p >> v >> t;
    if (p + v + t > 1) {
      tac++;
    }
  }
  cout << tac;
  return 0;
}
