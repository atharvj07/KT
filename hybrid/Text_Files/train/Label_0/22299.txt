#include <bits/stdc++.h>
using namespace std;
int a[1005], freq[1005];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int n, k;
  cin >> n >> k;
  int sets = n % 2 ? n / 2 + 1 : n / 2;
  for (int i = 0; i <= 1000; i++) freq[i] = 0;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    freq[a[i]]++;
  }
  int ct = 0;
  for (int i = 1; i <= 1000; i++)
    if (freq[i] % 2)
      ct += (freq[i] - 1);
    else
      ct += freq[i];
  if (ct >= 2 * sets)
    cout << 2 * sets << '\n';
  else
    cout << (sets - ct / 2) + ct << '\n';
  return 0;
}
