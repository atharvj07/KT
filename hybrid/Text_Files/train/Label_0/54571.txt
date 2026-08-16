import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    String s = sc.nextLine();
    sc.close();
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
      int charCode = (s.codePointAt(i) - 65 + n) % 26;
      sb.append(Character.toChars(charCode + 65));
    }
    System.out.println(sb.toString());
  }
}
