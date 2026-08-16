import java.io.*;

public class Main {

    public static void main(String[] argv) throws IOException {
        //*
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String s = in.readLine();
            if (s == null) {
                break;
            }
            f(s);
        }
        //*/
    }

    public static void f(String s) {
        double a = 0;
        try {
            a = Double.parseDouble(s);
            if (a < 1.0 || 10.0 < a) {
                return;
            }
        } catch (NumberFormatException numberFormatException) {
            return;
        }
        double sum = a;
        for (int i = 2; i <= 10; i++) {
            if (i % 2 == 0) {
                a *= 2;
            } else {
                a /= 3;
            }
            sum += a;
        }
        System.out.printf("%.8f\n", sum);
    }
}