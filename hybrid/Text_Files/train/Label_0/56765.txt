import java.util.*;

class Main {
    public static void main(final String[] args) {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      Set<Integer> d = new TreeSet<>();
      for (int i=0;i<n;i++) {
        int x = sc.nextInt();
        d.add(x);
      }
      System.out.println(d.size());
    }
}