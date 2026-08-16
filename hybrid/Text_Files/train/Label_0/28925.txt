#include <bits/stdc++.h>
using namespace std;
int arr[10000];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int r;
    cin >> r;
    while (r--) {
      int c;
      cin >> c;
      arr[c]++;
    }
  }
  for (int i = 1; i <= 103; i++) {
    if (arr[i] == n) cout << i << " ";
  }
  cout << endl;
  return 0;
}
