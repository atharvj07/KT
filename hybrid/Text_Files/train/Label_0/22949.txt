#include <bits/stdc++.h>
using namespace std;
int a, b, temp, ans;
int main() {
  cin >> a >> b;
  temp = abs(b - a);
  if (temp % 2 == 0) {
    for (int i = 1; i <= temp / 2; i++) ans += i;
    cout << ans * 2;
  } else {
    for (int i = 1; i <= temp / 2 + 1; i++) {
      ans += i;
    }
    ans *= 2;
    ans -= temp / 2 + 1;
    cout << ans;
  }
}
