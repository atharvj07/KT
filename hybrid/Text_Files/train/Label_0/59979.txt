import java.util.Scanner;

/**
 * Created by paz on 17-3-18.
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        long sum = 0;
        for(int i = 1; ;i++) {
            sum += i;
            if(sum >= x) {
                System.out.println(i);
                break;
            }
        }
    }
}