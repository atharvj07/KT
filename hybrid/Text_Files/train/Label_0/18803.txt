#include <bits/stdc++.h>
using namespace std;
int main() {
  int a;
  cin >> a;
  for (int i = a; i > 0; i--) {
    if (a % i == 0) {
      a = i;
      cout << a << " ";
    }
  }
  return 0;
}
