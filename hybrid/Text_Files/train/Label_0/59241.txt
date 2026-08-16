import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int min = 2000001;
        int count = 0;
        for (int i = 0; i < n; i++) {
            int tmp = sc.nextInt();
            if (min > tmp) {
                min = tmp;
                count++;
            }
        }
        System.out.println(count);
    }
}