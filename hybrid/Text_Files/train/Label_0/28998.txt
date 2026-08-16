#include <bits/stdc++.h>
using namespace std;
int sayi_s;
vector<int> sayilar;
int string_s;
int toplam;
int a_mi_b_mi;
int main() {
  scanf("%d", &sayi_s);
  for (int i = 0; i < sayi_s; i++) {
    sayilar.push_back(0);
    scanf(" %d", &sayilar[i]);
  }
  for (int i = sayi_s - 1; i >= 0; i--) {
    toplam += string_s;
    sayilar[i] -= toplam;
    string_s += sayilar[i];
    toplam += sayilar[i];
    while (sayilar[i]) {
      for (int j = 0; j <= i; j++) {
        if (a_mi_b_mi) {
          printf("a");
        } else {
          printf("b");
        }
      }
      sayilar[i]--;
      a_mi_b_mi = (a_mi_b_mi + 1) % 2;
    }
  }
  return 0;
}
