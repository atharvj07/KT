import java.util.Scanner;

public class C765 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int K = in.nextInt();
        int A = in.nextInt();
        int B = in.nextInt();
        int sets = A/K + B/K;
        if ((A%K != 0 && B < K) || (B%K != 0 && A < K)) {
            sets = -1;
        }
        System.out.println(sets);
    }

}
