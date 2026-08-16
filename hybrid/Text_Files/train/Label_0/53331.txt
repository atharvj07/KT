import java.util.Scanner;

/**
 *
 * @author Acer
 */
public class ExcitingBets {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while(T-- > 0){
            long a = sc.nextLong();
            long b = sc.nextLong();
            if(a==b){
                System.out.println(0+" "+0);
            }
            else{
                long gcd = Math.abs(a-b);            
                long rem = a%gcd;
                long step = Math.min(rem, gcd-rem);
                System.out.println(gcd+" "+step);
            }
        }
    }
    
}