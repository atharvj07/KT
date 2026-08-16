#include <bits/stdc++.h>
using namespace std;
int main() {
  vector<int> a;
  int j;
  int b[5] = {1, 1, 2, 7, 4};
  for (int i = 0; i < 5; i++) {
    cin >> j;
    a.push_back(j / b[i]);
  }
  sort(a.begin(), a.end());
  cout << a[0] << endl;
}
