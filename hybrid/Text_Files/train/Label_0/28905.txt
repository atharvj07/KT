#include <bits/stdc++.h>
using namespace std;
string buf, tmp;
int len, ans[4], ans1 = 10000000;
void swap(char& a, char& b) {
  char t = a;
  a = b;
  b = t;
}
void ww(int i, char fir, char sec) {
  tmp = buf;
  ans[i] = -1;
  if (tmp.rfind(sec) != -1) {
    int pos1 = tmp.rfind(sec);
    tmp.erase(pos1, 1);
    if (tmp.rfind(fir) != -1) {
      ans[i] = 0;
      int pos2 = tmp.rfind(fir);
      if (pos1 == len - 1 && pos2 == len - 2) {
        ans[i] = 0;
        return;
      }
      int z = 1;
      while (tmp[0] == '0') {
        swap(tmp[0], tmp[z++]);
        ans[i] += 1;
      }
      ans[i] += (len - 1 - pos1) + (len - 2 - pos2);
    }
  }
}
int main() {
  cin >> buf;
  len = buf.length();
  ww(0, '0', '0');
  ww(1, '2', '5');
  ww(2, '5', '0');
  ww(3, '7', '5');
  for (int i = 0; i < 4; i++)
    if (ans[i] >= 0) ans1 = min(ans[i], ans1);
  if (ans1 != 10000000)
    printf("%d", ans1);
  else
    printf("-1");
}
