#include <bits/stdc++.h>
using namespace std;
double ang[100010];
int edge = int(1e4);
double angle, pi = 3.1415926;
int main() {
  int n, a;
  double c, la;
  cin >> n >> a;
  angle = (double)180 * (n - 2) / n;
  c = sqrt((long double)2 * edge * edge * (1 - cos(angle / 180 * pi)));
  ang[0] = 0;
  ang[1] = angle / (n - 2);
  int k;
  double minn = 1000000000.0000000;
  for (register int i = 1; i <= n - 2; i++)
    if (minn > fabs(a - i * ang[1]))
      minn = fabs(a - i * ang[1]), k = i;
    else
      break;
  cout << "2 1 " << 2 + k << endl;
  return 0;
}
