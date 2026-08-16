import java.util.Scanner;

public class CF1065B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        long n = scanner.nextInt();
        long m = scanner.nextLong();

        double denseVertexes = Math.ceil((Math.sqrt(8 * m + 1) + 1) / 2);
        long denseVertexes1 = (long) denseVertexes;
        long max = n - (denseVertexes1 == 1 ? 0 : denseVertexes1);
        long min = n > 2 * m ? n - 2 * m : 0;
        System.out.println(String.format("%d %d", min, max));
    }
}
