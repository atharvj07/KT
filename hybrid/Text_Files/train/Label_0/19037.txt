#include <iostream>
#include <iomanip>
#include <complex>
#include <vector>
#include <algorithm>
#include <cmath>
#include <array>
using namespace std;

const double EPS = 1e-10;
const double INF = 1e12;
#define EQ(n,m) (abs((n)-(m)) < EPS)
#define X real()
#define Y imag()

typedef complex<double> P;
typedef vector<P> VP;
struct L : array<P, 2>{
    L(const P& a, const P& b){ at(0)=a; at(1)=b; }
    L(){}
};

double dot(P a, P b){
    return (conj(a)*b).X;
}
double cross(P a, P b){
    return (conj(a)*b).Y;
}
int ccw(P a, P b, P c){
    b -= a;
    c -= a;
    if(cross(b,c) > EPS) return +1; //ccw
    if(cross(b,c) < -EPS) return -1; //cw
    if(dot(b,c) < -EPS) return +2; //c-a-b
    if(abs(c)-abs(b) > EPS) return -2; //a-b-c
    return 0; //a-c-b
}

bool intersectSS(const L& a, const L& b){
    return ( ccw(a[0],a[1],b[0]) *ccw(a[0],a[1],b[1]) <= 0 ) &&
        ( ccw(b[0],b[1],a[0]) *ccw(b[0],b[1],a[1]) <= 0 );
}
bool intersectSP(const L& s, const P &p){
    return abs(cross(s[0]-p, s[1]-p))<EPS  && dot(s[0]-p, s[1]-p)<EPS;
}

int in_poly(const P &p, const VP &poly){
    int n = poly.size();
    int ret = -1;
    for(int i=0; i<n; i++){
        P a = poly[i]-p;
        P b = poly[(i+1)%n]-p;
        if(a.Y > b.Y) swap(a,b);
        if(intersectSP(L(a,b), P(0,0))) return 0;
        if(a.Y<=0 && b.Y>0 && cross(a,b)<0) ret = -ret;
    }
    return ret;
}

void dfs(int v, vector<bool> &used, vector<vector<int> > &adj){
    if(used[v]) return;
    used[v] = true;
    for(int nv: adj[v]){
        dfs(nv, used, adj);
    }
}

int main(){
    while(1){
        int n;
        cin >> n;
        if(n==0) break;
        
        for(int rep=0; rep<n; rep++){
            int m;
            cin >> m;
            vector<VP> sq(m, VP(4));
            for(int i=0; i<m; i++){
                for(int j=0; j<4; j++){
                    int x,y;
                    cin >> x >> y;
                    sq[i][j] = P(x, y);
                }
                swap(sq[i][0], sq[i][3]);
                swap(sq[i][1], sq[i][2]);
            }
            
            vector<vector<int> > adj(m);
            for(int i=0; i<m; i++){
                for(int j=i+1; j<m; j++){
                    bool overlap = false;
                    for(int k=0; k<4; k++){
                        if(in_poly(sq[i][k], sq[j]) >= 0 || in_poly(sq[j][k], sq[i]) >= 0){
                            overlap = true;
                        }
                        for(int l=0; l<4; l++){
                            if(intersectSS(L(sq[i][k], sq[i][(k+1)%4]), L(sq[j][l], sq[j][(l+1)%4]))){
                                overlap = true;
                            }
                        }
                    }
                    if(overlap){
                        adj[i].push_back(j);
                        adj[j].push_back(i);
                    }
                }
            }
            
            vector<bool> used(m, false);
            int count = 0;
            for(int i=0; i<m; i++){
                if(used[i]) continue;
                dfs(i, used, adj);
                count++;
            }
            cout << count << endl;
        }
    }
    return 0;
}

