import java.util.*;
public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        long x = (a/500)*1000;
        x+=((a%500)/5)*5;
        System.out.println(x);
    }
}