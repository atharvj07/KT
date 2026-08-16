#include <bits/stdc++.h>
using namespace std;
int city[51][51], plan[2501][2], n;
int main() {
  cin >> n;
  for (int i = 1; i <= n * n; i++) {
    cin >> plan[i][0] >> plan[i][1];
  }
  for (int i = 1; i <= n * n; i++) {
    if (city[plan[i][0]][plan[i][1]] < 1) {
      cout << i << endl;
      for (int k = 1; k <= n; k++) {
        city[plan[i][0]][k]++;
        ;
        city[k][plan[i][1]]++;
      }
    }
  }
  return 0;
}
