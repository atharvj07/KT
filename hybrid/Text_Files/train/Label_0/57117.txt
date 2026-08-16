import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(true){
            int N = sc.nextInt();
            int M = sc.nextInt();
            if(N == 0)break;
            int ans = 0;
            int price = M / N;
            for(int i = 0 ; i < N ; i++){
                int a = sc.nextInt();
                if(a < price)
                    ans += a;
                else
                    ans += price;
            }
            System.out.println(ans);
        }
    }
}
