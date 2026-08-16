#include <bits/stdc++.h>
using namespace std;
int main() {
  int t, i, max = 0, k;
  string s;
  cin >> t;
  vector<int> v;
  while (t) {
    v.clear();
    max = 0;
    cin >> k >> s;
    for (i = 0; i < k; i++) {
      if (s[i] == 'A') {
        v.push_back(i);
      }
    }
    v.push_back(k);
    for (i = 0; i < v.size() - 1; i++) {
      if (v[i + 1] - v[i] - 1 > max) {
        max = v[i + 1] - v[i] - 1;
      }
    }
    cout << max << endl;
    t--;
  }
}
