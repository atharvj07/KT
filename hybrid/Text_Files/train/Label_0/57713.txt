import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int E = sc.nextInt();
            int Y = sc.nextInt();

            if ( E == 0 ) {
                Y -= 1867;
                if ( Y <= 44 ) {
                    System.out.println("M" + Y);
                    continue;
                }
                Y -= 44;
                if ( Y <= 14 ) {
                    System.out.println("T" + Y);
                    continue;
                }
                Y -= 14;
                if ( Y <= 63 ) {
                    System.out.println("S" + Y);
                    continue;
                }
                Y -= 63;
                System.out.println("H" + Y);
            } else {
                Y += 1867;
                if ( E > 1 ) {
                    Y += 44;
                }
                if ( E > 2 ) {
                    Y += 14;
                }
                if ( E > 3 ) {
                    Y += 63;
                }
                System.out.println(Y);
            }
        }
    }
}

