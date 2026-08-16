#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define all(v) (v).begin(),(v).end()
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define fi first
#define se second
template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

struct T{
    int l,r,x;
    T(int a,int b,int c):l(a),r(b),x(c){}
    bool operator<(const T &t)const{
        if(t.l!=l)return l<t.l;
        if(t.r!=r)return r<t.r;
        return x<t.x;
    }
};

signed main(){
    int N,Q;
    scanf("%lld%lld",&N,&Q);
    set<T>s;
    s.insert(T(0,N,0));
    s.insert(T(N,1001001001,1001001001));
    while(Q--){
        int a,b;
        scanf("%lld%lld",&a,&b);
        auto it=s.lower_bound(T(a,-1,-1));
        if(it->l!=a){
            it--;
            int l=it->l,r=it->r,x=it->x;
            s.erase(it);
            s.insert(T(l,a,x));
            s.insert(T(a,r,x));
        }

        while(b){
            it=s.lower_bound(T(a,-1,-1));
            it--;
            bool isend=false;
            if(it==s.begin())isend=true;
            else{
                auto jt=it;
                jt--;
                if((jt->x-it->x)*(it->r-it->l)>b)isend=true;
            }
            int l=it->l,r=it->r,x=it->x;
            if(isend){
                s.erase(it);
                x+=b/(it->r-it->l);
                b%=(it->r-it->l);
                if(b){
                    s.insert(T(l,l+b,x+1));
                    s.insert(T(l+b,r,x));
                }
                else{
                    s.insert(T(l,r,x));
                }
                b=0;
            }
            else{
                auto jt=it;
                jt--;
                b-=(jt->x-it->x)*(it->r-it->l);
                l=jt->l;
                x=jt->x;
                s.erase(it);s.erase(jt);
                s.insert(T(l,r,x));
            }
        }
    }

    each(it,s){
        if(it->l==N)break;
        rep(i,it->r-it->l)printf("%lld\n",it->x);
    }
    return 0;
}
