#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const double pi=3.141592653589793;
typedef unsigned long long ull;
typedef long double ldouble;
const ll INF=1e18;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }

// 拡張ユークリッドの互除法
// ax + by = gcd(a, b) となる gcd(a, b) を返す。
// x, yの値はint型の変数を入れるとその関数に格納されている値が変更される。
ll exgcd(int a, int b, int& x, int& y){
    int d = a;
    if( b!= 0){
        d = exgcd(b, a%b, y, x);
        y -= (a / b) * x;
    } else {
        x = 1; y = 0;
    }
    return d;
}

int main(){
    int a, b, x, y;
    cin >> a >> b;
    exgcd(a, b, x, y);
    cout << x << " " << y << endl;
}
