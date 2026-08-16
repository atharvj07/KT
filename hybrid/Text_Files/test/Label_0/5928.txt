#include <bits/stdc++.h>
using namespace std;
int main() {
  string route;
  cin >> route;
  if (route.size() % 2 != 0) {
    cout << -1 << endl;
    return 0;
  }
  int L = 0;
  int R = 0;
  int U = 0;
  int D = 0;
  for (int i = 0; i < route.size(); i++) {
    if (route[i] == 'L') {
      L++;
    } else if (route[i] == 'R') {
      R++;
    } else if (route[i] == 'U') {
      U++;
    } else if (route[i] == 'D') {
      D++;
    }
  }
  int hor, vert;
  hor = abs(L - R);
  vert = abs(U - D);
  if ((hor % 2 != 0 && vert % 2 != 0) || (hor % 2 == 0 && vert % 2 == 0)) {
    cout << (hor + vert) / 2 << endl;
  } else {
    cout << -1 << endl;
  }
}
