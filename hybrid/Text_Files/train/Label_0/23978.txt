#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
using namespace std;

#define DEBUG(x) cerr << "L" << __LINE__ << " " << #x << " = " << x << endl

const int MAX_N = 300000;

const int INF = 1e9;
const int sqrtN = 500;

int data[(MAX_N + sqrtN - 1) / sqrtN * sqrtN];
int add[(MAX_N + sqrtN - 1) / sqrtN];
int min1[(MAX_N + sqrtN - 1) / sqrtN];

struct SegmentArray {
  const int B;
  SegmentArray(int n) : B((n + sqrtN - 1) / sqrtN) { }
  void update(int a, int b, int v) {
    for(int k = 0; k < B; ++k) {
      int l = k * sqrtN, r = (k + 1) * sqrtN;
      if(r <= a || b <= l) continue;
      if(a <= l && r <= b) {
        add[k] += v;
        continue;
      }
      min1[k] = INF;
      int st = std::max(a, l), en = std::min(b, r);
      for(int i = k * sqrtN; i < (k + 1) * sqrtN; ++i) {
        if(st <= i && i < en) data[i] += v;
        if(min1[k] > data[i]) min1[k] = data[i];
      }
    }
  }
  int search(int p) {
    int a = 0;
    int b = p + 1;
    for(int k = B - 1; k >= 0; k--) {
      int l = k * sqrtN, r = (k + 1) * sqrtN;
      if(r <= a || b <= l) continue;
      if(a <= l && r <= b) {
        if(add[k] + min1[k] < 2) {
          for(int j = sqrtN - 1; j >= 0; --j) {
            if(add[k] + data[k * sqrtN + j] < 2) {
              return k * sqrtN + j + 1;
            }
          }
        }
      }
      else {
        int st = std::max(a, l), en = std::min(b, r);
        for(int i = en - 1; i >= st; --i) {
          if(add[k] + data[i] < 2) {
            return i + 1;
          }
        }
      }
    }
  }
};

char S[300001];

int main() {
  int N, Q; scanf("%d%d", &N, &Q);
  scanf("%s", S);
  SegmentArray seg1(N);
  set<int> seg2;
  for(int i = 0; i < N; ++i) { 
    seg1.update(i, N, (S[i] == '(' ? 1 : -1));
    if(S[i] == ')') seg2.insert(i);
  }
  for(int q = 0; q < Q; ++q) {
    int p; scanf("%d", &p);
    --p;
    if(S[p] == '(') {
      S[p] = ')';
      seg2.insert(p);
      seg1.update(p, N, -2);
      int np = *seg2.begin();
      S[np] = '(';
      seg2.erase(np);
      seg1.update(np, N, +2);
      printf("%d\n", np + 1);
    }
    else {
      S[p] = '(';
      seg2.erase(p);
      seg1.update(p, N, +2);
      int np = seg1.search(p);
      S[np] = ')';
      seg2.insert(np);
      seg1.update(np, N, -2);
      printf("%d\n", np + 1);
    }
  }
}