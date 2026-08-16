#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n, k;
    cin >> n >> k;
    if (n == k)
      cout << "yes\n";
    else if (n == 1 && k > 1)
      cout << "no\n";
    else if ((n == 3 || n == 2) && k <= 3)
      cout << "yes\n";
    else if ((n == 3 || n == 2) && k > 3)
      cout << "no\n";
    else {
      cout << "yes\n";
    }
  }
}
