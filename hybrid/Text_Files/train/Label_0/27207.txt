#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<math.h>
#include<complex>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<functional>
#include<assert.h>
#include<numeric>
using namespace std;
#define REP(i,m,n) for(int i=(int)(m) ; i < (int) (n) ; ++i )
#define rep(i,n) REP(i,0,n)
typedef long long ll;
typedef pair<int,int> pint;
typedef pair<ll,int> pli;
const int inf=1e9+7;
const ll longinf=1LL<<60 ;
const ll mod=1e9+7 ;

int main(){
    int n;
    cin>>n;
    map<vector<int>,int> mp;
    rep(i,n){
        int w;
        cin>>w;
        vector<int> a={0,1,2};
        rep(j,w){
            int x;
            cin>>x;
            if(x)swap(a[1],a[2]);
            else swap(a[1],a[0]);
        }
        mp[a]++;
    }
    bool ok=false;
    if(mp[{0,1,2}])ok=true;
    if(mp[{0,2,1}]>=2)ok=true;
    if(mp[{1,0,2}]>=2)ok=true;
    if(mp[{2,1,0}]>=2)ok=true;
    if(mp[{1,2,0}]>=3)ok=true;
    if(mp[{2,0,1}]>=3)ok=true;
    if(mp[{1,2,0}]>=1&&mp[{2,0,1}]>=1)ok=true;
    if(mp[{0,2,1}]&&mp[{1,0,2}]&&mp[{1,2,0}])ok=true;
    if(mp[{0,2,1}]&&mp[{1,0,2}]&&mp[{2,0,1}])ok=true;
    if(mp[{2,1,0}]&&mp[{1,0,2}]&&mp[{1,2,0}])ok=true;
    if(mp[{2,1,0}]&&mp[{1,0,2}]&&mp[{2,0,1}])ok=true;
    if(mp[{0,2,1}]&&mp[{2,1,0}]&&mp[{1,2,0}])ok=true;
    if(mp[{0,2,1}]&&mp[{2,1,0}]&&mp[{2,0,1}])ok=true;
    if(ok)cout<<"yes"<<endl;
    else cout<<"no"<<endl;
    return 0;
}
