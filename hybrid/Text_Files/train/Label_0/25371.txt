#include <bits/stdc++.h>
using namespace std;
int v[100010];
int n, k;
int main() {
  cin >> n >> k;
  int solution = 0;
  for (int i = 1; i <= k; i++) {
    int m;
    cin >> m;
    for (int j = 1; j <= m; j++) cin >> v[j];
    int j;
    if (v[1] == 1) {
      j = 2;
      while (v[j] == v[j - 1] + 1) j++;
      for (; j <= m; j++) {
        solution += 2;
      }
      continue;
    }
    for (j = 1; j <= m; j++)
      if (j == 1)
        solution++;
      else
        solution += 2;
  }
  cout << solution << "\n";
  return 0;
}
