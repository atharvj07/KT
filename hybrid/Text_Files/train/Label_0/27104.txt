#include <bits/stdc++.h>
using namespace std;
typedef struct hour {
  int lt, pos;
  hour(int _lt, int _pos) {
    lt = _lt;
    pos = _pos;
  }
  bool operator<(const hour &_hour) const { return lt > _hour.lt; }
};
int main() {
  ifstream inp;
  ofstream outp;
  inp.open("input.txt");
  outp.open("output.txt");
  if (!inp) {
    cout << "file not found";
    return 0;
  }
  int n, h, i, lt;
  vector<hour> vec;
  inp >> n >> h;
  for (i = 0; i < n; i++) {
    inp >> lt;
    vec.push_back(hour(lt, i + 1));
  }
  sort(vec.begin(), vec.end());
  outp << vec[h - 1].lt << "\n";
  for (i = 0; i < h; i++) outp << vec[i].pos << " ";
  inp.close();
  outp.close();
  return 0;
}
