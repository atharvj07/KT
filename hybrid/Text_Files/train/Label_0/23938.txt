#include <iostream>
using namespace std;

int main(){
    int a,b,n;
    cin >> a>> b >> n;
    int ans=0;
    for(int i=0; i<n; i++){
        int s,f;
        cin >> s >> f;
        if((a<s && s<b) || (s<=a && a<f)){
            ans=1;
        }
    }
    cout << ans << endl;
    return 0;
}

