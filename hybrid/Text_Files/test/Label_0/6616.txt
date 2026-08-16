#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>
using namespace std;
int abs(int a){
    return a<0?-a:a;
}
int main(){
    int d,n,m;
    while(cin>>d,d){
        cin>>n>>m;
        vector<int>s;
        for(int i=0;i<n-1;i++){
            int a;
            cin>>a;
            s.push_back(a);
        }
        s.push_back(0);
        sort(s.begin(),s.end());
        for(int i=0;i<s.size();i++){
            if(s[i]>=d/2)break;
            s.push_back(s[i]+d);
        }
        s.push_back(1e9+1);
        int sum=0;
        while(m--){
            int p;
            cin>>p;
            vector<int>::iterator ite;
            ite=upper_bound(s.begin(),s.end(),p);
            sum+=min(abs(p-(*(ite-1))),abs(p-(*ite)));
        }
        cout<<sum<<endl;
    }
}