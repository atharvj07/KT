#include <bits/stdc++.h>
using namespace std;
int main(){
    int A,B,C,K;
    cin>>A>>B>>C>>K;
    int M=max({A,B,C});
    cout<<pow(2,K)*M-M+A+B+C<<endl;
}