import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        while (true) {
            int n = sc.nextInt();
            if (n == 0) {
                break;
            }
            int count = 0;
            for (int i = 0; i < n / 4; i++) {
                count += sc.nextInt();
            }
            sb.append(count).append("\n");
        }
        System.out.print(sb);
    }
}
