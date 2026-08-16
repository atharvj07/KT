#include <iostream>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  int a[2] = {1, M + 2}, b[2] = {M + 1, 2 * M + 1};
  for (int i = 0; i < M; ++i) {
    cout << (a[i & 1] + (i >> 1)) << ' '
         << (b[i & 1] - (i >> 1)) << endl;
  }

  return 0;
}
