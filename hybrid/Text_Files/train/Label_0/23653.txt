#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    long long a[n + 5];
    for (int i = 0; i < n; i++) cin >> a[i];
    int temp = a[0], j = 1;
    int cnt = 1;
    while (j < n) {
      if (a[j] == temp) cnt++;
      j++;
    }
    if (cnt == n) {
      cout << "1";
      cout << endl;
      for (int i = 0; i < n; ++i) cout << "1 ";
    } else if (n % 2 == 0) {
      cout << "2" << endl;
      for (int i = 0; i < n; i++) {
        if (i & 1)
          cout << "2 ";
        else
          cout << "1 ";
      }
    } else {
      vector<long long> sol(n);
      bool flag = false;
      for (int i = 0; i < n; ++i) {
        if (a[i] == a[(i + 1) % n]) {
          flag = true;
          int g = i + 1;
          bool num = true;
          while (g < n) {
            if (num) {
              sol[g] = 2;
            } else
              sol[g] = 1;
            g++;
            num = !num;
          }
          g = i;
          num = true;
          while (g >= 0) {
            if (num) {
              sol[g] = 2;
            } else
              sol[g] = 1;
            g--;
            num = !num;
          }
        }
      }
      if (flag) {
        cout << "2" << endl;
        for (int i = 0; i < n; i++) cout << sol[i] << " ";
        cout << endl;
      } else {
        cout << endl << "3" << endl;
        for (int i = 0; i < n - 1; i++) {
          if (i & 1)
            cout << "2"
                 << " ";
          else
            cout << "1"
                 << " ";
        }
        cout << "3" << endl;
      }
    }
  }
  return 0;
}
