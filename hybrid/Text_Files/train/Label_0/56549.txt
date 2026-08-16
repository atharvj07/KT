import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int ans = 0;
        if(a < b) {
            ans = b - a - w;
        } else if(a > b) {
            ans = a - b - w;
        }
        if(ans < 0) {
            ans = 0;
        }
        System.out.println(ans);
    }
}
