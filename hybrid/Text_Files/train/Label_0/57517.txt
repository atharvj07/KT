import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long b = 1;
        long a = 0;
        for (int i = 0; i < n; i++) {
            int q = sc.nextInt();
            int x = sc.nextInt();
            if (q == 1) {
                b *= x;
                a *= x;
            } else if (q == 2) {
                a -= x;
            } else {
                a += x;
            }
        }
        System.out.println(a + " " + b);
    }
}

