
import java.util.Scanner;

public class Three {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        long n = s.nextLong();
        long[] a = new long[(int) n];
        long[] b = new long[(int) n];
        for (long i = 0; i < n; i++) {
            a[(int) i] = s.nextLong();
            b[(int) i] = a[(int) i];
        }

        if(n==1)
        {
            System.out.println(1+" "+1);
            System.out.println((-a[(int)0]));
            System.out.println(1+" "+1);
            System.out.println(0);
            System.out.println(1+" "+1);
            System.out.println(0);
        }
        else {
            //step 1
            System.out.println(1 + " " + (n - 1));
            for (long i = 0; i < n - 1; i++) {
                System.out.print(((n - 1) * a[(int) i]) + " ");
                a[(int) i] += ((n - 1)) * a[(int) i];
            }
            System.out.println();

            //step 2
            System.out.println(n + " " + n);
            for (long i = n - 1; i < n; i++) {
                System.out.print((-a[(int) i]) + " ");
                a[(int) i] = a[(int) i] + (-1) * b[(int) i];
            }
            System.out.println();


            //step 3
            System.out.println(1 + " " + n);
            for (long i = 0; i < n; i++) {
                System.out.print((-a[(int) i]) + " ");
                a[(int) i] = a[(int) i] + -a[(int) i];
            }
        }

    }
}
