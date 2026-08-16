#include <bits/stdc++.h>
using namespace std;
int main() {
  long long v, num, i, val, mini = 100000000, r = 0;
  string s = "";
  cin >> v;
  long long ar[10];
  for (i = 1; i <= 9; i++) {
    cin >> ar[i];
    if (ar[i] <= mini) {
      mini = ar[i];
      num = i;
    }
  }
  val = v / mini;
  v = v - val * mini;
  if (val == 0) {
    cout << -1;
    return 0;
  }
  for (i = 0; i < val; i++) {
    s += to_string(num);
  }
  r = 0;
  for (i = 9; i >= 0; i--) {
    if (i > num && v >= ar[i] - mini) {
      while (v >= ar[i] - mini && r < val && s[r] - '0' < i) {
        s[r] = (i + '0');
        v -= (ar[i] - mini);
        r++;
      }
    }
  }
  cout << s;
  return 0;
}
