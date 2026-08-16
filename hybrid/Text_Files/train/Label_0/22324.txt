#include <bits/stdc++.h> // only for GCC

using namespace std;

int main(){
    double a, l, x;
    while(cin >> a >> l >> x){
        double b = sqrt(abs(pow(l, 2)-pow(a/2, 2)));
        double ans = a*b/2;
        double d = sqrt(pow((l+x)/2, 2)-pow(l/2, 2));
        ans += l*d;
        printf("%lf\n", ans);
    }
}