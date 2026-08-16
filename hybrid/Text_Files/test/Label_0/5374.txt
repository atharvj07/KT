#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <memory>
#include <cstring>
#include <cassert>
#include <numeric>
#include <sstream>
#include <complex>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cctype>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#define REP2(i, m, n) for (int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(S) (S).begin(), (S).end()

template <typename T, typename E>
ostream &operator<<(std::ostream &os, const std::pair<T, E> &p){
  return os << "(" << p.first << ", " << p.second << ")";
}

typedef long long ll;

string memo[110][110][2];

string rec(int o, int z, int num){
  if (o == 0 && z == 0) return num == 1 ? "" : "2";
  if (memo[o][z][num] != "") return memo[o][z][num];
  string &res = memo[o][z][num] = "2";
  if (num == 0 && z > 0 && rec(o, z - 1, 1) != "2"){
    res = '0' + rec(o, z - 1, 1);
  }
  if (num == 1){
    if (o > 0 && rec(o - 1, z, 0) != "2") res = min(res, '1' + rec(o - 1, z, 0));
    if (o > 0 && rec(o - 1, z, 1) != "2") res = min(res, '1' + rec(o - 1, z, 1));
    if (z > 0 && rec(o, z - 1, 0) != "2") res = min(res, '0' + rec(o, z - 1, 0));
  }
  return res;
}

int main(){
  ios::sync_with_stdio(false);

  int N;
  cin >> N;
  vector<int> B, O, Z;
  
  REP(i, N) {
    int num;
    cin >> num;
    if (num == 0){
      Z.push_back(num);
    } else if (num == 1){
      O.push_back(num);
    } else {
      B.push_back(num);
    }
  }
  
  sort(ALL(B));
  if (Z.size() % 2 != 0 && O.size() == 0 && B.size() != 0){
    O.push_back(B[0]);
    reverse(ALL(B));
    B.pop_back();
    sort(ALL(B));
  }
  if ((int)B.size() > 1 && B[B.size() - 2] == 2 && B[B.size() - 1] == 3){
    swap(B[B.size() - 2], B[B.size() - 1]);
  }
  
  REP(i, B.size()) cout << B[i] << endl;
  string str = rec(O.size(), Z.size(), 1);
  
  if (str == "2"){
    reverse(ALL(O));
    REP(i, Z.size()) cout << Z[i] << endl;
    REP(i, O.size()) cout << O[i] << endl;
  } else {
    REP(i, str.size()) cout << (str[i] == '0' ? 0 : O[0]) << endl;
  }
  
  return 0;
}