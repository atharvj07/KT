#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
typedef pair<LL, LL> PLL;

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define FF first
#define SS second
template<class S, class T>
istream& operator>>(istream& is, pair<S,T>& p){
  return is >> p.FF >> p.SS;
}

const double EPS = 1e-10;
const double PI  = acos(-1.0);
const LL MOD = 1e9+7;

typedef vector<LL> Col;
typedef vector<Col> Matrix;
Matrix mul(const Matrix& A, const Matrix& B){
  const int R = A.size(), C = B[0].size(), sz = B.size();
  Matrix AB(R, Col(C));

  for(int i=0;i<R;++i)
    for(int j=0;j<C;++j)
      for(int k=0;k<sz;++k)
		(AB[i][j] += A[i][k] * B[k][j]) %= MOD;

  return AB;
}

// O(N^3 lgN)
Matrix powA(const Matrix& A, int n){
  const int N = A.size();
  Matrix p(N, Col(N, 0)), w = A;
  for(int i=0;i<N;++i) p[i][i] = 1;

  while(n>0){
	if(n&1)
	  p = mul(p, w);
	w = mul(w, w);
	n >>= 1;
  }

  return p;
}

void dump(const Matrix& A){
  REP(i,SZ(A)){
	REP(j,SZ(A[i]))
	  cout << A[i][j] << (j%5==4?" | ":" ");
	cout << endl;
	if(i%5==4)cout<<string(SZ(A)+20,'-')<<endl;
  }
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int N, K, C, T; cin >> N >> K >> C >> T;
  --C;
  VI as(K), bs(K), ts(K);
  Matrix A(5*N, Col(5*N));
  REP(i,N) REP(t,4)
	A[5*i+t][5*i+t+1]++;

  REP(i,K){
	cin >> as[i] >> bs[i] >> ts[i];
	--as[i];
	--ts[i];
	for(int k=0;k<bs[i];++k)
	  A[k*5+ts[i]][(as[i]+k)*5]++;
	for(int k=0;k<as[i];++k)
	  A[(bs[i]+k)*5+ts[i]][k*5]++;
	for(int k=as[i]+bs[i];k<N;++k)
	  A[5*k+ts[i]][5*k]++;
  }

  A = powA(A, T);
  cout << A[0][5*C] << endl;
  
  return 0;
}