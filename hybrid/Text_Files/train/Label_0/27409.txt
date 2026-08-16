#include <bits/stdc++.h>
using namespace std;
int main() {
  int x, input, past = 0, max = 0;
  vector<int> arr, arr2;
  cin >> x;
  while (x--) {
    cin >> input;
    arr.push_back(input);
    if (find(arr2.begin(), arr2.end(), input) == arr2.end())
      arr2.push_back(input);
  }
  for (int i = 0; i < arr2.size(); i++) {
    past = count(arr.begin(), arr.end(), arr2[i]);
    if (past > max) max = past;
  }
  cout << max;
  return 0;
}
