#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  int a[100];
  int v[100];
  int p[100];
  int t[100];
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int m = 3;
  int c = 0;
  for (int i = 0; i < n; i++) {
    v[i] = a[i];
    if (i == 0)
      t[i] = m;
    else {
      t[i] = p[i - 1];
    }
    int s[4];
    for (int j = 1; j <= 3; j++) {
      s[j] = 0;
    }
    s[v[i]] = 1;
    s[t[i]] = 1;
    for (int j = 1; j <= 3; j++) {
      if (s[j] == 0) {
        p[i] = j;
      }
    }
    if (t[i] == v[i]) {
      c = 1;
    }
  }
  if (c == 1) {
    cout << "NO";
  } else {
    cout << "YES";
  }
}
