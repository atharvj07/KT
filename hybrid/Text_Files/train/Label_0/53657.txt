import java.math.BigInteger;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    ArrayList<BigInteger> a = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      a.add(new BigInteger(sc.next()));
    }
    a.sort(Comparator.comparing(BigInteger::longValue).reversed());
    if (n == 2) {
      System.out.println(a.get(0));
      return;
    }
    BigInteger result = a.get(0);
    for (int i = 2; i < n; i++) {
      result = result.add(a.get(i / 2));
    }
    System.out.println(result);
  }
}
