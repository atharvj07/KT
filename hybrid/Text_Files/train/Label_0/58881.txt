import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] e = new int[4];
        for(int i = 0; i < 4; i++) {
            e[i] = sc.nextInt();
        }
        Arrays.sort(e);

        System.out.println(e[0] + e[2] == e[1] + e[3] ? "yes" : "no");
    }
}