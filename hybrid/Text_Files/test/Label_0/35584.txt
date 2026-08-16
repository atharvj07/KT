import java.io.PrintStream;
import java.util.Scanner;

public class Main {
    private static final PrintStream so = System.out;
    private static final Scanner     sc = new Scanner(System.in);

    public static void main(String[] args) {
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            if (sc.nextInt() % 2 == 1) {
                so.println("first");
                return;
            }
        }
        so.println("second");
    }
}
