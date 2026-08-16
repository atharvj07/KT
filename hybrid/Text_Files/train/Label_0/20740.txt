#include <bits/stdc++.h>
using namespace std;
int n, freq[15], r;
string ans[] = {"1869", "6819", "9186", "6198", "1698", "1986", "1896"};
string s;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> s;
  n = s.size();
  freq[1] = freq[6] = freq[8] = freq[9] = -1;
  for (int i = 0; i < n; i++) freq[s[i] - '0']++;
  for (int i = 1; i < 10; i++) {
    for (int j = 0; j < freq[i]; j++) {
      cout << i;
      r = (r * 10 + i) % 7;
    }
  }
  for (int i = 0; i < 7; i++) {
    int tmp = r;
    for (int j = 0; j < 4; j++) tmp = (tmp * 10 + ans[i][j] - '0') % 7;
    if (!tmp) {
      cout << ans[i];
      break;
    }
  }
  for (int i = 0; i < freq[0]; i++) cout << 0;
  return 0;
}
