#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <iomanip>
#include <cstdio>

using namespace std;
typedef  long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
#define  MP make_pair
#define  PB push_back
#define inf  1000000007
#define rep(i,n) for(int i=0;i<(int)(n);++i)

template<typename A, size_t N, typename T>
void Fill(A (&array)[N], const T &val){
    std::fill( (T*)array, (T*)(array+N), val );
}
int main(){
    int n;
    while(cin >> n &&n!=0){
        vector<vector<pair<ll,int> > > g(n);
        vector<int> p(n);
        vector<ll>d(n);
        for(int i=1;i<n;i++){
            cin >> p[i];
            p[i]--;
        }
        ll ans=0;
        for(int i=1;i<n;i++){
            cin >> d[i];
            ans+=d[i];
        }
        ans *=3;
        for(int i=1;i<n;i++){
            g[i].PB(MP(d[i],p[i]));
            g[p[i]].PB(MP(d[i],i));
        }
        ll s = 0;
        vector<bool>flag(n);
        for(int i=0;i<n;i++){
            if(g[i].size()==1){
                s += g[i][0].first;
                flag[i] = 1;
            }
        }
        priority_queue<pair<ll,int>,vector<pair<ll,int> >,greater<pair<ll,int> >  >pq;
        for(int i=0;i<n;i++){
            if(g[i].size()!=1){
                pq.push(MP((ll)0,i));
                flag[i] = 1;
                break;
            }
        }
        int l=-1;
        while(!pq.empty()){
            auto a = pq.top();
            l = a.second;
            pq.pop();
            for(auto x:g[l]){
                if(!flag[x.second]){
                    flag[x.second] = 1;
                    pq.push(MP(a.first+x.first,x.second));
                }
            }
        }
        rep(i,n)if(g[i].size()!=1)flag[i]=0;
        if(l!=-1)pq.push(MP((ll)0,l)),flag[l]=1;
        ll r = 0;
        while(!pq.empty()){
            auto a = pq.top();
            r = a.first;
            pq.pop();
            for(auto x:g[a.second]){
                if(!flag[x.second]){
                    flag[x.second] = 1;
                    pq.push(MP(a.first+x.first,x.second));
                }
            }
        }
        ans -= 2*s+r;
        cout <<ans << endl;
    }
    return 0;
}
