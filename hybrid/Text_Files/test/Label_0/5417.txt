#include <bits/stdc++.h>
int faster_in() {
  int r = 0, c;
  for (c = getchar(); c <= 32; c = getchar())
    ;
  if (c == '-') return -faster_in();
  for (; c > 32; r = (r << 1) + (r << 3) + c - '0', c = getchar())
    ;
  return r;
}
using namespace std;
const int INF = int(1e9 + 7);
string txt, txt2;
deque<int> cola1, cola2;
vector<pair<int, int> > operaciones;
void init() {
  string txt1;
  txt1 = txt + "c";
  int c = 1;
  for (int i = 0; i < txt1.size() - 1; ++i) {
    if (txt1[i] == txt1[i + 1])
      c++;
    else {
      cola1.push_back(c);
      c = 1;
    }
  }
  txt1 = txt2;
  txt1 = txt1 + "c";
  c = 1;
  for (int i = 0; i < txt1.size() - 1; ++i) {
    if (txt1[i] == txt1[i + 1])
      c++;
    else {
      cola2.push_back(c);
      c = 1;
    }
  }
}
void tle() {
  cout << "wrong\n";
  tle();
}
void igualdad() {
  int num1, num2, num3, num4, num5;
  while (cola1.size() > 2 || cola2.size() > 2) {
    if (cola1.size() >= cola2.size()) {
      num1 = cola1.front();
      cola1.pop_front();
      num2 = cola1.front();
      cola1.pop_front();
      num3 = cola1.front();
      cola1.pop_front();
      num4 = cola2.front();
      cola2.pop_front();
      if (cola2.size() > 0) {
        num5 = cola2.front();
        cola2.pop_front();
      } else
        num5 = 0;
      cola1.push_front(num3 + num4);
      cola2.push_front(num2 + num5);
      cola2.push_front(num1);
      operaciones.push_back(pair<int, int>(num1 + num2, num4));
    } else {
      num1 = cola2.front();
      cola2.pop_front();
      num2 = cola2.front();
      cola2.pop_front();
      num3 = cola2.front();
      cola2.pop_front();
      num4 = cola1.front();
      cola1.pop_front();
      if (cola1.size() > 0) {
        num5 = cola1.front();
        cola1.pop_front();
      } else
        num5 = 0;
      cola2.push_front(num3 + num4);
      cola1.push_front(num2 + num5);
      cola1.push_front(num1);
      operaciones.push_back(pair<int, int>(num4, num1 + num2));
    }
  }
  bool fswap = false;
  if (cola1.size() < cola2.size()) {
    swap(cola2, cola1);
    fswap = 1;
  }
  if (cola1.size() != 2) tle();
  if (cola2.size() == 1) {
    if (fswap == false)
      operaciones.push_back(pair<int, int>(cola1.front(), 0));
    else
      operaciones.push_back(pair<int, int>(0, cola1.front()));
  } else {
    num1 = cola1.front();
    cola1.pop_front();
    num2 = cola1.front();
    cola1.pop_front();
    num3 = cola2.front();
    cola2.pop_front();
    num4 = cola2.front();
    cola2.pop_front();
    operaciones.push_back(pair<int, int>(num1 + num2, num3));
    operaciones.push_back(pair<int, int>(0, num1));
  }
}
pair<int, int> change(deque<int> &prim, deque<int> &segun) {
  int num1, num2, num3, num4, num5, num6;
  num1 = prim.front();
  prim.pop_front();
  num2 = prim.front();
  prim.pop_front();
  num3 = prim.front();
  prim.pop_front();
  num4 = prim.front();
  prim.pop_front();
  num5 = segun.front();
  segun.pop_front();
  if (segun.size() > 0) {
    num6 = segun.front();
    segun.pop_front();
  } else
    num6 = 0;
  prim.push_front(num4 + num5);
  segun.push_front(num6 + num3);
  segun.push_front(num2);
  segun.push_front(num1);
  return pair<int, int>(num1 + num2 + num3, num5);
}
void desigual() {
  int valor1, valor2;
  valor1 = cola1.size();
  valor2 = cola2.size();
  while (max(valor1 - valor2, valor2 - valor1) >= 3) {
    if (cola1.size() > cola2.size()) {
      operaciones.push_back(change(cola1, cola2));
    } else {
      pair<int, int> auxresp = change(cola2, cola1);
      swap(auxresp.first, auxresp.second);
      operaciones.push_back(auxresp);
    }
    valor1 = cola1.size();
    valor2 = cola2.size();
  }
  int num1, num2, num3, num4;
  while (cola1.size() > 1 || cola2.size() > 1) {
    num1 = cola1.front();
    cola1.pop_front();
    if (cola1.size() > 0) {
      num2 = cola1.front();
      cola1.pop_front();
    } else
      num2 = 0;
    num3 = cola2.front();
    cola2.pop_front();
    if (cola2.size() > 0) {
      num4 = cola2.front();
      cola2.pop_front();
    } else
      num4 = 0;
    cola1.push_front(num3 + num2);
    cola2.push_front(num1 + num4);
    operaciones.push_back(pair<int, int>(num1, num3));
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> txt >> txt2;
  init();
  deque<int> cola;
  int tot = 0;
  if (txt[0] == txt2[0]) {
    if (cola1.size() == 1) {
      for (int i = 0; i < cola2.size(); i += 2) {
        tot += cola2.front();
        cola.push_back(cola2.front());
        int auxvalor = cola.size(), n = cola2.size();
        cola2.pop_front();
        if (n - auxvalor - auxvalor <= 2) {
          int auxvalor2 = cola.back();
          cola.pop_back();
          cola.push_back(auxvalor2 + cola1.front());
          operaciones.push_back(pair<int, int>(0, tot));
          break;
        }
        if (cola2.size() > 1) {
          tot += cola2.front();
          cola.push_back(cola2.front());
          cola2.pop_front();
        }
      }
      cola1 = cola;
      desigual();
    } else if (cola2.size() == 1) {
      swap(cola1, cola2);
      for (int i = 0; i < cola2.size(); i += 2) {
        tot += cola2.front();
        cola.push_back(cola2.front());
        int auxvalor = cola.size(), n = cola2.size();
        cola2.pop_front();
        if (n - auxvalor - auxvalor <= 2) {
          int auxvalor2 = cola.back();
          cola.pop_back();
          cola.push_back(auxvalor2 + cola1.front());
          operaciones.push_back(pair<int, int>(tot, 0));
          break;
        }
        if (cola2.size() > 1) {
          tot += cola2.front();
          cola.push_back(cola2.front());
          cola2.pop_front();
        }
      }
      cola1 = cola;
      swap(cola1, cola2);
      desigual();
    } else
      igualdad();
  } else {
    desigual();
  }
  cout << operaciones.size() << endl;
  for (int i = 0; i < operaciones.size(); ++i) {
    cout << operaciones[i].first << " " << operaciones[i].second << endl;
  }
}
