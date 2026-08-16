#include <bits/stdc++.h>
using namespace std;
void *mybsearch(const void *key, const void *base, size_t num, size_t width,
                int (*cmp)(const void *elem1, const void *elem2)) {
  void *result, *prevResult = NULL;
  while (true) {
    if (result = bsearch(key, base, num, width, cmp))
      prevResult = result;
    else
      break;
    num = ((char *)result - (char *)base) / width;
  }
  return prevResult;
}
int cmp(const void *a, const void *b) { return *(int *)a - *(int *)b; }
struct Pair {
  int a;
  bool good;
  Pair() { good = false; }
};
int main() {
  Pair mas[109][109];
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> mas[i][j].a;
    }
  }
  for (int i = 0; i < n; i++) {
    mas[i][i].good = true;
  }
  int t = n - 1;
  for (int j = 0; j < n; j++) {
    mas[t--][j].good = true;
  }
  int magic = (n - 1) / 2;
  for (int j = 0; j < n; j++) {
    mas[magic][j].good = true;
  }
  for (int j = 0; j < n; j++) {
    mas[j][magic].good = true;
  }
  int count = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (mas[i][j].good == true) count += mas[i][j].a;
    }
  }
  cout << count << endl;
  return 0;
}
