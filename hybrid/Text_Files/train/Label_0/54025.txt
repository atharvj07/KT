import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();
        long ans = 0;
        int min = Math.min(x,y);
        if(a+b >= c*2){
            ans += min * 2 * c;
            
        }else{
            ans += min * (a + b);
        }
        x -= min;
        y -= min;
        if(x > 0){
            ans += Math.min(a,c*2) * x;
        }else if(y > 0){
            ans += Math.min(b,c*2) * y;
        }
        System.out.println(ans);
    }
}
