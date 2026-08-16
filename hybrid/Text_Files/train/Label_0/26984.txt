#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  int s = 0;
  int a[100000];
  memset(a, 0, sizeof(a));
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (int j = 0; j < n; j++) {
    if (a[j] != a[j + 1]) s++;
  }
  cout << s << endl;
}
