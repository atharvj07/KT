#include <bits/stdc++.h>
using namespace std;
int main() {
  int a1, a2, a3;
  int b1, b2, b3, n;
  cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3 >> n;
  int numb = a1 + a2 + a3;
  int numb1 = b1 + b2 + b3;
  numb = numb + 4;
  int req = numb / 5;
  numb1 = numb1 + 9;
  int req2 = numb1 / 10;
  if (req + req2 <= n)
    cout << "YES";
  else
    cout << "NO";
}
