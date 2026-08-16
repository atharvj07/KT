import java.util.Scanner;

public class Platforms18B {
    public static void main(String[] args) {
        long n,d,m,l;

        Scanner scanner = new Scanner(System.in);
        n = scanner.nextLong();
        d = scanner.nextLong();
        m = scanner.nextLong();
        l = scanner.nextLong();
        if (m-l == 1) {
            long x = (n*m -1)/d;
            System.out.println(d*(x+1));
        } else {
            System.out.println(findFallDown(n,d,m,l));
        }
    }

    static long findFallDown(long n, long d, long m, long l) {
        long k = 1;
        long nextMove = d;
        while (k <= n) {
            long left = (k-1) * m;
            if (nextMove < left) {
                return nextMove;
            }
            long right = left + l;
            while (nextMove >= left && nextMove <= right) {
                nextMove += d;
            }
            k++;
        }
        return nextMove;
    }
}
