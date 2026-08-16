
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long N = scan.nextInt();
        long P = scan.nextInt();
        long Q = scan.nextInt();
        long C[] = new long[(int)N];
        long ans = 0;
        for(int i = 0; i < N; i++){
            long num = scan.nextInt();
            C[i] = (Q - i) * P - num;
            ans += num;
        }
        Arrays.sort(C);
        long S = ans;
        for(int i = 0; i < N; i++){
            S += C[(int)N - i - 1];
            S += i * P * 2;
            ans = Math.max(ans, S);
        }
        System.out.println(ans);
    }
}
