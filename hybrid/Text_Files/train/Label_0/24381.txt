#include <bits/stdc++.h>
using namespace std;
const long long INF = 2e18;
long long mdl = 1e9 + 7;
int n;
string s;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n;
  cin >> s;
  int cur = 0;
  for (int i = 0; i < n; i++) {
    if (s[i] == '(')
      cur++;
    else
      cur--;
  }
  if (cur != 0) {
    cout << 0 << endl;
    cout << 1 << " " << 1 << endl;
    return 0;
  }
  int numPairs = 0, x, y;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      swap(s[i], s[j]);
      int count = 0, minVal = 0, minIdx = -1, curPairs = 0;
      for (int k = 0; k < n; k++) {
        if (s[k] == '(')
          count++;
        else
          count--;
        if (count < minVal) {
          minVal = count;
          minIdx = k;
        }
      }
      cur = 0;
      for (int k = minIdx + 1; k < n; k++) {
        if (s[k] == '(')
          cur++;
        else
          cur--;
        if (cur == 0) curPairs++;
      }
      for (int k = 0; k <= minIdx; k++) {
        if (s[k] == '(')
          cur++;
        else
          cur--;
        if (cur == 0) curPairs++;
      }
      if (curPairs > numPairs) {
        x = i + 1;
        y = j + 1;
        numPairs = curPairs;
      }
      swap(s[i], s[j]);
    }
  }
  cout << numPairs << endl;
  cout << x << " " << y << endl;
}
