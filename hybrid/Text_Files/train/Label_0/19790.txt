#include <bits/stdc++.h>
using namespace std;
vector<int> vector1(3000), vector2(3000);
int a[1001][1001];
int main() {
  long long sum = 0;
  int i, j, n;
  cin >> n;
  for (i = 0; i < n; ++i) {
    int x, y;
    cin >> x >> y;
    a[x][y] = 1;
    vector1[x + y]++;
    vector2[1000 - x + y + 1]++;
  }
  for (i = 0; i < 1001; ++i) {
    for (j = 0; j < 1001; ++j)
      if (a[i][j] == 1) {
        int x = 0, y = 0;
        if (vector2[1000 - i + j + 1] > 1) x = vector2[1000 - i + j + 1] - 1;
        if (vector1[i + j] > 1) y = vector1[i + j] - 1;
        sum += x + y;
        vector1[i + j]--;
        vector2[1000 - i + j + 1]--;
      }
  }
  cout << sum;
  return 0;
}
