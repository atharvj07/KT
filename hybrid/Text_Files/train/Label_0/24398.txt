#include <bits/stdc++.h>
using namespace std;
int main() {
  char a[1000];
  int i, y = 0, u = 0, z = 0, len;
  cin >> a;
  len = strlen(a);
  if (len < 5) {
    cout << "Too weak";
    return 0;
  }
  for (i = 0; a[i] != '\0'; i++) {
    if (isupper(a[i])) y++;
    if (islower(a[i])) z++;
    if (a[i] >= '0' && a[i] <= '9') u++;
  }
  if (y > 0 && z > 0 && u > 0) {
    cout << "Correct";
    return 0;
  }
  cout << "Too weak";
  return 0;
}
