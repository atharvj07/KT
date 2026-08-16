import java.util.*;
public class M {
    public static void main(String[] Args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = 0;
        for(int k =0;k<n;k++)
            t+=sc.nextInt();
        int ans = 0;
        for(int k = 1;k<=5;k++){
            if((k+t)%(n+1)!=1){
                ans++;
            }
        }
        System.out.println(ans);
    }
}
