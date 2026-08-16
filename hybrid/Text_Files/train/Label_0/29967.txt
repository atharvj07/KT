#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  int n, a, b;
  cin >> n >> a >> b;
  int level = 0;
  while (a != b) {
    a = (a + 1) / 2;
    b = (b + 1) / 2;
    level++;
  }
  if ((1 << level) == n)
    cout << "Final!" << endl;
  else
    cout << level << endl;
  return 0;
}
