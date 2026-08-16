
import java.util.Scanner;

public class Main
{

    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);

        double a = scan.nextDouble();

        System.out.printf("%.8f %.8f\n", a * a * Math.PI, (a * 2) * Math.PI);

    }
}

