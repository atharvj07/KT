import java.util.Scanner;

public class Main {
    public static void main(String [] args) {
        int posCC, posR;
        Scanner scan = new Scanner(System.in);
        posCC = scan.nextInt();
        posR = scan.nextInt();

        int prizeMoney = 0;

        int [] prizeAmt = {300000, 200000, 100000};
        if (posCC < 4) {
            prizeMoney += prizeAmt[posCC - 1];
        }
        if (posR < 4) {
            prizeMoney += prizeAmt[posR - 1];
        }
        if (posCC == 1 && posR == 1)
            prizeMoney += 400000;

        System.out.println(prizeMoney);
    }
}