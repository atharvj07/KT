import java.util.Scanner;

public class P7 {
    public static void main(String[] arg) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int tot = a*c;
        int cont = 0;

        while(tot > 0){
            tot = tot -b;
            cont++;
        }

        tot = a*c;

        int f = 0;
        int cont2 = 0;

        while(f + c*b < tot){
            cont2++;
            f=f+b;
        }

        System.out.println(cont2);

    }
}
