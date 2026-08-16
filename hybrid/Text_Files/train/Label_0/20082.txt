#include <bits/stdc++.h>
using namespace std;
long long K, maxarea = 1, input;
vector<long long> side, length;
int main() {
  for (int i = 0; i < 3; i++) {
    cin >> input;
    side.push_back(input);
    side[i]--;
  }
  cin >> K;
  sort(side.begin(), side.end());
  for (int i = 0; i < 3; i++) {
    if (side[i] >= K / (3 - i)) {
      length.push_back(K / (3 - i));
      K -= K / (3 - i);
    } else {
      length.push_back(side[i]);
      K -= side[i];
    }
  }
  for (int i = 0; i < 3; i++) maxarea *= (length[i] + 1);
  cout << maxarea << endl;
  return 0;
}
