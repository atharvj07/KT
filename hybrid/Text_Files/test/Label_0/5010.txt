#include <bits/stdc++.h>
using namespace std;
long long n, m, s[100010], length[100010], cont[100010], num[100010],
    freq[100010];
int main() {
  cin >> m >> s[0] >> num[0];
  freq[0] = 1;
  for (int i = 1; i < m; i++) {
    cin >> s[i];
    if (s[i] == 1) {
      cin >> num[i];
      freq[i] = freq[i - 1] + 1;
    } else {
      cin >> length[i] >> cont[i];
      freq[i] = freq[i - 1] + (length[i] * cont[i]);
    }
  }
  cin >> n;
  for (int i = 0; i < n; i++) {
    long long x, ii;
    cin >> x;
    while (1) {
      ii = lower_bound(freq, freq + m, x) - freq;
      if (s[ii] == 1) {
        cout << num[ii] << " ";
        break;
      } else {
        x = (x - freq[ii - 1] - 1) % length[ii] + 1;
      }
    }
  }
}
