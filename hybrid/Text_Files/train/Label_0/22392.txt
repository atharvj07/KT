#include <bits/stdc++.h>
using namespace std;
vector<int> arr;
int main() {
  int n;
  cin >> n;
  arr.assign(n + 1, 0);
  int curr = 1;
  for (int i = 2; i <= n; i++) {
    if (!arr[i]) {
      for (int j = 1; i * j <= n; j++)
        if (!arr[i * j]) arr[i * j] = curr;
      curr++;
    }
  }
  for (int i = 2; i < n + 1; i++) cout << arr[i] << " ";
  cout << endl;
  return 0;
}
