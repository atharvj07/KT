#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n;
        cin>>n;
        vector<long long int> v;
        for (long long int i = 0; i < n; i++)
        {
            long long int k;
            cin>>k;
            v.push_back(k);
        }
        sort(v.begin(), v.end());
        long long int flag = v.size() - 1;
        for (long long int i = 1; i < v.size(); i++)
        {
            if (v[i] != v[i - 1])
            {
                flag = i - 1;
                break;
            }
        }
        cout<<v.size() - 1 - flag<<endl;
    }
    return 0;
}