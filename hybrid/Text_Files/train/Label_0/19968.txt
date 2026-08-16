#include <bits/stdc++.h>
using namespace std;

int main(){
    long long h;
    cin >> h;

    long long n = log2(h);
    cout << long(pow(2, n + 1)) - 1 << endl;
}
