#include <bits/stdc++.h>
using namespace std;
string str;
long long ans[2001], sum[2001], temp, pal[2001][2001], n;
int main() {
  ios_base::sync_with_stdio(false);
  cin >> str;
  n = str.size();
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n - i; j++) {
      int x = j;
      int y = j + i;
      if (x == y)
        pal[x][y] = 1;
      else if (x == y - 1 && str[x] == str[y])
        pal[x][y] = 1;
      else if (pal[x + 1][y - 1] == 1 && str[x] == str[y])
        pal[x][y] = 1;
    }
  for (int i = 0; i < n; i++) {
    temp = 0;
    for (int j = 0; j <= i; j++)
      if (pal[j][i]) temp++;
    sum[i] = (i ? sum[i - 1] : 0) + temp;
  }
  for (int i = 0; i < n; i++) {
    temp = 0;
    for (int j = 0; j <= i; j++) temp += pal[j][i] * sum[j - 1];
    ans[i] = ans[i - 1] + temp;
  }
  cout << ans[n - 1] << endl;
}
