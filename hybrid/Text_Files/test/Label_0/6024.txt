#include<iostream>
#include<string>

using namespace std;

int main() {
    int t;
    cin>>t;
    while (t--) {
        long long n;
        cin>>n;
        long long temp = n;
        int c = 0, i;
        string s = "1";
        while(temp != 0) {
            temp = temp / 10;
            c++;
        }
        int sum = (c - 1) * 9;
        for(i = 0; i < (c-1); i++){
            s += '1';
        }
        int num = stoi(s);
        int plus = num;
        while(num <= n) {
            sum++;
            num += plus;
        }
        //if(num == n) sum++;
        cout<<sum<<endl;
    }
    return 0;
}