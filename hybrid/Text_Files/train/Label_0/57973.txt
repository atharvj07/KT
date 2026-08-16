import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner in=new Scanner(System.in);
        float d=in.nextFloat(),t=in.nextFloat(),s=in.nextFloat();
        if((d/s)<=t)
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}