#include <bits/stdc++.h>
using namespace std;
class machine {
 private:
  int n;
  vector<int> arr;
  int mn;
  int mx;
  int cur;
  int sz;

 public:
  machine(int n) {
    this->n = n;
    sz = 0;
    arr.resize(101);
    mn = 101;
    mx = 0;
    cur = -1;
  }
  void getInput() {
    int tmp;
    for (int i = 0; i < n; i++) {
      cin >> tmp;
      mx = max(mx, tmp);
      mn = min(mn, tmp);
      arr[tmp]++;
    }
  }
  int getBegin() {
    sz = 0;
    for (int i = mn; i <= mx; i++) {
      if (arr[i]) {
        mn = i;
        return i;
      }
    }
    return -1;
  }
  int getNext() {
    for (int i = cur; i <= mx; i++) {
      if (arr[i]) {
        return i;
      }
    }
    return -1;
  }
  int use(int i) {
    sz++;
    cur = max(i, sz);
    if (arr[i] > 0) {
      arr[i]--;
      return 1;
    }
    return -1;
  }
};
int main() {
  int n;
  cin >> n;
  int arr[n];
  machine st(n);
  st.getInput();
  int buf;
  int np = 0;
  while (true) {
    buf = st.getBegin();
    if (buf == -1) {
      break;
    }
    buf = st.use(buf);
    if (buf == -1) {
      break;
    }
    while (true) {
      buf = st.getNext();
      if (buf == -1) {
        break;
      }
      buf = st.use(buf);
      if (buf == -1) {
        break;
      }
    }
    np++;
  }
  cout << np << endl;
}
