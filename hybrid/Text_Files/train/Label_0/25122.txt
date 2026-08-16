#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int a, b, w, x, c;
  cin >> a >> b >> w >> x >> c;
  if (c <= a)
    printf("0\n");
  else {
    long long int I = c - a;
    b -= (I - 1) * x;
    long long int J = ceill((double)(x - b) / (w - x));
    cout << I + J;
  }
  return 0;
}
