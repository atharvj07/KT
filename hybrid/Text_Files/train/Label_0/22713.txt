#include <iostream>

using namespace std;

typedef long long ll;

void extgcd(ll a, ll b, ll& d, ll& x, ll& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        d = a;
    }
    
    else {
        extgcd(b, a % b, d, y, x);
        y -= x * (a / b);
    }  
}

int main() {
    ll a, b;
    cin >> a >> b;
    ll d, x, y;
    extgcd(a, b, d, x, y);
    cout << x <<" " << y << endl;
    return 0;
}