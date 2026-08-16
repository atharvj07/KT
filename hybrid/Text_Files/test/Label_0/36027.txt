import java.util.Scanner;

/**
 *
 * @author ZEZOmaster
 */
public class SystemofEquations {

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int counter = 0;
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 33; j++) {
                if (Math.pow(i, 2) + j == n && Math.pow(j, 2) + i == m) {
                    counter++;
                }
            }
        }
        System.out.println(counter);
    }
}