#include <bits/stdc++.h>
using namespace std;
int main() {
  int w, y, i, a, b, mx = 1, x = 0;
  cin >> y >> w;
  x = max(y, w);
  const string probability[7] = {"", "1/1", "5/6", "2/3", "1/2", "1/3", "1/6"};
  cout << probability[x] << endl;
}
