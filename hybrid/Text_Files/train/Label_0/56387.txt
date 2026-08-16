import java.util.Scanner;

public class C {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        for (int i = 1; i > 0; i--) solve(scan);
    }

    protected static void solve(Scanner scan) {
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[] a = new int[n];
        int[] b = new int[m];

        for (int i = 0; i < n; i++) {
            a[i] = scan.nextInt();
        }

        for (int i = 0; i < m; i++) {
            b[i] = scan.nextInt();
        }

        int i = 0;

        for (; i < 2 << 9; i++) {
            boolean af = false;
            for (int j : a) {
                af = false;
                for (int k : b) {
                    if ((i | (j & k)) == i) {
                        af = true;
                        break;
                    }
                }
                if (!af) {
                    break;
                }
            }
            if (af) break;
        }


        System.out.println(i);
    }
}