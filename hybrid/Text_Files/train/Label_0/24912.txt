#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);  cin.tie(NULL);  cout.tie(NULL);
    int n, l, t;    cin >> n >> l >> t; vector<int> vec;
    int say=0;
    for(int i=0;n>i;i++){
        int x, w;   cin >> x >> w;
        if(w==1){
            vec.push_back((t+x)%l); say+=(x+t)/l;
        }
        else{
            say-=(t-x-1+l)/l;   vec.push_back(((x-t)%l+l)%l);
        }
        say=(say+n)%n;
    }
    sort(vec.begin(), vec.end());
    for(int i=say;n>i;i++){
        cout << vec[i] << "\n";
    }
    for(int i=0;say>i;i++){
        cout << vec[i] << "\n";
    }
}
