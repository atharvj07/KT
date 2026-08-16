#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main(){
    int w, h, n, x, y, a;
    int w0=0, h0=0;
    cin>>w>>h>>n;
    for (int i=0; i<n; i++){
        cin>>x>>y>>a;
        if (a == 1 && w0 < x) w0 = x;
        if (a == 2 && w > x) w = x;
        if (a == 3 && h0 < y) h0 = y;
        if (a == 4 && h > y) h = y;
    }
    if ((w<w0)|(h<h0)) cout<<0<<endl;
    else cout<<(w-w0)*(h-h0)<<endl;
}
