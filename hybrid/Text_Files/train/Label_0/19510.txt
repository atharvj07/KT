#include <bits/stdc++.h>
using namespace std;
int main() {
  int arr[95]{};
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    int m;
    scanf("%d", &m);
    arr[m] = 1;
  }
  int c = 0;
  int ans = 0;
  int i;
  for (i = 1; i <= 90; i++) {
    c++;
    if (arr[i] != 0) {
      c = 0;
    }
    if (c == 15) {
      break;
    }
  }
  if (i == 91) i--;
  cout << i;
}
