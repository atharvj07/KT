#include <bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin >> N;
    __int128_t M = 1, INF = int64_t(1e18) + 1;
    while(N--){
        int64_t a;
        cin >> a;
        M = min(M*a, INF);
    }
    if(M == INF) M = -1;
    cout << int64_t(M) << endl;
    return 0;
}