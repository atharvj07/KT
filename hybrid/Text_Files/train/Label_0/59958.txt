import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int a = sc.nextInt();
            int l = sc.nextInt();
            if (a == 0 && l == 0) break;
            List<Integer> list = new ArrayList<Integer>();
            for (int i = 1; i <= 20; i++) {
                list.add(a);
                char[] chars = String.format("%0"+ l + "d", a).toCharArray();
                Arrays.sort(chars);
                String small = new String(chars);
                String big = new StringBuilder(small).reverse().toString();
                a = Integer.parseInt(big) - Integer.parseInt(small);
                int j = list.indexOf(a);
                if (j != -1) {
                    System.out.println(j + " " + a + " " + (i-j));
                    break;
                }
            }
        }
        sc.close();
    }
}