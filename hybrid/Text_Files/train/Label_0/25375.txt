#include <bits/stdc++.h>
using namespace std;

long long int N, a;
unordered_map<long long, long long> m;

int main(){
    scanf("%lld", &N);
    for(int i = 0; i < N; ++i){
        scanf("%lld", &a);
        ++m[a];
    }
    a = 0;
    for(auto i : m){
        a += i.second >= i.first ? i.second - i.first : i.second;
    }
    cout << a << endl;
    return 0;
}
