import java.util.Scanner;


public class Main {

    public static int cnta[]=new int[26];
    public static int cntb[]=new int[26];
    public static int cntc[]=new int[26];
    public static StringBuilder res;
    public static void main(String[] args) {
        Scanner cin=new Scanner(System.in);
        String a=cin.nextLine(),b=cin.nextLine(),c=cin.nextLine();
        
        for(int i=0;i<26;i++){
            cnta[i]=cntb[i]=cntc[i]=0;
        }
        for(int i=0;i<a.length();i++){
            cnta[a.charAt(i)-'a']++;
        }
        for(int i=0;i<b.length();i++){
            cntb[b.charAt(i)-'a']++;
        }
        for(int i=0;i<c.length();i++){
            cntc[c.charAt(i)-'a']++;
        }
        int maxn=0,f=0,s=0;
        for(int i=0;i<=a.length()/b.length();i++){
            if(judge(i)){
                int other=100000;
                for(int j=0;j<26;j++){
                    if(cntc[j]==0)continue;
                    other=Math.min(other, (cnta[j]-cntb[j]*i)/cntc[j]);
                    if(other==0)break;
                }
                if(i+other>maxn){
                    maxn=i+other;
                    f=i;
                    s=other;
                }
            }
        }
		res=new StringBuilder();
        for(int i=0;i<f;i++){
            res.append(b);
        }
        for(int i=0;i<s;i++){
            //System.out.print(c);
            res.append(c);
        }
        for(int i=0;i<26;i++){
            cnta[i]-=cntb[i]*f;
            cnta[i]-=cntc[i]*s;
        }
        for(int i=0;i<26;i++){
            for(int j=0;j<cnta[i];j++)
                res.append((char)(i+'a'));
        }
        System.out.println(res.toString());
        //cin.close();
    }
    public static boolean judge(int x){
        for(int i=0;i<26;i++){
            if(cntb[i]*x>cnta[i])return false;
        }
        return true;
    }

}