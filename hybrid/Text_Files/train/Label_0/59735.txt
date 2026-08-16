import java.util.*;
public  class Main{
    public static void eraseZero(int n,String s){
        int cnt = 0;
        int ans = 0;
        int f = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '1'){
                f = 1;
                ans += cnt;
                cnt = 0;
            }
            if(s.charAt(i) == '0' && f==1){
                cnt++;
            }
 
        }
        System.out.println(ans);
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        String str[]=new String[n];
        for(int i=0;i<n;i++){
            str[i]=sc.next();
        }
        for(int i=0;i<n;i++){
            eraseZero(n,str[i]);
        }
    }
}
   				 										   		 		 		