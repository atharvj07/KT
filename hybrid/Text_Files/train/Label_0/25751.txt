#include <bits/stdc++.h>
using namespace std;
int a1, a2, a3, a4;
int head;
int b, c;
int nott(int x) {
  if (x == 4) return 7;
  return 4;
}
int main() {
  cin >> a1 >> a2 >> a3 >> a4;
  if (abs(a3 - a4) > 1) {
    cout << -1 << endl;
    return 0;
  }
  if (a3 > a4) head = 4;
  if (a4 > a3) head = 7;
  c = a3;
  b = a4;
  if (!head) {
    if (b != a1)
      head = 4;
    else
      head = 7;
  }
  if (head) {
    if (head == 7)
      c++;
    else
      b++;
  }
  if (b > a1 || c > a2) {
    cout << -1 << endl;
    return 0;
  }
  if (head == 7) {
    cout << 7;
    a2--;
    a4--;
    c--;
  }
  for (int i = 0; i < a1 - (b - 1); ++i) cout << 4;
  for (int i = 0; i < b - 1 - (b == c + 1); ++i) cout << 74;
  for (int i = 0; i < a2 - (b - 1) + (b == c + 1); ++i) cout << 7;
  if (b == c + 1) cout << 4;
  cout << endl;
  return 0;
}
