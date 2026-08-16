#include <bits/stdc++.h>
using namespace std;
bool solve(int a, int b, char str[]) {
  vector<int> arr;
  int curr = 0;
  for (int i = 0; str[i] != 0; i++) {
    if (str[i] == '.')
      curr++;
    else if (str[i] == 'X' && curr != 0) {
      arr.push_back(curr);
      curr = 0;
    }
  }
  if (curr != 0) arr.push_back(curr);
  int crit = 0, non_crit = 0, crit_len;
  for (int i = 0; i < arr.size(); i++) {
    int s = arr[i];
    if ((s >= b && s < a) || ((s - a) % 2 == 0 && (s - a) / 2 >= 2 * b) ||
        ((s - a) % 2 == 1 && (s - a + 1) / 2 >= 2 * b)) {
      return false;
    }
    if (s >= 2 * b) {
      crit++;
      crit_len = s;
    } else if (s >= a)
      non_crit++;
  }
  if (crit > 1) {
    return false;
  }
  if (crit == 0) {
    return (non_crit % 2 == 1);
  }
  for (int i = 0; i <= crit_len - a; i++) {
    int j = crit_len - a - i;
    if (!(i >= b && i < a) && !(j >= b && j < a) && !(i >= 2 * b) &&
        !(j >= 2 * b) && ((non_crit + (i >= a) + (j >= a)) % 2 == 0))
      return true;
  }
  return false;
}
int main() {
  int q;
  cin >> q;
  for (int i = 0; i < q; i++) {
    int a, b;
    char str[300005];
    cin >> a >> b >> str;
    cout << (solve(a, b, str) ? "YES" : "NO") << endl;
  }
}
