#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  vector<int> v;
  int a[n];
  int b[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    v.push_back(a[i]);
    b[i] = a[i];
  }
  sort(b, b + n);
  string s;
  cin >> s;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '1') {
      if (i != n - 2) {
        for (int j = i + 1; j < s.size(); j++) {
          if (s[j] == '0') {
            sort(v.begin() + i, v.begin() + j + 1);
            i = j;
            break;
          } else if (s[j] == '1' && j == s.size() - 1) {
            sort(v.begin() + i, v.end());
            i = j;
            break;
          }
        }
      } else {
        if (v[i] > v[i + 1]) {
          swap(v[i], v[i + 1]);
        }
      }
    }
  }
  bool pos = 1;
  for (int i = 0; i < v.size(); i++) {
    if (v[i] != b[i]) {
      pos = 0;
      break;
    }
  }
  if (pos == 1) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}
