import java.util.*;

public class C {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String s = scanner.next();
    int res = 0;
    Deque<Character> st = new ArrayDeque<>();
    for (int i = 0; i < s.length(); i++) {
      char chr = s.charAt(i);
      if (chr == '<' || chr == '[' || chr == '{' || chr == '(') {
        st.push(chr);
      } else {
        if (st.size() == 0) {
          System.out.println("Impossible");
          return;
        }
        char schr = st.pop();
        if (!((schr == '<' && chr == '>') || (schr == '[' && chr == ']') || (schr == '{' && chr == '}') || (schr == '(' && chr == ')'))) {
          res++;
        }
      }
    }
    if (st.size() != 0) {
      System.out.println("Impossible");
    } else {
      System.out.println(res);
    }
  }
}