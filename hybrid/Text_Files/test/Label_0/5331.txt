#include <bits/stdc++.h>
using namespace std;
int a[100];
int b[100];
int main() {
  int n, L;
  cin >> n >> L;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (int i = 0; i < n; i++) {
    cin >> b[i];
  }
  vector<int> p, q;
  for (int i = 1; i < n; i++) {
    p.push_back(a[i] - a[i - 1]);
    q.push_back(b[i] - b[i - 1]);
  }
  p.push_back(L - a[n - 1] + a[0]);
  q.push_back(L - b[n - 1] + b[0]);
  for (int i = 0; i < n; i++) {
    vector<int> dum;
    for (int j = 0; j < n; j++) {
      dum.push_back(q[(j + i) % n]);
    }
    if (dum == p) {
      cout << "YES" << endl;
      exit(0);
    }
  }
  cout << "NO" << endl;
  return 0;
}
