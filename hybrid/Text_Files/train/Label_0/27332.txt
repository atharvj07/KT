#include <bits/stdc++.h>
using namespace std;
int main() {
  int n = 0;
  long long x = 0;
  char signo = ' ';
  long helados = 0;
  int chamacos_tristes = 0;
  cin >> n;
  cin >> x;
  for (int i = 0; i < n; i++) {
    cin >> signo;
    cin >> helados;
    if (signo == '+')
      x += helados;
    else if (x < helados)
      chamacos_tristes++;
    else
      x -= helados;
  }
  cout << x << " " << chamacos_tristes;
  return 0;
}
