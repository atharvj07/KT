#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main()
{
    stack<int> stk;

    // input
    string str;
    int result;
    cin >> str >> result;

    // calc M pattern
    int mresult = 0;
    int n;
    for (int i = 0; i < (int)str.size(); i++) {
        switch (str[i]) {
        case '*':
            n = stk.top(); stk.pop();
            stk.push(n*(str[i+1]-'0'));
            i++;
            break;
        case '+':
            break;
        default:
            stk.push(str[i]-'0');
            break;
        }
    }
    while (!stk.empty()) {
        int a = stk.top(); stk.pop();
        mresult += a;
    }

    // calc L pattern
    int lresult = str[0]-'0';
    for (int i = 1; i < (int)str.size(); i++) {
        switch (str[i]) {
        case '*':
            lresult *= str[i+1]-'0';
            break;
        case '+':
            lresult += str[i+1]-'0';
            break;
        default:
            break;
        }
    }

    // output
    if (result == mresult) {
        if (result == lresult)
            cout << "U" << endl;
        else
            cout << "M" << endl;
    } else {
        if (result == lresult)
            cout << "L" << endl;
        else
            cout << "I" << endl;
    }

    return 0;
}