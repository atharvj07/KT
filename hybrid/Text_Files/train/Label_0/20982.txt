#include <bits/stdc++.h>
#define ll long long
#define INF 1000000005
#define MOD 1000000007
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;--i)
#define srep(i,s,t) for(int i=(int)(s);i<(int)(t);++i)
#define each(a,b) for(auto& (a): (b))
#define all(v) (v).begin(),(v).end()
#define len(v) (int)(v).size()
#define zip(v) sort(all(v)),v.erase(unique(all(v)),v.end())
#define cmx(x,y) x=max(x,y)
#define cmn(x,y) x=min(x,y)
#define fi first
#define se second
#define pb push_back
#define show(x) cout<<#x<<" = "<<(x)<<endl
#define spair(p) cout<<#p<<": "<<p.fi<<" "<<p.se<<endl
#define sar(a,n) cout<<#a<<":";rep(pachico,n)cout<<" "<<a[pachico];cout<<endl
#define svec(v) cout<<#v<<":";rep(pachico,v.size())cout<<" "<<v[pachico];cout<<endl
#define svecp(v) cout<<#v<<":";each(pachico,v)cout<<" {"<<pachico.first<<":"<<pachico.second<<"}";cout<<endl
#define sset(s) cout<<#s<<":";each(pachico,s)cout<<" "<<pachico;cout<<endl
#define smap(m) cout<<#m<<":";each(pachico,m)cout<<" {"<<pachico.first<<":"<<pachico.second<<"}";cout<<endl

using namespace std;

typedef pair<int,int> P;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<P> vp;
typedef vector<string> vs;

const int MAX_N = 101;

struct edge
{
    int to,cost;
};

vector<edge> G[MAX_N];
int d[MAX_N];

// max c * x s.t. A*x <= b, x >= 0
class Simplex {
private:
    using Arr = vector<double>;
    using Mat = vector<vector<double> >;
    int* index;
    double** a;
    int row, column, L;

    void Set(const Mat& A, const Arr& b, const Arr& c){
        infinity = none = false;
        row = A.size(),column = A[0].size() + 1;
        index = new int[row + column];
        int i, j;
        for(i = 0; i < row + column; i++){
            index[i] = i;
        }
        L = row;
        a = new double*[row + 2];
        for(i = 0; i < row + 2; i++){
            a[i] = new double[column + 4];
        }
        for(i = 0; i < row; i++){
            for(j = 0; j < column - 1; j++){
                a[i][j] = -A[i][j];
            }
            a[i][column-1] = 1;
    	    a[i][column] = b[i];
    	    if(a[L][column] > a[i][column]) L = i;
        }
        for(j = 0; j < column - 1; j++){
            a[row][j] = c[j];
        }
    	a[row+1][column-1] = -1;
    }

    void solve(){
        int E, i, j;
        for(E = column - 1;;){
    	    if(L < row){
                swap(index[E], index[L + column]);
        		a[L][E] = 1 / a[L][E];
                for(j = 0; j < column + 1; j++){
                    if(j != E) a[L][j] *= -a[L][E];
                }
        		for(i = 0; i < row + 2; i++){
                    if(abs(a[i][E]) < EPS || i == L) continue;
                    for(j = 0; j < column + 1; j += 4){
                        if(j != E) a[i][j] += a[i][E] * a[L][j];
                        if(j+1 != E) a[i][j+1] += a[i][E] * a[L][j+1];
                        if(j+2 != E) a[i][j+2] += a[i][E] * a[L][j+2];
                        if(j+3 != E) a[i][j+3] += a[i][E] * a[L][j+3];
                    }
                    a[i][E] = a[i][E] * a[L][E];
        		}
    	    }
    	    E = -1;
            double pre = EPS, pre2 = EPS;
    	    for(j = 0; j < column; j++){
                if(E < 0){
                    if(abs(a[row + 1][j]) < EPS && a[row][j] > pre2) E = j, pre2 = a[row][j];
                    else if(a[row + 1][j] > pre) E = j, pre = a[row + 1][j];
                }
            }
    	    if(E < 0) break;
            L = -1;
            for(i = 0; i < row; i++){
                if(a[i][E] < -EPS){
                    if(L < 0 || a[L][column] / a[L][E] - a[i][column] / a[i][E] < EPS) L = i;
                }
            }
            if(L < 0){
                infinity = true;
                return;
            }
    	}
    	if(a[row + 1][column] < -EPS){
    	    none = true;
    	    return;
    	}
    	x.assign(column - 1, 0);
        for(i = 0; i < row; i++){
            if(index[column + i] < column - 1) x[index[column + i]] = a[i][column];
        }
    	ans = a[row][column];
    }
public:
    bool infinity, none;
    double ans;
    Arr x;
    Simplex(const Mat& A, const Arr& b, const Arr& c){
        Set(A,b,c);
        solve();
    }
};

struct eda{
    int from,to,cost;
};

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,m;
    cin >> n >> m;
    vector<eda> es(m);
    rep(i,m){
        int x,y,s;
        cin >> x >> y >> s;
        G[x].pb((edge){y,s});
        es[i] = (eda){x,y,s};
    }
    rrep(i,n){
        each(e,G[i]){
            cmx(d[i],d[e.to]+e.cost);
        }
    }
    int mx = d[0];
    vd b(m+1,0.0), c(n+m,0.0);
    rep(i,m){
        c[n+i] = 1.0;
    }
    vector<vd> A(m+1,vd(n+m,0.0));
    rep(i,m){
        A[i][es[i].from] = 1, A[i][es[i].to] = -1, A[i][n+i] = 1;
        b[i] = -es[i].cost;
    }
    A[m][n-1] = 1, b[m] = mx;
    Simplex sp(A,b,c);
    int ans = round(sp.ans);
    cout << ans << "\n";
    return 0;
}

