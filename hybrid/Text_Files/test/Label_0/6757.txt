#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:134217728")
using namespace std;
int n, m;
void print(int x) {
  if (x > m) return;
  cout << x << ' ';
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    print(2 * n + i * 2 + 1);
    print(i * 2 + 1);
    print(2 * n + i * 2 + 2);
    print(i * 2 + 2);
  }
  return 0;
}
