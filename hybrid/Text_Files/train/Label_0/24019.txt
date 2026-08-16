#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <unordered_set>

namespace std{
    #define fi first
    #define se second 
    
    using LL = long long ;
    using PII = pair<LL,LL> ;

    template<>
    struct hash<PII>{
        size_t operator()(const PII& x) const{
            return 10003*hash<LL>()(x.fi)+hash<LL>()(x.se) ;
        }
    };
}

using namespace std ;

int main()
{
    int test ;
    cin >> test ;
    for(int T = 1 ; T <= test ; ++T)
    {
        int n , m ;
        cin >> n >> m ;
        set<int> g ;
        for(int i = 0 , x ; i < n ; ++i)
        {
            cin >> x ;
            g.insert(x) ;
        }
        int ans = 0 ;
        for(int j = 0 , x ; j < m ; ++j)
        {
            cin >> x ;
            if(g.count(x)) ans++ ;
        }
        cout << ans << endl;   
    }
    return 0 ;
}