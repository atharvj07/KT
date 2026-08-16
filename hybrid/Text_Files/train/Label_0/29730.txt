#include <bits/stdc++.h>
#define REP(i,n) for(int i=0; i<(int)(n); ++i)

using namespace std;

long long module(long long x, long long m){
    while(x >= m) x -= m;
    return x;
}

long long mul(long long a, long long b, long long mod){
    if(b == 0) return 0;
    long long res = mul(module(a + a, mod), b / 2, mod);
    if(b & 1) res = module(res + a, mod);
    return res;
}

long long pow(long long a, long long b, long long mod){
    if(b == 0) return 1;
    long long res = pow(mul(a, a, mod), b / 2, mod);
    if(b & 1) res = mul(res, a, mod);
    return res;
}

long long inv(long long a, long long mod){
    return pow(a, mod - 2, mod);
}


int main(){
    int N;
    const long long P = 10000000019;
    while(cin >> N){
        long long X = 0;
        for(int i = 0; i < N; i++){
            int ope;
            long long Y;
            cin >> ope >> Y;
            if(ope == 1){
                X = (X + Y + P) % P;
            }else if(ope == 2){
                X = (X - Y + P) % P;
            }else if(ope == 3){
                X = mul(X, abs(Y), P);
                if(Y < 0) {
                    X = (-X + P) % P;
                }
            }else{
                X = mul(X, inv(abs(Y), P), P);
                if(Y < 0) {
                    X = (-X + P) % P;
                }
            }
            //cout << X << endl;
        }
        if(X > INT_MAX){
            X = X - P;
        }
        cout << X << endl;
    }
    return 0;
}