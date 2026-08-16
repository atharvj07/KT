#include <bits/stdc++.h>
using namespace std;
bool isOdd(int val) { return val % 2; }
int nod(int a, int b) {
  if (a > b) swap(a, b);
  while (a) {
    b %= a;
    swap(a, b);
  }
  return b;
}
int main(int argc, char **argv) {
  int n;
  std::cin >> n;
  int div = 0;
  if (isOdd(n)) {
    div = (n - 1) / 2;
  } else {
    div = n / 2;
  }
  for (int i = div; i > 0; --i) {
    int a = i;
    int b = n - a;
    if (nod(a, b) == 1) {
      cout << a << " " << b;
      return 0;
    }
  }
  return 0;
}
