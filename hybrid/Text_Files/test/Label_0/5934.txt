#include<bits/stdc++.h>

using namespace std;

int main()
{
    map <string,int> m;
    int q;
    cin>>q;
    while(q--)
    {
        int a;
        cin>>a;
        if(a==0)
        {
            string key;
            long long x;
            cin>>key>>x;
            m[key]=x;
        }
        else if(a==1)
        {
            string key;
            cin>>key;
            if(m.count(key))
                cout<<m[key]<<endl;
            else
                cout<<"0"<<endl;
        }
        else if(a==2)
        {
            string key;
            cin>>key;
            m.erase(key);
        }
        else
        {
            string l,r;
            cin>>l>>r;
            auto p=m.lower_bound(l);
            while(p!=m.end()&&p->first<=r)
            {
                cout<<p->first<<" "<<p->second<<endl;
                p++;
            }
        }
    }
    return 0;
}

