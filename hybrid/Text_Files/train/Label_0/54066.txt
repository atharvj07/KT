import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        while(sc.hasNextLine()){
            String s = sc.nextLine();

            s = s.replaceAll("apple", "\n\n\n\n\n");
            s = s.replaceAll("peach", "apple");
            s = s.replaceAll("\n\n\n\n\n", "peach");

            System.out.println(s);
        }
    }
}