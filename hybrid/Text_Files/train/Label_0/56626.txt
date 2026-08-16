import java.util.*;
 
public class Main{
	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int ans = 999;
        for(int i = 0; i < s.length() - 2; i++){
        	String str = s.substring(i, i + 3);
            int n = Integer.parseInt(str);
            n = 753 - n;
            if(Math.abs(n) < ans){
            	ans = Math.abs(n);
            }
        }
        System.out.println(ans);
    }
}