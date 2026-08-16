#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int i = n, j = 1, output[17] = {-1}, output_l = 0;
  while (i > 0) {
    if (i % 2 == 1) {
      output[output_l] = j;
      output_l++;
    }
    i /= 2;
    j++;
  }
  for (int i = output_l - 1; i > -1; i--) {
    cout << output[i] << " ";
  }
  cout << endl;
  return 0;
}
