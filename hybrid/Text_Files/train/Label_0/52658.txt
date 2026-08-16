import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();

        if (m < n - 1) {
            System.out.println("Impossible");
            System.exit(0);
        }

        int s = 0;
        boolean possible = false;
        int[] a = new int[200000];
        int[] b = new int[200000];

        for (int i = 1; i <= n; ++i) {
            for (int j = i + 1; j <= n; ++j)
                if (1 == gcd(j, i)) {
                    ++s;
                    a[s] = i;
                    b[s] = j;
                }
            if (s >= m) {
                possible = true;
                break;
            }
        }

        if (possible) {
            System.out.println("Possible");
            for (int i = 1; i <= m; ++i)
                System.out.println(a[i] + " " + b[i]);
        } else {
            System.out.println("Impossible");
        }
    }


    public static int gcd(int a, int b) {
        if (a % b == 0)
            return b;
        else
            return gcd(b, a % b);
    }



}
