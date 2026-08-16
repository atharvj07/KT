import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        String text;
        int count = 0;
        while (!(text=sc.next()).equals("END_OF_TEXT")) {
            if (text.toLowerCase().equals(word)) count++;
        }
        System.out.println(count);
    }
}

