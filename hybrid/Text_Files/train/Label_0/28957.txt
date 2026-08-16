#include<bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b);

int main(){
    long long w, h, c;
    cin >> w >> h >> c;

    long long ky = gcd(w, h);
    long long ans1 = w / ky;
    long long ans2 = h / ky;
    long long ans = ans1 * ans2;
    cout << ans * c << '\n';
        return 0;
}

long long gcd(long long a, long long b){
    while(b != 0){
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}
