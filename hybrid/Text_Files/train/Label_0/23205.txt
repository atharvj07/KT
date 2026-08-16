#include <bits/stdc++.h>
using namespace std;
int n;
string a;
string b;
vector<int> da;
vector<int> db;
bool win(char a, char b) {
  if (a == 'P' && b == 'R') return true;
  if (a == 'R' && b == 'S') return true;
  if (a == 'S' && b == 'P') return true;
  return false;
}
int main() {
  cin >> n >> a >> b;
  int i = 0, j = 0, sa = 0, sb = 0;
  da.push_back(0);
  db.push_back(0);
  do {
    if (win(a[i], b[j])) ++sa;
    if (win(b[j], a[i])) ++sb;
    da.push_back(sa);
    db.push_back(sb);
    i = (i + 1) % a.length();
    j = (j + 1) % b.length();
  } while (i != 0 || j != 0);
  int k = da.size() - 1;
  cout << db[n % k] + db[k] * (n / k) << ' ';
  cout << da[n % k] + da[k] * (n / k) << endl;
  return 0;
}
