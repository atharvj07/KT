#include <bits/stdc++.h>
using namespace std;
const long long MAX = 2500000000;
const int inf = 0x3f3f3f3f;
const double EPS = 1e-9;
const double PII = 2 * asin(1.0);
const long long mod = 1e9 + 7;
int double_cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
multimap<string, vector<string> > funcoes;
map<string, string> variaveis;
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    string aux;
    cin >> aux;
    cin.ignore();
    getline(cin, aux);
    string temp, func;
    vector<string> termos;
    for (int j = 0; j < ((int)aux.size()); ++j) {
      if (aux[j] != ' ') {
        if (aux[j] == '(') {
          func = temp;
          temp.clear();
        } else if (aux[j] == ')' || aux[j] == ',') {
          termos.push_back(temp);
          temp.clear();
        } else
          temp += aux[j];
      }
    }
    funcoes.insert(make_pair(func, termos));
  }
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    string a, b;
    cin >> a >> b;
    variaveis[b] = a;
  }
  scanf("%d", &n);
  cin.ignore();
  for (int i = 0; i < n; ++i) {
    int cont = 0;
    string aux;
    getline(cin, aux);
    string temp, func;
    vector<string> termos;
    for (int j = 0; j < ((int)aux.size()); ++j) {
      if (aux[j] != ' ') {
        if (aux[j] == '(') {
          func = temp;
          temp.clear();
        } else if (aux[j] == ')' || aux[j] == ',') {
          termos.push_back(temp);
          temp.clear();
        } else
          temp += aux[j];
      }
    }
    for (auto i : funcoes) {
      if (i.first != func) continue;
      bool pode = true;
      if (((int)termos.size()) != ((int)i.second.size()))
        pode = false;
      else {
        for (int j = 0; j < ((int)i.second.size()); ++j) {
          if (i.second[j] == "T") continue;
          if (i.second[j] != variaveis[termos[j]]) {
            pode = false;
            break;
          }
        }
      }
      if (pode) cont++;
    }
    printf("%d\n", cont);
  }
}
