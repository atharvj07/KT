#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  while (cin >> n) {
    for (int i = 0; i < n; i++) cout << (char)('a' + i % 4);
    cout << endl;
  }
}
