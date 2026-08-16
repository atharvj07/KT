import java.math.BigDecimal;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // TODO 自動生成されたメソッド・スタブ

        Scanner sc = new Scanner(System.in);
        BigDecimal one = new BigDecimal(1);

        BigDecimal r1 = new BigDecimal(sc.nextInt());
        BigDecimal r2 = new BigDecimal(sc.nextInt());

        r1 = one.divide(r1,12,BigDecimal.ROUND_UP );
        r2 = one.divide(r2,12,BigDecimal.ROUND_UP );
        BigDecimal r3 = r1.add(r2);
        r3 = one.divide(r3,12,BigDecimal.ROUND_UP);
        System.out.println(r3);

    }

}
