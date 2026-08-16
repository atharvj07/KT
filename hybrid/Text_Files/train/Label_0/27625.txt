#include <bits/stdc++.h>
#define For(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define rFor(i, a, b) for(int (i)=(a)-1; (i)>=(b); (i)--)
#define rep(i, n) For((i), 0, (n))
#define rrep(i, n) rFor((i), (n), 0)
using namespace std;
typedef long long lint;

bool isprime(int i){
    for(int j=2; j*j<=i; ++j){
        if(i % j == 0) return false;
    }
    return true;
}

lint gcd(lint p, lint q){
    if(p < 0) p = -p;
    if(q < 0) q = -q;
    if(p < q) swap(p, q);
    while(q){
        lint r = p % q;
        p = q;
        q = r;
    }
    return p;
}

int main(){
    int n; cin >> n;
    vector<lint> a(n+1); rep(i, n+1) cin >> a[n-i];
    vector<lint> prime;
    vector<lint> p;
    if(n >= 2) prime.push_back(2);
    for(int i=3; i<=n; i+=2)if(isprime(i)) prime.push_back(i);
    lint g = a[0];
    rep(i, n) g = gcd(g, a[i+1]);
    for(int i=2; i*i<=g; ++i){
        if(g % i == 0){
            while(g % i == 0) g /= i;
            p.push_back(i);
        }
    }
    if(g > 1) p.push_back(g);
    rep(i, prime.size()){
        vector<lint> b(n+1); rep(j, n+1) b[j] = a[j];
        rFor(j, n+1, prime[i]){
            b[j-prime[i]+1] += b[j];
            b[j] = 0;
        }
        bool flag = true;
        rep(j, n+1)if(b[j] % prime[i] != 0){
            flag = false;
            break;
        }
        if(!flag) continue;
        p.push_back(prime[i]);
    }
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());
    rep(i, p.size()) cout << p[i] << endl;
}