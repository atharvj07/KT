#include <queue>
#include<iostream>
using namespace std;
int n,a,s[2];
priority_queue<int> q;
int main(){
    cin>>n;
    for(int i=1;i<=n;i++)cin>>a,q.push(a);
    for(int i=1;i<=n;i++){
        a=q.top();
        q.pop();
        s[i%2]+=a;
    }
    cout<<s[1]-s[0];
    return 0;
}