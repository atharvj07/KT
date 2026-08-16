#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int f, x;
  cin >> f;
  x = f + 1;
  if (f == 0) {
    f = 0;
  } else if (x % 2 == 0) {
    f = x / 2;
  } else {
    f++;
  }
  cout << f << endl;
  return 0;
}
