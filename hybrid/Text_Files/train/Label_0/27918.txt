#include <bits/stdc++.h>
using namespace std;
char s1[10005], s2[1000001];
int l1, l2, q[28][10005], l[28];
int get_next_char_after(char x, int i) {
  int a = x - 'a', low = 0, high = l[a] - 1, mid;
  while (low < high) {
    mid = (low + high) / 2;
    if (q[a][mid] <= i)
      low = mid + 1;
    else
      high = mid;
  }
  if (q[a][low] == -1 || q[a][low] <= i)
    return -1;
  else
    return q[a][low];
}
bool n_copies_ok(int n) {
  int j = -1;
  for (int i = 0; i < l2 && n > 0; i++) {
    do {
      int k = get_next_char_after(s2[i], j);
      if (k == -1) {
        j = k;
        n--;
      } else
        j = k;
    } while (n > 0 && (j == -1 || s1[j] != s2[i]));
  }
  return (n > 0);
}
int main() {
  scanf("%s", s1);
  scanf("%s", s2);
  l1 = strlen(s1);
  l2 = strlen(s2);
  memset(l, 0, sizeof(l));
  for (int i = 0; i < l1; i++) {
    int a = s1[i] - 'a';
    q[a][l[a]++] = i;
  }
  int low = (l2 / l1), high = l2;
  while (low < high) {
    int mid = (low + high) / 2;
    if (n_copies_ok(mid)) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }
  if (!n_copies_ok(low)) {
    printf("-1\n");
  } else {
    printf("%d\n", low);
  }
}
