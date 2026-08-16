#include <bits/stdc++.h>
using namespace std;
class compare {
 public:
  bool operator()(int x, int y) { return x > y; }
};
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n;
  cin >> n;
  vector<int> vec;
  int ara[n + 3];
  ara[0] = 0;
  for (int i = 0; i < n; i++) {
    cin >> ara[i + 1];
  }
  for (int i = 1; i <= n; i++) {
    int xar[n + 3];
    xar[0] = ara[1] - ara[0];
    for (int k = 0; k < i; k++) {
      xar[k] = ara[k + 1] - ara[k];
    }
    int j;
    for (j = 1; j <= n; j++) {
      int xx = (j - 1) % i;
      if (ara[j] == xar[xx] + ara[j - 1]) {
      } else
        break;
    }
    if (j == n + 1) {
      vec.push_back(i);
    }
  }
  int siz = vec.size();
  cout << siz << endl;
  for (int i = 0; i < siz; i++) cout << vec[i] << " ";
  cout << endl;
  return 0;
}
