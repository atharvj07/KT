#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector
#define pb push_back

// 非連結を消せば連結

int main(void)
{
  int n;
  cin >> n;

  cout << n * (n - 1) / 2 - n / 2 << endl;
  for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
      if (i + j == n + 1 - (n % 2)) continue;
      cout << i << " " << j << endl;
    }
  }
  return 0;
}
