#include <bits/stdc++.h>
using namespace std;
char a[1002];
int i, j;
int k;
int n, q1, q2;
int an1[102], an2[102];
bool tiv(int x) {
  if (a[x] < '0') return false;
  if (a[x] > '9') return false;
  return true;
}
int main() {
  cin.getline(a, 1000);
  k = (int)(strlen(a));
  for (i = 0; i < k; i++) {
    if (i != 0 && a[i - 2] == '=') break;
    if (i == 0 || a[i - 2] == '+')
      q1++;
    else
      q2++;
    i += 3;
  }
  i = 0;
  while (!tiv(i)) i++;
  vector<int> v;
  for (i = i; i < k; i++) v.push_back(a[i] - '0');
  int p = 1;
  for (i = (int)v.size() - 1; i >= 0; i--) {
    n += p * (v[i]);
    p *= 10;
  }
  int sum = q1 * n - q2 * n;
  for (i = 0; i < q1; i++) an1[i] = n;
  for (i = 0; i < q2; i++) an2[i] = n;
  if (sum > n) {
    for (i = 0; i < q1; i++) {
      if (sum - (an1[i] - 1) <= n) {
        an1[i] -= sum - n;
        sum = n;
        break;
      } else {
        sum -= an1[i] - 1;
        an1[i] = 1;
      }
    }
  } else if (sum < n) {
    for (i = 0; i < q2; i++) {
      if (sum + (an2[i] - 1) >= n) {
        an2[i] -= n - sum;
        sum = n;
        break;
      } else {
        sum += an2[i] - 1;
        an2[i] = 1;
      }
    }
  }
  if (sum != n)
    cout << "Impossible" << endl;
  else {
    cout << "Possible" << endl;
    int k1 = 0, k2 = 0;
    for (i = 0; i < k; i++) {
      if (a[i] == '=') {
        cout << "= " << n << endl;
        break;
      }
      if (a[i] == '?') {
        if (i == 0 || a[i - 2] == '+') {
          cout << an1[k1++];
        } else {
          cout << an2[k2++];
        }
        continue;
      }
      cout << a[i];
    }
  }
}
