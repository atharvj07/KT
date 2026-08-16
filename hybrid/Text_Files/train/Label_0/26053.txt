#include <bits/stdc++.h>
using namespace std;
int a[10000], b[10000];
int main() {
  for (int i = 1; i <= 3; i++) {
    cin >> a[i];
  }
  for (int i = 1; i <= 3; i++) {
    cin >> b[i];
  }
  for (int i = 1; i <= 3; i++) {
    if (a[i] == b[i]) {
      cout << "YES";
      return 0;
    }
  }
  cout << "NO";
}
