#include <bits/stdc++.h>
using namespace std;
char word[105];
struct node {
  char w;
  int left;
  int right;
} words[105];
int hashs[15];
int record[105];
int main() {
  int n, q;
  scanf("%d%d", &n, &q);
  scanf("%s", word + 1);
  while (q--) {
    memset(hashs, 0, sizeof(hashs));
    int l, r;
    scanf("%d%d", &l, &r);
    for (int i = l; i <= r; i++) {
      words[i].w = word[i];
      words[i].right = i + 1;
      words[i].left = i - 1;
    }
    int point = l;
    int dir = 1;
    int sign = point;
    while (point >= l && point <= r) {
      if (words[point].w == '0' - 1) {
        if (dir == 1)
          words[sign].right = words[point].right,
          words[words[point].right].left = sign, point = words[sign].right;
        else
          words[sign].left = words[point].left,
          words[words[point].left].right = sign, point = words[sign].left;
        continue;
      }
      if (words[sign].w == '>' && words[point].w == '<')
        words[sign].w = '0' - 1;
      if (words[sign].w == '<' && words[point].w == '>')
        words[sign].w = '0' - 1;
      if (words[sign].w == '<' && words[point].w == '<' && sign != point)
        words[sign].w = '0' - 1;
      if (words[sign].w == '>' && words[point].w == '>' && sign != point)
        words[sign].w = '0' - 1;
      if (words[point].w >= '0' && words[point].w <= '9')
        hashs[words[point].w - '0']++, words[point].w--;
      else if (words[point].w == '>')
        dir = 1;
      else if (words[point].w == '<')
        dir = -1;
      sign = point;
      if (dir == 1)
        point = words[point].right;
      else
        point = words[point].left;
    }
    for (int i = 0; i <= 9; i++)
      if (i == 9)
        printf("%d\n", hashs[i]);
      else
        printf("%d ", hashs[i]);
  }
}
