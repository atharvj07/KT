import java.util.*;

public class Main
{
    public static void main(String[] arqs)
    {
        Scanner scan = new Scanner(System.in);
        String cols = "ROYGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIVGBIV";

        int n = scan.nextInt();

        System.out.println(cols.substring(0, n));
    }
}