#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
int n;
string a, b;
string fir[N], sec[N];
map<string, int> m;
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    cin >> a >> b;
    fir[i] = a.substr(0, 3);
    sec[i] = a.substr(0, 2) + b.substr(0, 1);
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) m[fir[j]]++;
    for (int j = 1; j <= n; j++)
      if (m[fir[j]] > 1) fir[j] = sec[j];
    m.clear();
  }
  for (int i = 1; i <= n; i++) {
    m[fir[i]]++;
    if (m[fir[i]] > 1) {
      puts("NO");
      return 0;
    }
  }
  puts("YES");
  for (int i = 1; i <= n; i++) cout << fir[i] << endl;
  return 0;
}
