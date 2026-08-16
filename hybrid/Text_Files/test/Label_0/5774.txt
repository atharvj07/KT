#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll a[300005] , spare = 0;
int main(){
    ll n , q , i , j;
    cin >> n >> q;
    set < pair < ll , ll > > cur;
    for(i = 1;i<=n;i++){
        cin >> a[i];
        cur.insert( { i , a[i] } );
    }
    while(q--){
        ll x , gone = 0;
        cin >> x;
        pair < ll , ll > ind;
        for(auto i : cur){
            gone++;
            if (i.second == x){
                ind = i;
                break;
            }
        }
        cout << gone << "\n";
        cur.erase(ind);
        cur.insert({ spare , ind.second }) ;
        spare--;
    }
    return 0;
}
