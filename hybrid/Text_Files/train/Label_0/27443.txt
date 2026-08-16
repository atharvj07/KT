#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k; cin >> n >> k;
    vector<int> a(n);
    for(int i=0; i<n; i++) cin >> a[i];
    int l = 0; int r = 1e9;

    while(r-l > 1){
        int x = (l+r)/2;
        auto f = [&](int x){
            long long now = 0;
            for(int i=0; i<n; i++) now += (a[i]-1)/x;
            return now <= k;
        };
        if(f(x)) r = x; else l = x;
    }
    cout << r << endl;
    return 0;
}