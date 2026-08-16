import java.util.*;

public class C_A_Cookie_for_You{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        while (q-- > 0) {
            long a=sc.nextLong();
            long b=sc.nextLong();
            long n=sc.nextLong();
            long m=sc.nextLong();
            n-=Math.abs(a-b);
            boolean f=true;
            long min=Math.min(a,b);
            if(min<m)
            {
                f=false;
            }
            if((2*min-m)<n)
            {
                f=false;
            }
            if(f)
            {
                System.out.println("Yes");
            }
            else
            {
                System.out.println("No");
            }
        }
    }
}