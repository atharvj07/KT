import java.util.*;
public class Main {

    public static void main(String[] args) {
        //data input
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        long ct = 0;

        for (int i = 1; i < n; i++) {
            int m = n - i;
            if (m <= i) break;
            if (m + i == n) ct++;
        }

        System.out.println(ct);
    }
}