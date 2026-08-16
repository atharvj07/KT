public class Dominoes {

    public static void main(String... BiCola) {
        java.util.Scanner in = new java.util.Scanner(System.in);

        int n = in.nextInt();

        if (n % 2 == 0) {
            for (int i = 0; i < n; i++) {
                System.out.print(i % 4 < 2 ? 'a' : 'b');
            } // for
            System.out.println();
            for (int i = 0; i < n; i++) {
                System.out.print(i % 4 < 2 ? 'c' : 'd');
            } // for
            System.out.println();
            System.out.print('e');
            for (int i = 2; i < n; i++) {
                System.out.print(i % 4 < 2 ? 'g' : 'h');
            } // for
            System.out.print('f');
            System.out.println();
            System.out.print('e');
            for (int i = 2; i < n; i++) {
                System.out.print(i % 4 < 2 ? 'i' : 'j');
            } // for
            System.out.print('f');
            System.out.println();
        } else {
            System.out.print('a');
            for (int i = 0; i < n - 1; i++) {
                System.out.print(i % 4 < 2 ? 'b' : 'c');
            } // for
            System.out.println();
            System.out.print('a');
            for (int i = 0; i < n - 1; i++) {
                System.out.print(i % 4 < 2 ? 'e' : 'd');
            } // for
            System.out.println();
            for (int i = 0; i < n - 1; i++) {
                System.out.print(i % 4 < 2 ? 'f' : 'g');
            } // for
            System.out.print('h');
            System.out.println();
            for (int i = 0; i < n - 1; i++) {
                System.out.print(i % 4 < 2 ? 'i' : 'j');
            } // for
            System.out.print('h');
            System.out.println();
        } // else

    } // main

} // Dominoes
