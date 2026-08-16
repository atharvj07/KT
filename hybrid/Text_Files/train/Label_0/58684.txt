import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int num1, num2;
        StringBuilder in1 = new StringBuilder();
        StringBuilder in2 = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        num1 = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < num1; i++) {
            in1.append(sc.nextInt());
            //System.out.println(in1);
        }

        num2 = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < num2; i++) {
            in2.append(sc.nextInt());
            //System.out.println(in2);
        }

        if (in1.toString().compareTo(in2.toString()) >= 0)
            System.out.println(0);
        else
            System.out.println(1);

    }

}
