#include <bits/stdc++.h>
using namespace std;
char a[3000][3000];
int lamp[3000];
int main() {
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      cin >> a[i][j];
      if (a[i][j] == '1') lamp[j]++;
    }
  for (int i = 0; i < n; i++) {
    int f = 1;
    for (int j = 0; j < m; j++) {
      if (a[i][j] == '1' && lamp[j] == 1) f = 0;
    }
    if (f) {
      cout << "YES";
      return 0;
    }
  }
  cout << "NO";
}
