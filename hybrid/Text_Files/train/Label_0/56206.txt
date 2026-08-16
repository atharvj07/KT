import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        StringBuilder S = new StringBuilder(sc.next());
        int count = 0;

        for (int i = 1; i < S.capacity() - 16; i++) {
            if (S.charAt(i) == S.charAt(i - 1)) {
                count++;
            }
        }

        System.out.println(Math.min(count + K * 2, N - 1));
    }
}