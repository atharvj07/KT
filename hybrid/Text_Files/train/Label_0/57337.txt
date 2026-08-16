import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int H1 = sc.nextInt();
        int M1 = sc.nextInt();
        int H2 = sc.nextInt();
        int M2 = sc.nextInt();
        int K = sc.nextInt();
        sc.close();


        int H = (H2 - H1) * 60;
        int M = (M1 - M2);

        int result = H - M - K;

        System.out.println(result);

    }
}