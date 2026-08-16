
import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        Scanner ss = new Scanner(System.in);
        int q = ss.nextInt();

        for (int i = 0; i < q; i++) {
            int l1 = ss.nextInt();
            int r1 = ss.nextInt();
            int l2 = ss.nextInt();
            int r2 = ss.nextInt();
            
            System.out.print(l1+" ");
            if(l2!=l1)
            {
                System.out.print(l2);
            }
            else{
                l2++;
                System.out.print(l2);
            }
            System.out.println("");

        }

    }
}
