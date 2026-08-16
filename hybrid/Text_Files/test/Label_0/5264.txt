#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int a[n], x = 0;
    for(int i = 0; i < n; i++)  cin >> a[i], x ^= a[i];
    for(int i = 0; i < n; i++)  cout << (a[i]^x) << " \n"[i==n-1];
    return 0;
}