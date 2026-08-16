#include <bits/stdc++.h>
using namespace std;

#define M (long)1e9+7

int main(){
    int n, a, ans = 1;cin >> n;
    vector<int> cnt(n,0);//cnt[i] := 人数の差の絶対値がi人といった人の数
    for(int i=0;i<n;i++){
        cin >> a;
        if(a >= n){goto err;}
        cnt[a]++;
    }

    for (int i = n-1; i >= 1; i-=2) {
        if(cnt[i] != 2) goto err;
        ans *= 2;
        ans %= M;
    }

    cout << ans  << endl;
    return 0;

    err:
        cout << 0 << endl;

}