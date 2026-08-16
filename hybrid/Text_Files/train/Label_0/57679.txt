import java.util.HashSet;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();

        for(int i=0; i<t; i++) {
            HashSet<Integer> numbers = new HashSet<>();
            int n = input.nextInt();
            for(int j=0; j<n; j++)
                numbers.add(input.nextInt());
            System.out.println(numbers.size());
        }
    }
}


