#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int ar[n];
  for (int i = 0; i < n; i++) cin >> ar[i];
  int maxi = 0, mini = 0;
  for (int i = 0; i < n; i++) {
    if (ar[i] > ar[maxi]) maxi = i;
    if (ar[i] <= ar[mini]) mini = i;
  }
  if (maxi == mini)
    cout << "0";
  else if (maxi > mini)
    cout << maxi + n - mini - 2;
  else
    cout << maxi + n - mini - 1;
  return 0;
}
