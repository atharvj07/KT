#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    string s;cin>>s;
    int an=0,cur=0;
    for(char x:s){
        if(x=='R') cur++;
        else cur=0;
        an=max(an,cur);
    }cout<<an<<"\n";
}

