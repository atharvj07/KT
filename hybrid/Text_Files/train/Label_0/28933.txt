#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long int lli;

int main(){
    int n,q;
    cin >> n >> q;
    for(int i=0; i<q; i++){
        lli x,y;
        cin >> x >> y;
        if(n==1){
            cout << min(x, y) << endl;
            continue;
        }
        x--;
        y--;
        while(x != y){
            if(x < y) swap(x, y);
            x = (x-1)/n;
        }
        cout << x+1 << endl;
    }
    return 0;
}