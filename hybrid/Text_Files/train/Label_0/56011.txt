
import java.util.Scanner;

public class D {
    public static void main(String[] aaaa) {
        Scanner scanner = new Scanner(System.in);


        System.out.println("? 0 0");
        System.out.flush();

        int res = scanner.nextInt();
//        System.out.println("res " + res);


        int a = 0;
        int b = 0;
        for (int i = 29; i >= 0; i--) {
            int c = 0;
            int d = (a ^ b) + (1 << i);
            System.out.println("? " + c + " " + d);
            System.out.flush();
            int res1 = scanner.nextInt();
            //int res2 = scanner.nextInt();

            c = (a ^ b) + (1 << i);
            d = 0;
            System.out.println("? " + c + " " + d);
            System.out.flush();
            int res2 = scanner.nextInt();
            //int res4 = scanner.nextInt();
            int newres = 0;

            if (res >= 0 && res1 >=0 && res2 >= 0) {
                a += (1 << i);
                //b += (1 << i);
                newres = 1;
            }
            if (res >= 0 && res1 >=0 && res2 < 0) {
                a += (1 << i);
                b += (1 << i);
                newres = 1;
            }
            if (res >= 0 && res1 < 0 && res2 >= 0) {
                //a += (1 << i);
                //b += (1 << i);
                newres = 1;
            }
            if (res >= 0 && res1 < 0 && res2 < 0) {
                a += (1 << i);
                //b += (1 << i);
                newres = -1;
            }
            if (res < 0 && res1 >=0 && res2 >= 0) {
                //a += (1 << i);
                b += (1 << i);
                newres = 1;
            }
            if (res < 0 && res1 >=0 && res2 < 0) {
                a += (1 << i);
                b += (1 << i);
                newres = -1;
            }
            if (res < 0 && res1 < 0 && res2 >= 0) {
                //a += (1 << i);
                //b += (1 << i);
                newres = -1;
            }
            if (res < 0 && res1 < 0 && res2 < 0) {
                //a += (1 << i);
                b += (1 << i);
                newres = -1;
            }
//            System.out.println("res " + res + " a " + a + " b " + b);
            res = newres;


            //System.out.println("? 0 0");
        }
        System.out.println("! " + a + " " + b);







    }
}
