import java.util.Scanner;

public class B639 {
    public static void main(String... xxx){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = sc.nextInt();
        int h = sc.nextInt();

        if ((n-1 < d) || (2*h < d) || (d < 1) || (h < 1) || ((d == 1) && (n > 2)))
            System.out.println("-1");
        else{
            int i;
            for(i = 1; i <= h;){
                System.out.println(i + " " + ++i);
            }
            if (i < n){
                int k = (d == h) ? 2 : 1;
                System.out.println(k + " " + ++i);
                for(; i <= d;){
                    System.out.println(i + " " + ++i);
                }
                for(; i < n;){
                    System.out.println(k + " " + ++i);
                }
            }
        }
    }
}
