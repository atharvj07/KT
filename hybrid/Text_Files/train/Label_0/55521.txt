import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        String S = scan.next();
        String T = scan.next();
        boolean answer = solve(S, T);
        System.out.println(answer ? "Yes" : "No");
    }
    private static boolean solve(String S, String T) {
        String double_S = S + S;
        return double_S.indexOf(T) >= 0;
    }
}
