import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long ans = 0;
        for (int i=0;i<10;i++){
            for (int j=0;j<10;j++){
                int cij = 0;
                int cji = 0;
                for (int k=1;k<=n;k++){
                    String s = Integer.toString(k);
                    if (s.charAt(0)-'0'==i&&k%10==j)cij++;
                    if (s.charAt(0)-'0'==j&&k%10==i)cji++;
                }
                ans+=cij*(long)cji;
            }
        }
        System.out.println(ans);
    }
}
