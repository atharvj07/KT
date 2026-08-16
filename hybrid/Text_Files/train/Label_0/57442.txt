import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int N, K;
        String S;
        
        Scanner scanner = new Scanner(System.in);
        N = Integer.valueOf(scanner.nextLine());
        S = scanner.nextLine();
        K = Integer.valueOf(scanner.nextLine()) - 1;
        scanner.close();
        
        char[] c = S.toCharArray();
        char targetChar = c[K];

        for (int i = 0; i < N; i++) {
            if (c[i] != targetChar ) {
                c[i] = '*';
            }
        }

        System.out.println(String.valueOf(c));
    }
    
}