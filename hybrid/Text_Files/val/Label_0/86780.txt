import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = sc.nextInt();
    String S = sc.next();
    
    int zeroSeqCount = 0;
    int tail = 0;
    // set initial tail
    while (tail < N) {
      char c = S.charAt(tail);
      if (c == '0') {
        zeroSeqCount++;
        if (zeroSeqCount == K+1) {
          break;
        }
        tail++;
        while (tail < N && S.charAt(tail) == '0') {
          tail++;
        }
      } else {
        tail++;
      }
    }
    if (tail == N) {
      System.out.println(N);
      return;
    }

    int head = 0;
    int max = tail - head;
    while (tail < N) {

      //
      // move tail
      //

      // skip seq 0
      while (tail < N && S.charAt(tail) == '0') {
        tail++;
      }
      // move to head of next 0 seq
      while (tail < N && S.charAt(tail) != '0') {
        tail++;
      }
      
      //
      // move head
      //
      while (head < tail && S.charAt(head) != '0') {
        head++;
      }
      while (head < tail && S.charAt(head) == '0') {
        head++;
      }
      
      max = Math.max(max, tail-head);
    }
    
    System.out.println(max);
  }  
}