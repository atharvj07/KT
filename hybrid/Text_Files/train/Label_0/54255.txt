import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String o = sc.next();
        String e = sc.next();
        int n = o.length() + e.length();
        for(int i = 1; i <= n; i++){
            if(i % 2 == 1){
                System.out.print(o.charAt((i-1)/2));
            } else {
                System.out.print(e.charAt((i-1)/2));
            }
        }
    }
}