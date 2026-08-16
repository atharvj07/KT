#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;
typedef vector<pair<int,map<string,int> > > express;

string processSpace(const string &str){
    string res="";
    bool sp=false;
    for(int i = 0; i < str.size(); i++){
        if(str[i]!=' '){
            if(!sp&&res.size()!=0&&(res[res.size()-1]>='0'&&res[res.size()-1]<='9')
                &&(str[i]>='0'&&str[i]<='9')){

            }
            else if(res.size()!=0&&((res[res.size()-1]>='0'&&res[res.size()-1]<='9')
                ||(res[res.size()-1]>='a'&&res[res.size()-1]<='z'))
                &&((str[i]>='0'&&str[i]<='9')||(str[i]>='a'&&str[i]<='z'))){
                    res+='*';
            }
            else if(res.size()!=0&&((res[res.size()-1]>='0'&&res[res.size()-1]<='9')
                ||(res[res.size()-1]>='a'&&res[res.size()-1]<='z'))
                &&(str[i]=='(')){
                    res+='*';
            }
            else if(res.size()!=0&&(res[res.size()-1]==')')
                &&((str[i]>='0'&&str[i]<='9')||(str[i]>='a'&&str[i]<='z'))){
                    res+='*';
            }
            else if(res.size()!=0&&res[res.size()-1]==')'&&str[i]=='(')
                res+='*';
            res+=str[i];
            sp=false;
        }
        else{
            sp=true;
        }
    }
    return res;
}

express analysis(string str){
    express res;
    if(str.size()==0)return res;
    bool allNum=true;
    for(int i = 0; i < str.size(); i++){
        if(!(str[i]>='0'&&str[i]<='9')){
            allNum=false;
            break;
        }
    }
    if(allNum){
        int num=atoi(str.c_str());
        if(num!=0)
            res.push_back(make_pair(num,map<string,int>()));
        return res;
    }
    if(str.size()==1&&str[0]>='a'&&str[0]<='z'){
        map<string,int> msi;
        string tmp;
        tmp+=(str[0]);
        msi[tmp]=1;
        res.push_back(make_pair(1,msi));
        return res;
    }
    if(str[0]=='('){
        int cnt=0;
        bool no=false;
        for(int i = 1; i < str.size()-1; i++){
            if(str[i]==')')
                cnt--;
            else if(str[i]=='(')
                cnt++;
            if(cnt<0){
                no=true;
                break;
            }
        }
        if(!no)
            return analysis(str.substr(1,str.size()-2));
    }
    int cnt=0;
    for(int i = str.size()-1; i >= 0; i--){
        if(str[i]==')')
            cnt++;
        else if(str[i]=='(')
            cnt--;
        else if(cnt==0){
            if(str[i]=='+'||str[i]=='-'){
                express left=analysis(str.substr(0,i));
                express right=analysis(str.substr(i+1));
                for(int j = 0; j < left.size(); j++){
                    bool no=true;
                    for(int k = 0; k < res.size(); k++){
                        if(res[k].second==left[j].second){
                            int co=0;
                            if(str[i]=='+')
                                co=res[k].first+left[j].first;
                            else if(str[i]=='-')
                                co=res[k].first-left[j].first;
                            if(co==0){
                                res.erase(res.begin()+k);
                                no=false;
                                break;
                            }
                            else{
                                res[k].first=co;
                                no=false;
                                break;
                            }
                        }
                    }
                    if(no)
                        res.push_back(left[j]);
                }
                for(int j = 0; j < right.size(); j++){
                    bool no=true;
                    for(int k = 0; k < res.size(); k++){
                        if(res[k].second==right[j].second){
                            int co=0;
                            if(str[i]=='+')
                                co=res[k].first+right[j].first;
                            else if(str[i]=='-')
                                co=res[k].first-right[j].first;
                            if(co==0){
                                res.erase(res.begin()+k);
                                no=false;
                                break;
                            }
                            else{
                                res[k].first=co;
                                no=false;
                                break;
                            }
                        }
                    }
                    if(no){
                        if(str[i]=='-')right[j].first*=-1;
                        res.push_back(right[j]);
                    }
                }
                return res;
            }
        }
    }
    cnt=0;
    for(int i = str.size()-1; i >= 0; i--){
        if(str[i]==')')
            cnt++;
        else if(str[i]=='(')
            cnt--;
        else if(cnt==0){
            if(str[i]=='*'){
                express left=analysis(str.substr(0,i));
                express right=analysis(str.substr(i+1));
                for(int k = 0; k < left.size(); k++){
                    for(int j = 0; j < right.size(); j++){
                        int co=left[k].first*right[j].first;
                        map<string,int> literals=left[k].second;
                        for(map<string,int>::iterator it=right[j].second.begin();it!=right[j].second.end();it++)
                            literals[it->first]+=it->second;
                        pair<int,map<string,int> > p=make_pair(co,literals);
                        bool no=false;
                        for(int l = 0; l < res.size(); l++){
                            if(p.second==res[l].second){
                                int coSum=p.first+res[l].first;
                                if(coSum==0){
                                    res.erase(res.begin()+l);
                                    no=true;
                                    break;
                                }
                                else{
                                    res[l].first=coSum;
                                    no=true;
                                    break;
                                }
                            }
                        }
                        if(!no)
                            res.push_back(p);
                    }
                }
                return res;
            }
        }
    }
    cnt=0;
    for(int i = str.size()-1; i >= 0; i--){
        if(str[i]==')')
            cnt++;
        else if(str[i]=='(')
            cnt--;
        else if(cnt==0){
            if(str[i]=='^'){
                express left=analysis(str.substr(0,i));
                express right=analysis(str.substr(i+1));
                map<string,int> msi;
                msi[left[0].second.begin()->first]=right[0].first;
                res.push_back(make_pair(1,msi));
                return res;
            }
        }
    }
    return res;
}

int main(){
    string teacher;
    while(getline(cin,teacher)&&teacher!="."){
        teacher=processSpace(teacher);
        vector<pair<int,map<string,int> > > t=analysis(teacher);
        sort(t.begin(),t.end());
        string student;
        while(getline(cin,student)&&student!="."){
            student=processSpace(student);
            vector<pair<int,map<string,int> > > s=analysis(student);
            sort(s.begin(),s.end());
            if(s==t)
                cout<<"yes"<<endl;
            else
                cout<<"no"<<endl;
        }
        cout<<"."<<endl;
    }
    return 0;
}