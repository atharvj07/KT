import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] t = new int[n];
        for (int i = 0; i < n; i++) {
            t[i] = sc.nextInt();
        }
        int maxValue = Arrays.stream(t).max().getAsInt();
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 1; i <= maxValue; i++) {
            if(maxValue % i == 0) set.add(i);
        }
        long ans = 0;
        for (int num: t) {
            ans += set.ceiling(num) - num;
        }
        System.out.println(ans);
    }
}
