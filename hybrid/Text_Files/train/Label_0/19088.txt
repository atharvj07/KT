#include <bits/stdc++.h>
using namespace std;
string s;
int i, j, k, l;
int q = 0, rq, rh;
int h;
int hnow;
int qnow;
int main() {
  cin >> s;
  for (i = 0; i < s.length(); i++)
    if (s[i] == 'H')
      h++;
    else
      q++;
  q = int(sqrt(double(q) + 1e-9));
  h = h / (q + 1);
  l = h + q;
  for (i = 0; i < l; i++)
    if (s[i] == 'H')
      hnow++;
    else
      qnow++;
  i--;
  int p = 0;
  while (true) {
    if (hnow == h && qnow == q) {
      p++;
      if (p * p > 1000000) break;
      string code = s.substr(i - l + 1, l);
      string outp = "";
      for (int i = 0; i < l; i++)
        if (code[i] == 'H')
          outp += 'H';
        else
          outp += code;
      if (outp == s) {
        cout << "Yes" << endl;
        exit(0);
      }
    }
    i++;
    if (i == s.length()) break;
    if (s[i] == 'H')
      hnow++;
    else
      qnow++;
    if (s[i - l] == 'H')
      hnow--;
    else
      qnow--;
  };
  cout << "No" << endl;
  return 0;
}
