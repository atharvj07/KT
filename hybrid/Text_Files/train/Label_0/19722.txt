#include <bits/stdc++.h>
using namespace std;
long long int A[2001], B[2001];
vector<long long int> X;
int main() {
  long long int n, m;
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    cin >> A[i];
  }
  for (int i = 0; i < n; i++) {
    cin >> B[i];
  }
  for (int i = 0; i < n; i++) {
    long long int x = (B[i] - (A[0] % m) + m) % m;
    X.push_back(x);
  }
  sort(B, B + n);
  sort(X.begin(), X.end());
  for (int i = 0; i < X.size(); i++) {
    int fl = 0;
    vector<long long int> C;
    for (int j = 0; j < n; j++) {
      C.push_back((A[j] + X[i]) % m);
    }
    sort(C.begin(), C.end());
    for (int j = 0; j < n; j++) {
      if (C[j] != B[j]) {
        fl = 1;
      }
    }
    if (fl != 1) {
      cout << X[i] << endl;
      return 0;
    }
  }
  return 0;
}
