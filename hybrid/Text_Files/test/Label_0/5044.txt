#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <climits>
#include <cmath>
#include <complex>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <cstdint>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define MP make_pair
#define PB push_back
#define inf 1000000007
#define rep(i,n) for(int i = 0; i < (int)(n); ++i)
#define all(x) (x).begin(),(x).end()

template<typename A, size_t N, typename T>
void Fill(A (&array)[N], const T &val){
    std::fill( (T*)array, (T*)(array+N), val );
}
 
template<class T> inline bool chmax(T &a, T b){
    if(a<b){
        a = b;
        return true;
    }
    return false;
}

template<class T> inline bool chmin(T &a, T b){
    if(a>b){
        a = b;
        return true;
    }
    return false;
}

vector<vector<int> > g;
bool flag[1010];
int s[1010];
int dfs(int id){
    if(flag[id])return s[id];
    flag[id] = 1;
    set<int> st;
    st.insert(0);
    for(auto x:g[id]){
        st.insert(dfs(x));
    }
    rep(i,1010){
        if(st.count(i)==0){
            s[id] = i;
            return s[id];
        }
    }
}
int res[1010];
int main(){
    int n,m;
    cin >> n >> m;
    vector<int>a(n);
    rep(i,n){
        cin >> a[i];
        a[i]%=2;
    }
    g.resize(n);
    rep(i,m){
        int c,d;
        cin >> c >> d;
        c--;d--;
        g[c].push_back(d);
    }
    rep(i,n){
        dfs(i);       
    }
    int b = 0;
    rep(i,n){
        if(a[i]){
            res[s[i]]++;
        }
    }
    bool f = 0;
    rep(i,1010){
        if(res[i]%2!=0){
            f = 1;
        }
    }
    if(!f){
        cout << 2 << endl;
    }else{
        cout << 1 << endl;
    }
    return 0;
}
