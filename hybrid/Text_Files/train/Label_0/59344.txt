import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Integer[] num = new Integer[n];
        boolean isNumber = true;
        for (int i = 0; i < m; i++) {
            sc.nextLine();
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (num[a-1] == null || num[a-1] == b) {
                num[a-1] = b;
            } else {
                isNumber = false;
                break;
            }
        }
        if (isNumber) {
            if ((n != 1 && num[0] != null && num[0] == 0)) {
                System.out.println("-1");
            } else {
                if (n != 1 && num[0] == null) {
                    num[0] = 1;
                }
                for (int i = 0; i < n; i++) {
                    System.out.print(num[i] != null ? num[i] : 0);
                }
                System.out.println();
            }
        } else {
            System.out.println("-1");
        }
    }
}
