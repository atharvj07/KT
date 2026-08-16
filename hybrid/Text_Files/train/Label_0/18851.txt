#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i = 0; i < (int)n; i++)
typedef long long ll;

int main(){
    int n;
    cin >> n;
    int p[n];
    rep(i,n) cin >> p[i];
    int a[n+1];
    rep(i,n) a[i+1] = n*(i+1);
    int b[n+1];
    rep(i,n) b[p[i]] = (n*n+1+i)-a[p[i]];
    rep(i,n) cout << a[i+1]  << " ";
    cout << endl;
    rep(i,n) cout << b[i+1] << " ";
    cout << endl;
    return 0;
}