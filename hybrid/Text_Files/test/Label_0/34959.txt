import java.math.BigDecimal;
import java.util.*;

public class Main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        long X = sc.nextLong();

        if (X <= 6) {
            System.out.println(1);
        } else {
            long numOfSet = X / 11; // set is (6, 5)
            long remain = X % 11;
            if (remain == 0) {
                System.out.println(2 * numOfSet);
            } else if (remain <= 6) {
                System.out.println(2 * numOfSet + 1);
            } else {
                System.out.println(2 * numOfSet + 2);
            }
        }
    }
}