#include <bits/stdc++.h>
using namespace std;
template <class T>
T pwr(T b, T p) {
  T r = 1, x = b;
  while (p) {
    if (p & 1) r *= x;
    x *= x;
    p = (p >> 1);
  }
  return r;
}
template <class T>
T lcm(T a, T b) {
  return (a / __gcd(a, b)) * b;
}
template <class T>
T sqr(T a) {
  return a * a;
}
template <class T>
void xswap(T &x, T &y) {
  if (x != y) {
    x ^= y;
    y ^= x;
    x ^= y;
  }
}
template <typename T>
inline bool isOn(T &mask, int pos) {
  return ((mask) & (1LL << pos));
}
template <typename T>
inline T setf(T mask, int pos) {
  return mask = ((mask) & (~(1LL << pos)));
}
template <typename T>
inline T sett(T mask, int pos) {
  return mask = ((mask)(1LL << pos));
}
template <typename T>
inline T flip(T mask, int pos) {
  return mask = ((mask) ^ (1LL << pos));
}
template <class T1>
void put(T1 e) {
  cout << e << endl;
}
template <class T1, class T2>
void put(T1 e1, T2 e2) {
  cout << e1 << " " << e2 << endl;
}
template <class T1, class T2, class T3>
void put(T1 e1, T2 e2, T3 e3) {
  cout << e1 << " " << e2 << " " << e3 << endl;
}
template <class T1, class T2, class T3, class T4>
void put(T1 e1, T2 e2, T3 e3, T4 e4) {
  cout << e1 << " " << e2 << " " << e3 << " " << e4 << endl;
}
template <class T1, class T2, class T3, class T4, class T5>
void put(T1 e1, T2 e2, T3 e3, T4 e4, T5 e5) {
  cout << e1 << " " << e2 << " " << e3 << " " << e4 << " " << e5 << endl;
}
template <class T1>
void putv(vector<T1> e1) {
  for (int i = 0; i < e1.size(); i++)
    (!i ? cout << e1[i] : cout << " " << e1[i]);
  cout << endl;
}
template <class T1>
void puta(T1 arr[], int l) {
  for (int i = 0; i < l; i++) (!i ? cout << arr[i] : cout << " " << arr[i]);
  cout << endl;
}
template <class T1>
bool tk(T1 &e1) {
  return (cin >> e1 ? true : false);
}
template <class T1, class T2>
bool tk(T1 &e1, T2 &e2) {
  return (cin >> e1 >> e2 ? true : false);
}
template <class T1, class T2, class T3>
bool tk(T1 &e1, T2 &e2, T3 &e3) {
  return (cin >> e1 >> e2 >> e3 ? true : false);
}
template <class T1, class T2, class T3, class T4>
bool tk(T1 &e1, T2 &e2, T3 &e3, T4 &e4) {
  return (cin >> e1 >> e2 >> e3 >> e4 ? true : false);
}
priority_queue<int> que[200007];
vector<int> ans;
int main() {
  int n, shakes;
  tk(n);
  for (int i = 1; i <= n; ++i) {
    tk(shakes);
    que[shakes].push(i);
  }
  int now_shakes = 0, i = 0;
  while (i < n) {
    if (now_shakes < 0) {
      put("Impossible");
      return 0;
    } else if (que[now_shakes].empty()) {
      now_shakes -= 3;
    } else {
      ans.push_back(que[now_shakes].top());
      que[now_shakes].pop();
      now_shakes++;
      i++;
    }
  }
  put("Possible");
  putv(ans);
  return 0;
}
