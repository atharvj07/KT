#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    string s;
    cin >> n >> s;
    int r=0;
    for(char c : s)
        if(c=='R')
            r++;
    cout << ((r>n/2)?"Yes":"No") << endl;
}