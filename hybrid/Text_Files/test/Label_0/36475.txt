import java.util.*;
public class Solution{
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int T  = sc.nextInt();
        while(T-->0){
            String s = sc.next();
            int n = s.length();
            String ans = "10";
            boolean check = true;
            char ch = s.charAt(0);
            for(int i=1;i<n;i++){
                if(check && ch ==s.charAt(i)){
                    check = true;
                }
                else
                    check =false;
                ans += "10";
            }
            if(check){
                System.out.println(s);
                continue;
            }
            System.out.println(ans);
        }
    }
}