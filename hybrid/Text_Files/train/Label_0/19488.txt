#include<bits/stdc++.h>
using namespace std;

#define int long long

typedef long long ll;
typedef pair<int,int>pint;
typedef vector<int>vint;
typedef vector<pint>vpint;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(v) (v).begin(),(v).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
template<class T,class U>void chmin(T &t,U f){if(t>f)t=f;}
template<class T,class U>void chmax(T &t,U f){if(t<f)t=f;}

int gcd(int a,int b){
    return b?gcd(b,a%b):a;
}

struct data{
    int vx,vy,x0,y0;
    data(int a,int b,int c,int d){
        int g=gcd(abs(a),abs(b));
        a/=g;b/=g;
        if(a<0)a*=-1,b*=-1;
        else if(a==0&&b<0)b*=-1;
        vx=a;vy=b;x0=c;y0=d;
    }
    bool operator==(const data &d){
        if(vx!=d.vx||vy!=d.vy)return false;
        int xx=x0-d.x0,yy=y0-d.y0;
        if(vx==0)return xx==0;
        if(vy==0)return yy==0;
        return xx%vx==0&&yy%vy==0&&xx/vx==yy/vy;
    }
};

int N;
int x[10],y[10];

int table[10][10];

int p[]={1,2,3,4,5,6,7,8};
vint lis;
bool f[100];
int ans=1145141919;

void dfs(int n,int c){
    if(n==N-1){
        chmin(ans,c);
        return;
    }

    int idx=p[n];
    rep(i,lis.size()){
        int tmp=table[lis[i]][idx];
        lis.pb(idx);
        if(f[tmp])dfs(n+1,c);
        else{
            f[tmp]=1;
            dfs(n+1,c+1);
            f[tmp]=0;
        }
        lis.pop_back();
    }
}

signed main(){
    cin>>N;
    rep(i,N)cin>>x[i]>>y[i],x[i]*=2,y[i]*=2;

    vector<data>vec;
    rep(i,N)rep(j,N)if(i!=j){
        data d(y[j]-y[i],x[i]-x[j],(x[i]+x[j])/2,(y[i]+y[j])/2);
        int t=-1;
        rep(k,vec.size())if(vec[k]==d)t=k;
        if(t==-1){
            table[i][j]=vec.size();
            vec.pb(d);
        }
        else{
            table[i][j]=t;
        }
    }

    do{
        lis.clear();
        lis.pb(0);
        dfs(0,0);
    }while(next_permutation(p,p+N-1));

    cout<<ans<<endl;

    return 0;
}