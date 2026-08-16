#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  int N, M, k, a;
  cin >> N >> M;
  vector<int> s(N);
  for (int i = 0; i != M; ++i) {
    cin >> k;
    for (int j = 0; j != k; ++j) {
      cin >> a;
      s[a-1] |= (1 << i);
    }
  }

  int p{};
  for (int i = 0; i != M; ++i) {
    cin >> a;
    p |= (a << i);
  }
  
  int ans{};
  int n = lround(pow(2,N));
  for (int i = 0; i != n; ++i) {
    int q{p};
    for (int j = 0; j != N; ++j) {
      if (i & (1 << j)) q = q ^ s[j];
    }
    if (!q) ++ans;
  }
  cout << ans << endl;
}
