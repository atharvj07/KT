#include <bits/stdc++.h>
using namespace std;
void err() {
  cout << "shit" << endl;
  exit(1);
}
int main() {
  int n;
  scanf("%d", &n);
  int ans = 0;
  for (int i = 1; i < n; i++) {
    ans += 2 * i - 1;
  }
  ans = ans * 2 + 2 * n - 1;
  printf("%d\n", ans);
  return 0;
}
