#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  bool flag = 1;
  cin >> n;
  double* mas = new double[n];
  for (int i = 0; i < n; i++) {
    cin >> mas[i];
  }
  for (int i = 1; i < n - 1; i++) {
    flag = flag && (mas[i] == (mas[i - 1] + mas[i + 1]) / 2);
  }
  if (flag) {
    cout << mas[n - 1] + (mas[n - 1] - mas[n - 2]);
  } else {
    cout << mas[n - 1];
  }
  cout << endl;
  cin.get();
  return 0;
}
