#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;

int main(){
  int N, Q;
  cin >> N >> Q;
  vector<int> A(Q), B(Q);
  REP(i,Q) {
    cin >> A[i] >> B[i]; --A[i]; --B[i];
  }

  set<int> st;
  vector<int> cup(N);
  iota(ALL(cup), 0);
  int ball = 0;
  st.insert(0);
  st.insert(cup[ball + 1]);
  REP(i,Q) {
    swap(cup[A[i]], cup[B[i]]);
    if(A[i] == ball) ball = B[i];
    else if(B[i] == ball) ball = A[i];
    if(ball - 1 >= 0) st.insert(cup[ball - 1]);
    if(ball + 1 < N) st.insert(cup[ball + 1]);
  }
  cout << st.size() << endl;
  return 0;
}

