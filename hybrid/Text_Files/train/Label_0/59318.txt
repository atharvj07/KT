import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

// MainT1P2018C
public class Main {

    private static boolean isOdd(int val) {
        return ((val & 1) != 0);
    }

    public static void main(String[] args) {
        try (
                Scanner in = new Scanner(System.in);
                PrintWriter out = new PrintWriter(System.out))
        {
            final int N = in.nextInt();
            final int[] A = new int[N];
            Arrays.setAll(A, i -> Integer.parseInt(in.next()));

            final int halfN = N / 2;
            long result = 0L;
            Arrays.sort(A);
            if (isOdd(N)) {

                long r1 = 0L;
                r1 -= 2 * Arrays.stream(A, 0, halfN).asLongStream().sum();
                r1 += 2 * Arrays.stream(A, halfN, N).asLongStream().sum();
                r1 -= A[halfN];
                r1 -= A[halfN + 1];

                long r2 = 0L;
                r2 -= 2 * Arrays.stream(A, 0, halfN + 1).asLongStream().sum();
                r2 += 2 * Arrays.stream(A, halfN + 1, N).asLongStream().sum();
                r2 += A[halfN - 1];
                r2 += A[halfN];

                result = Math.max(r1, r2);

            } else {
                result -= 2 * Arrays.stream(A, 0, halfN).asLongStream().sum();
                result += 2 * Arrays.stream(A, halfN, N).asLongStream().sum();
                result += A[halfN - 1];
                result -= A[halfN];
            }
            out.println(result);
        }
    }
}
