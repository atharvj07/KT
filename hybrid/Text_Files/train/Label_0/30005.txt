#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int,int> PI;
const double EPS=1e-8;
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SZ(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) a.rbegin(),a.rend()
#define FLL(a,b) memset((a),b,sizeof(a))
#define CLR(a) FLL(a,0)
#define declare(a,it) __typeof(a) it=(a)
#define FOR(it,a) for(declare(a.begin(),it);it!=a.end();++it)
#define FORR(it,a) for(declare(a.rbegin(),it);it!=a.rend();++it)
template<class T,class U> ostream& operator<< (ostream& o, const pair<T,U>& v){return o << "(" << v.F << ", " << v.S << ")";}
template<class T> ostream& operator<< (ostream& o, const vector<T>& v){o << "{";rep(i,SZ(v)) o << (i?", ":"") << v[i];return o << "}";}
int dx[]={0,1,0,-1,1,1,-1,-1};
int dy[]={1,0,-1,0,-1,1,1,-1};
int s2i(string& a){stringstream ss(a);int r;ss>>r;return r;}
int geti(){int n;scanf("%d", &n);return n;}

int x[100],y[100];


int main(int argc, char *argv[])
{
  int n;
  cin >> n;

  double sumx = 0;
  double sumy = 0;
  for(int i = 0; i < n; ++i){
    cin >> x[i] >> y[i];
    sumx += x[i];
    sumy += y[i];
  }
  sumx /= n;
  sumy /= n;
  
  bool ok = true;
  for(int i = 0; i < n; ++i){
    double ax = x[(i+1)%n] - x[i];
    double ay = y[(i+1)%n] - y[i];
    double bx = x[(i+1+n/2)%n] - x[(i+n/2)%n];
    double by = y[(i+1+n/2)%n] - y[(i+n/2)%n];
    ok &= abs(ax*by - bx*ay) < EPS;
    ok &= abs(ax*ax+ay*ay-(bx*bx + by*by)) < EPS;
  }
  
  if(ok && ~n%2) printf("%.10f %.10f\n", sumx, sumy);
  else cout << "NA" << endl;
  
  return 0;
}